from __future__ import annotations

import json
from contextlib import contextmanager
from datetime import date, datetime, time, timedelta

from sqlalchemy import DateTime, Float, ForeignKey, Integer, String, Text, UniqueConstraint, create_engine, inspect, select, text
from sqlalchemy.orm import Mapped, Session, joinedload, mapped_column, relationship, sessionmaker

from ptit_reflex.config import DATA_DIR
from ptit_reflex.db import Base
from ptit_reflex.models import (
    CriterionGroup,
    Criterion,
    Event,
    EventParticipation,
    ParticipationStatus,
    ScoreEntry as LegacyScoreEntry,
    Semester,
    Submission as LegacySubmission,
    User,
    UserRole,
)
from ptit_reflex.services.evaluation_service import (
    approve_event_participation,
    get_active_events,
    get_criteria_tree,
    get_semesters,
    submit_event_participation,
)
from ptit_reflex.services.evidence_files import delete_evidence_upload, is_image_file, resolve_evidence_upload
from ptit_reflex.services.seed import CRITERION_BLUEPRINT, seed_default_data


def _store_password_plain(password: str) -> str:
    """Demo bài tập: lưu mật khẩu dạng plaintext (cột vẫn tên password_hash)."""
    return password


def _password_matches(plain: str, stored: str | None) -> bool:
    return plain == (stored or "")


DEFAULT_ADVISOR_USERNAME = "CVHT001"
DEFAULT_ADMIN_USERNAME = "admin"
REFLEX_DATABASE_PATH = DATA_DIR / "reflex_student_conduct.db"
REFLEX_DATABASE_URL = f"sqlite:///{REFLEX_DATABASE_PATH.as_posix()}"


def current_app_time() -> datetime:
    return datetime.now().astimezone().replace(tzinfo=None, microsecond=0)


class ReflexSubmission(Base):
    __tablename__ = "reflex_submissions"
    __table_args__ = (UniqueConstraint("student_id", "semester_id", name="uq_reflex_student_semester"),)

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    student_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    semester_id: Mapped[int] = mapped_column(ForeignKey("semesters.id"))
    status: Mapped[str] = mapped_column(String(40), default="draft")
    self_total: Mapped[float] = mapped_column(Float, default=0.0)
    class_total: Mapped[float] = mapped_column(Float, default=0.0)
    advisor_total: Mapped[float] = mapped_column(Float, default=0.0)
    student_note: Mapped[str] = mapped_column(Text, default="")
    class_note: Mapped[str] = mapped_column(Text, default="")
    advisor_note: Mapped[str] = mapped_column(Text, default="")
    submitted_at: Mapped[datetime | None] = mapped_column(DateTime, nullable=True)
    class_reviewed_at: Mapped[datetime | None] = mapped_column(DateTime, nullable=True)
    advisor_reviewed_at: Mapped[datetime | None] = mapped_column(DateTime, nullable=True)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    student: Mapped[User] = relationship()
    semester: Mapped[Semester] = relationship()
    scores: Mapped[list["ReflexScore"]] = relationship(
        back_populates="submission",
        order_by="ReflexScore.id",
        cascade="all, delete-orphan",
    )


class ReflexScore(Base):
    __tablename__ = "reflex_scores"
    __table_args__ = (UniqueConstraint("submission_id", "criterion_id", name="uq_reflex_submission_criterion"),)

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    submission_id: Mapped[int] = mapped_column(ForeignKey("reflex_submissions.id"))
    criterion_id: Mapped[int] = mapped_column(ForeignKey("criteria.id"))
    self_score: Mapped[float] = mapped_column(Float, default=0.0)
    class_score: Mapped[float] = mapped_column(Float, default=0.0)
    advisor_score: Mapped[float] = mapped_column(Float, default=0.0)
    student_comment: Mapped[str] = mapped_column(Text, default="")
    class_feedback: Mapped[str] = mapped_column(Text, default="")
    advisor_feedback: Mapped[str] = mapped_column(Text, default="")

    submission: Mapped[ReflexSubmission] = relationship(back_populates="scores")
    criterion: Mapped[Criterion] = relationship()


class ReflexEvidence(Base):
    __tablename__ = "reflex_evidences"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    student_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    created_by_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    semester_id: Mapped[int] = mapped_column(ForeignKey("semesters.id"))
    category_key: Mapped[str] = mapped_column(String(60))
    summary: Mapped[str] = mapped_column(String(255))
    payload_json: Mapped[str] = mapped_column(Text, default="{}")
    status: Mapped[str] = mapped_column(String(40), default="pending_class")
    class_feedback: Mapped[str] = mapped_column(Text, default="")
    advisor_feedback: Mapped[str] = mapped_column(Text, default="")
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    submitted_at: Mapped[datetime | None] = mapped_column(DateTime, nullable=True)
    class_reviewed_at: Mapped[datetime | None] = mapped_column(DateTime, nullable=True)
    advisor_reviewed_at: Mapped[datetime | None] = mapped_column(DateTime, nullable=True)

    student: Mapped[User] = relationship(foreign_keys=[student_id])
    creator: Mapped[User] = relationship(foreign_keys=[created_by_id])
    semester: Mapped[Semester] = relationship()


class ReflexSemesterMetric(Base):
    __tablename__ = "reflex_semester_metrics"
    __table_args__ = (UniqueConstraint("student_id", "semester_id", name="uq_reflex_student_semester_metric"),)

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    student_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    semester_id: Mapped[int] = mapped_column(ForeignKey("semesters.id"))
    gpa: Mapped[float] = mapped_column(Float, default=0.0)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    student: Mapped[User] = relationship()
    semester: Mapped[Semester] = relationship()


reflex_engine = create_engine(
    REFLEX_DATABASE_URL,
    echo=False,
    connect_args={"check_same_thread": False},
)
ReflexSessionLocal = sessionmaker(bind=reflex_engine, expire_on_commit=False)


def ensure_semester_stage_windows_column() -> None:
    try:
        cols = [c["name"] for c in inspect(reflex_engine).get_columns("semesters")]
    except Exception:
        return
    if "conduct_stage_windows_json" in cols:
        return
    with reflex_engine.begin() as conn:
        conn.execute(text("ALTER TABLE semesters ADD COLUMN conduct_stage_windows_json TEXT"))


def ensure_user_profile_columns() -> None:
    try:
        cols = {c["name"] for c in inspect(reflex_engine).get_columns("users")}
    except Exception:
        return
    column_defs = {
        "phone": "TEXT",
        "birth_date": "TEXT",
        "gender": "TEXT",
        "address": "TEXT",
    }
    missing = {name: sql for name, sql in column_defs.items() if name not in cols}
    if not missing:
        return
    with reflex_engine.begin() as conn:
        for name, sql_type in missing.items():
            conn.execute(text(f"ALTER TABLE users ADD COLUMN {name} {sql_type}"))


def ensure_event_detail_columns() -> None:
    try:
        cols = {c["name"] for c in inspect(reflex_engine).get_columns("events")}
    except Exception:
        return
    column_defs = {
        "start_time": "TEXT",
        "end_time": "TEXT",
        "location": "TEXT",
    }
    missing = {name: sql for name, sql in column_defs.items() if name not in cols}
    if not missing:
        return
    with reflex_engine.begin() as conn:
        for name, sql_type in missing.items():
            conn.execute(text(f"ALTER TABLE events ADD COLUMN {name} {sql_type}"))


DEFAULT_CONDUCT_STAGE_LABELS = [
    "Cập nhật, duyệt minh chứng",
    "Sinh viên đánh giá",
    "Ban cán sự đánh giá",
    "Chủ nhiệm lớp xác nhận",
]


TEXT_MAP = {
    "Quan tri he thong": "Quản trị hệ thống",
    "Cong nghe thong tin": "Công nghệ thông tin",
    "Ky thuat phan mem": "Kỹ thuật phần mềm",
    "He thong thong tin": "Hệ thống thông tin",
    "Hoc ky 1 nam hoc 2023 - 2024": "Học kỳ 1 năm học 2023 - 2024",
    "Hoc ky 2 nam hoc 2023 - 2024": "Học kỳ 2 năm học 2023 - 2024",
    "Hoc ky 1 nam hoc 2024-2025": "Học kỳ 1 năm học 2024-2025",
    "Hoc ky 2 nam hoc 2024-2025": "Học kỳ 2 năm học 2024-2025",
    "Hoc ky 1 nam hoc 2025-2026": "Học kỳ 1 năm học 2025-2026",
    "Hoc ky 2 nam hoc 2025-2026": "Học kỳ 2 năm học 2025-2026",
    "Tieu chi 1. Danh gia ve y thuc tham gia hoc tap": "Tiêu chí 1. Đánh giá về ý thức tham gia học tập",
    "Tieu chi 2. Danh gia ve y thuc chap hanh noi quy, quy che, quy dinh trong Hoc vien": "Tiêu chí 2. Đánh giá về ý thức chấp hành nội quy, quy chế, quy định trong Học viện",
    "Tieu chi 3. Danh gia ve y thuc va ket qua tham gia hoat dong chinh tri- xa hoi, van hoa, van nghe, the thao, phong chong toi pham cac te nan xa hoi": "Tiêu chí 3. Đánh giá về ý thức và kết quả tham gia hoạt động chính trị - xã hội, văn hóa, văn nghệ, thể thao, phòng chống tội phạm và các tệ nạn xã hội",
    "Tieu chi 4. Danh gia y thuc cong dan trong quan he cong dong": "Tiêu chí 4. Đánh giá ý thức công dân trong quan hệ cộng đồng",
    "Tieu chi 5. Danh gia ve y thuc va tham gia phu trach lop, cac doan the trong truong, thanh tich dac biet": "Tiêu chí 5. Đánh giá về ý thức và kết quả tham gia phụ trách lớp, các đoàn thể trong nhà trường, thành tích đặc biệt trong học tập và rèn luyện",
    "Y thuc va thai do trong hoc tap": "Ý thức và thái độ trong học tập:",
    "Ket qua hoc tap trong ky hoc": "Kết quả học tập trong kỳ học",
    "Y thuc chap hanh tot noi quy ve cac ky thi": "Ý thức chấp hành tốt nội quy về các kỳ thi",
    "Y thuc va thai do tham gia cac hoat dong ngoai khoa, cac su kien lien quan den nghien cuu khoa hoc, hoc thuat, chuyen mon, Cau lac bo": "Ý thức và thái độ tham gia các hoạt động ngoại khóa, các sự kiện liên quan đến nghiên cứu khoa học, học thuật, chuyên môn, Câu lạc bộ",
    "Tinh than vuot kho, phan dau vuon len trong hoc tap": "Tinh thần vượt khó, phấn đấu vươn lên trong học tập (có ĐTBCTL học kỳ sau lớn hơn học kỳ trước đó; đối với sinh viên năm thứ nhất, học kỳ 1 không có điểm dưới 2,5)",
    "Thuc hien nghiem tuc cac noi quy, quy che, cac quy dinh hien hanh trong Hoc vien.": "Thực hiện nghiêm túc các nội quy, quy chế, các quy định hiện hành trong Học viện.",
    "Thuc hien quy dinh ve cong tac noi tru, ngoai tru": "Thực hiện quy định về công tác nội trú, ngoại trú",
    "Thuc hien nghiem tuc cac buoi hop lop/ sinh hoat doan the do Hoc vien/Khoa/Vien, CVHT, Lop/Chi doan to chuc": "Thực hiện nghiêm túc các buổi họp lớp/ sinh hoạt đoàn thể do Học viện/Khoa/Viện, CVHT, Lớp/Chi đoàn tổ chức (tùy thuộc vào số buổi tổ chức sinh hoạt, họp)",
    "Tham gia cac buoi hoi thao viec lam, dinh huong nghe nghiep do Hoc vien to chuc": "Tham gia các buổi hội thảo việc làm, định hướng nghề nghiệp do Học viện tổ chức",
    "Tham gia day du cac hoat dong chinh tri, xa hoi, the thao, tinh nguyen, cac buoi sinh hoat chuyen de": "Tham gia đầy đủ các hoạt động chính trị, xã hội, các hoạt động văn hóa, văn nghệ, thể thao, phong trào tình nguyện, các buổi sinh hoạt chuyên đề do Học viện, lớp/chi đoàn, địa phương nơi cư trú tổ chức",
    "Tham gia cong tac xa hoi nhu: hien mau nhan dao, ung ho nguoi ngheo, bao lut": "Tham gia công tác xã hội như: hiến máu nhân đạo, ủng hộ người nghèo gặp thiên tai lũ lụt và các công tác xã hội khác",
    "Tuyen truyen tich cuc hinh anh ve Truong/Khoa tren mang xa hoi": "Tuyên truyền tích cực hình ảnh về Trường/Khoa trên các trang mạng xã hội",
    "Tich cuc tham gia hoat dong phong chong toi pham, bao cao hanh vi lien quan toi ma tuy, te nan xa hoi": "Tích cực tham gia các hoạt động phòng, chống tội phạm, các tệ nạn xã hội, phát hiện và báo cáo kịp thời những hành vi có liên quan đến ma túy, các tệ nạn xã hội khác",
    "Dua tin sai lech, thieu kiem chung, binh luan tieu cuc ve Hoc vien/Khoa": "Đưa các thông tin sai lệch, thông tin chưa được kiểm chứng, đăng bình luận không chính xác, thiếu tích cực về Học viện/ Khoa/ ngành đang học.",
    "Chap hanh nghiem chinh chu truong cua Dang, phap luat cua Nha nuoc va dia phuong": "Chấp hành nghiêm chỉnh chủ trương của Đảng, chính sách, pháp luật của Nhà nước, Học viện và của địa phương nơi cư trú",
    "Tich cuc tham gia tuyen truyen phap luat, co y thuc giu gin ve sinh chung": "Tích cực tham gia tuyên truyền chủ trương của Đảng, chính sách, pháp luật của Nhà nước, Học viện và quy định của địa phương nơi cư trú; có ý thức thực hiện giữ gìn vệ sinh chung",
    "Co moi quan he dung muc voi Thay/Co, can bo, nhan vien Hoc vien": "Có mối quan hệ đúng mực với Thầy/ Cô, cán bộ, nhân viên Học viện",
    "Co moi quan he tot voi ban be trong lop; tinh than doan ket, chia se, giup do": "Có mối quan hệ tốt với bạn bè trong lớp và mọi người xung quanh; có tinh thần đoàn kết, chia sẻ, giúp đỡ nhau trong học tập và các vấn đề khác trong cộng đồng",
    "Duoc bieu duong khen thuong trong cac hoat dong y thuc cong dan": "Được biểu dương khen thưởng trong các hoạt động liên quan đến ý thức công dân trong quan hệ cộng đồng",
    "Vi pham an ninh, trat tu xa hoi, an toan giao thong": "Vi phạm an ninh, trật tự xã hội; an toàn giao thông (có giấy báo của các cơ quan hữu quan)",
    "Lop truong, lop pho, bi thu, BCH doan, chu nhiem cau lac bo...": "Sinh viên được Học viện phân công làm lớp trưởng, lớp phó; bí thư, phó bí thư chi đoàn, BCH đoàn Học viện/khoa; BCH Hội sinh viên Học viện/khoa; chủ nhiệm, phó chủ nhiệm các Câu lạc bộ, đội nhóm",
    "Thanh vien tham gia cac Cau lac bo duoc ghi nhan hoan thanh nhiem vu...": "Thành viên tham gia các Câu lạc bộ, đội nhóm trực thuộc Học viện/khoa được tập thể sinh viên và đơn vị quản lý ghi nhận hoàn thành tốt nhiệm vụ; sinh viên tham gia tổ chức các chương trình, lớp tập huấn, hoạt động tập thể",
    "Sinh vien dat thanh tich dac biet trong hoc tap, ren luyen": "Sinh viên đạt thành tích đặc biệt trong học tập, rèn luyện",
}


ROLE_LABELS = {
    UserRole.ADMIN.value: "Admin",
    UserRole.ADVISOR.value: "Cố vấn học tập",
    UserRole.CLASS_MONITOR.value: "Ban cán sự",
    UserRole.STUDENT.value: "Sinh viên",
}


SUBMISSION_LABELS = {
    "draft": "Chưa gửi",
    "student_submitted": "Chờ duyệt",
    "class_reviewed": "Chờ xác nhận",
    "advisor_reviewed": "Hoàn tất",
}


PARTICIPATION_STATUS_LABELS = {
    ParticipationStatus.PENDING: "Chờ duyệt",
    ParticipationStatus.APPROVED: "Đã duyệt",
    ParticipationStatus.REJECTED: "Từ chối",
}


EVIDENCE_STATUS_LABELS = {
    "pending_class": "Chờ duyệt",
    "class_approved": "Đã duyệt",
    "advisor_approved": "Đã duyệt",
    "rejected": "Từ chối",
}


EVIDENCE_CATEGORIES = [
    {"key": "special_achievement", "label": "Thành tích đặc biệt"},
    {"key": "positive_promotion", "label": "Tuyên truyền tích cực về Trường/Khoa"},
    {"key": "social_work", "label": "Tham gia công tác xã hội"},
    {"key": "residence", "label": "Công tác nội trú, ngoại trú"},
]


CATEGORY_LABELS = {item["key"]: item["label"] for item in EVIDENCE_CATEGORIES}


CLASSROOMS = {
    "D23CQAT001": {
        "advisor_username": "CVHT001",
        "advisor_name": "Cố vấn học tập 001",
        "class_monitor_username": "B23DCAT001",
        "class_monitor_name": "Nguyễn Đức Anh",
        "faculty": "An toàn thông tin",
        "major": "An toàn thông tin",
    },
    "D23CQAT002": {
        "advisor_username": "CVHT002",
        "advisor_name": "Cố vấn học tập 002",
        "class_monitor_username": "B23DCAT004",
        "class_monitor_name": "Phạm Gia Hân",
        "faculty": "An toàn thông tin",
        "major": "An toàn thông tin",
    },
    "D23CQCN001": {
        "advisor_username": "CVHT003",
        "advisor_name": "Cố vấn học tập 003",
        "class_monitor_username": "B23DCCN001",
        "class_monitor_name": "Nguyễn Hoàng Nam",
        "faculty": "Công nghệ thông tin",
        "major": "Công nghệ thông tin",
    },
    "D23CQCN002": {
        "advisor_username": "CVHT004",
        "advisor_name": "Cố vấn học tập 004",
        "class_monitor_username": "B23DCCN004",
        "class_monitor_name": "Bùi Khánh Vy",
        "faculty": "Công nghệ thông tin",
        "major": "Công nghệ thông tin",
    },
}


CLASS_MONITOR_USERNAMES = {
    config.get("class_monitor_username", "")
    for config in CLASSROOMS.values()
    if config.get("class_monitor_username")
}
STUDENT_LIKE_ROLES = [UserRole.STUDENT, UserRole.CLASS_MONITOR]
REGISTER_GENDER_OPTIONS = ["Nam", "Nữ", "Khác"]
ROLE_MANAGEMENT_SYSTEM_GROUP_LABEL = "Tài khoản hệ thống"
ROLE_MANAGEMENT_ROLE_ORDER = {
    UserRole.ADVISOR.value: 0,
    UserRole.CLASS_MONITOR.value: 1,
    UserRole.STUDENT.value: 2,
    UserRole.ADMIN.value: 3,
}


_STUDENT_PROFILE_ROWS = [
    {
        "student_code": "B23DCAT001",
        "full_name": "Nguyễn Đức Anh",
        "class_name": "D23CQAT001",
        "phone": "0903100001",
        "gender": "Nam",
        "birth_date": "2005-01-12",
        "faculty": "An toàn thông tin",
        "major": "An toàn thông tin",
        "address": "Hà Đông, Hà Nội",
    },
    {
        "student_code": "B23DCAT002",
        "full_name": "Trần Minh Châu",
        "class_name": "D23CQAT001",
        "phone": "0903100002",
        "gender": "Nữ",
        "birth_date": "2005-03-18",
        "faculty": "An toàn thông tin",
        "major": "An toàn thông tin",
        "address": "Thanh Xuân, Hà Nội",
    },
    {
        "student_code": "B23DCAT003",
        "full_name": "Lê Quốc Bảo",
        "class_name": "D23CQAT001",
        "phone": "0903100003",
        "gender": "Nam",
        "birth_date": "2005-05-07",
        "faculty": "An toàn thông tin",
        "major": "An toàn thông tin",
        "address": "Cầu Giấy, Hà Nội",
    },
    {
        "student_code": "B23DCAT004",
        "full_name": "Phạm Gia Hân",
        "class_name": "D23CQAT002",
        "phone": "0903200001",
        "gender": "Nữ",
        "birth_date": "2005-02-14",
        "faculty": "An toàn thông tin",
        "major": "An toàn thông tin",
        "address": "Đống Đa, Hà Nội",
    },
    {
        "student_code": "B23DCAT005",
        "full_name": "Đỗ Hải Nam",
        "class_name": "D23CQAT002",
        "phone": "0903200002",
        "gender": "Nam",
        "birth_date": "2005-06-21",
        "faculty": "An toàn thông tin",
        "major": "An toàn thông tin",
        "address": "Bắc Từ Liêm, Hà Nội",
    },
    {
        "student_code": "B23DCAT006",
        "full_name": "Vũ Khánh Linh",
        "class_name": "D23CQAT002",
        "phone": "0903200003",
        "gender": "Nữ",
        "birth_date": "2005-09-09",
        "faculty": "An toàn thông tin",
        "major": "An toàn thông tin",
        "address": "Long Biên, Hà Nội",
    },
    {
        "student_code": "B23DCCN001",
        "full_name": "Nguyễn Hoàng Nam",
        "class_name": "D23CQCN001",
        "phone": "0903300001",
        "gender": "Nam",
        "birth_date": "2005-01-30",
        "faculty": "Công nghệ thông tin",
        "major": "Công nghệ thông tin",
        "address": "Nam Từ Liêm, Hà Nội",
    },
    {
        "student_code": "B23DCCN002",
        "full_name": "Võ Ngọc Linh",
        "class_name": "D23CQCN001",
        "phone": "0903300002",
        "gender": "Nữ",
        "birth_date": "2005-04-09",
        "faculty": "Công nghệ thông tin",
        "major": "Công nghệ thông tin",
        "address": "Hoàng Mai, Hà Nội",
    },
    {
        "student_code": "B23DCCN003",
        "full_name": "Trần Đức Long",
        "class_name": "D23CQCN001",
        "phone": "0903300003",
        "gender": "Nam",
        "birth_date": "2005-07-27",
        "faculty": "Công nghệ thông tin",
        "major": "Công nghệ thông tin",
        "address": "Ba Đình, Hà Nội",
    },
    {
        "student_code": "B23DCCN004",
        "full_name": "Bùi Khánh Vy",
        "class_name": "D23CQCN002",
        "phone": "0903400001",
        "gender": "Nữ",
        "birth_date": "2005-02-22",
        "faculty": "Công nghệ thông tin",
        "major": "Công nghệ thông tin",
        "address": "Gia Lâm, Hà Nội",
    },
    {
        "student_code": "B23DCCN005",
        "full_name": "Phan Minh Khoa",
        "class_name": "D23CQCN002",
        "phone": "0903400002",
        "gender": "Nam",
        "birth_date": "2005-08-11",
        "faculty": "Công nghệ thông tin",
        "major": "Công nghệ thông tin",
        "address": "Hai Bà Trưng, Hà Nội",
    },
    {
        "student_code": "B23DCCN006",
        "full_name": "Đặng Thu Trang",
        "class_name": "D23CQCN002",
        "phone": "0903400003",
        "gender": "Nữ",
        "birth_date": "2005-10-03",
        "faculty": "Công nghệ thông tin",
        "major": "Công nghệ thông tin",
        "address": "Thanh Trì, Hà Nội",
    },
]


STUDENT_PROFILES: dict[str, dict] = {
    row["student_code"]: {
        **row,
        "email": f"{row['student_code'].lower()}@stu.ptit.edu.vn",
        "status": "Đang học",
        "citizen_id": "",
        "semester_metrics": {},
    }
    for row in _STUDENT_PROFILE_ROWS
}


AUTO_GPA_CRITERION_TITLE = "Ket qua hoc tap trong ky hoc"
RISING_SPIRIT_CRITERION_TITLE = "Tinh than vuot kho, phan dau vuon len trong hoc tap"
STUDY_ACTIVITY_EVENT_CRITERION_TITLE = (
    "Y thuc va thai do tham gia cac hoat dong ngoai khoa, cac su kien lien quan den nghien cuu khoa hoc, hoc thuat, chuyen mon, Cau lac bo"
)
CLASS_MEETING_EVENT_CRITERION_TITLE = (
    "Thuc hien nghiem tuc cac buoi hop lop/ sinh hoat doan the do Hoc vien/Khoa/Vien, CVHT, Lop/Chi doan to chuc"
)
CAREER_WORKSHOP_EVENT_CRITERION_TITLE = "Tham gia cac buoi hoi thao viec lam, dinh huong nghe nghiep do Hoc vien to chuc"
CLASS_MONITOR_ROLE_CRITERION_TITLE = "Lop truong, lop pho, bi thu, BCH doan, chu nhiem cau lac bo..."
EVIDENCE_CRITERION_MAP = {
    "special_achievement": "Sinh vien dat thanh tich dac biet trong hoc tap, ren luyen",
    "positive_promotion": "Tuyen truyen tich cuc hinh anh ve Truong/Khoa tren mang xa hoi",
    "social_work": "Tham gia cong tac xa hoi nhu: hien mau nhan dao, ung ho nguoi ngheo, bao lut",
    "residence": "Thuc hien quy dinh ve cong tac noi tru, ngoai tru",
}


DETAIL_FIELDS = {
    "special_achievement": [
        ("award_level", "Cấp đạt giải"),
        ("activity_content", "Nội dung hoạt động"),
        ("participation_time", "Ngày tham gia"),
        ("url", "Đường dẫn"),
        ("file_name", "Tập tin minh chứng"),
    ],
    "positive_promotion": [
        ("activity_content", "Nội dung hoạt động"),
        ("event_name", "Sự kiện"),
        ("share_time", "Ngày chia sẻ"),
        ("url", "Đường dẫn"),
        ("file_name", "Tập tin minh chứng"),
    ],
    "social_work": [
        ("social_type", "Tham gia công tác xã hội"),
        ("participation_time", "Ngày tham gia"),
        ("url", "Đường dẫn"),
        ("file_name", "Tập tin minh chứng"),
    ],
    "residence": [
        ("residence_type", "Phân loại cư trú"),
        ("dormitory", "Ký túc xá"),
        ("room_number", "Số phòng"),
        ("city", "Tỉnh/Thành phố"),
        ("district", "Quận/Huyện"),
        ("ward", "Xã/Phường"),
        ("street_address", "Số nhà, đường phố"),
        ("host_name", "Họ tên chủ nhà/trọ/người thân"),
        ("host_phone", "SĐT của chủ nhà/trọ/người thân"),
        ("file_name", "Tập tin minh chứng"),
    ],
}


AUTO_EVENT_CRITERIA_TITLES = {
    STUDY_ACTIVITY_EVENT_CRITERION_TITLE,
    CLASS_MEETING_EVENT_CRITERION_TITLE,
    CAREER_WORKSHOP_EVENT_CRITERION_TITLE,
}


SEEDED_USERNAMES = {
    DEFAULT_ADMIN_USERNAME,
    *(config["advisor_username"] for config in CLASSROOMS.values()),
    *STUDENT_PROFILES.keys(),
}
SUPPRESSED_SEED_USERS_PATH = DATA_DIR / "suppressed_seed_users.json"


DEFAULT_ACTIVE_SCORES = {
    "Y thuc chap hanh tot noi quy ve cac ky thi": 4.0,
    "Ket qua hoc tap trong ky hoc": 0.0,
    STUDY_ACTIVITY_EVENT_CRITERION_TITLE: 0.0,
    "Thuc hien nghiem tuc cac noi quy, quy che, cac quy dinh hien hanh trong Hoc vien.": 15.0,
    "Thuc hien quy dinh ve cong tac noi tru, ngoai tru": 0.0,
    CLASS_MEETING_EVENT_CRITERION_TITLE: 0.0,
    CAREER_WORKSHOP_EVENT_CRITERION_TITLE: 0.0,
    "Tham gia cong tac xa hoi nhu: hien mau nhan dao, ung ho nguoi ngheo, bao lut": 0.0,
    "Tuyen truyen tich cuc hinh anh ve Truong/Khoa tren mang xa hoi": 0.0,
    CLASS_MONITOR_ROLE_CRITERION_TITLE: 0.0,
    "Sinh vien dat thanh tich dac biet trong hoc tap, ren luyen": 0.0,
}


VISIBLE_ZEROS = {
    "Ket qua hoc tap trong ky hoc",
    STUDY_ACTIVITY_EVENT_CRITERION_TITLE,
    "Thuc hien quy dinh ve cong tac noi tru, ngoai tru",
    CLASS_MEETING_EVENT_CRITERION_TITLE,
    CAREER_WORKSHOP_EVENT_CRITERION_TITLE,
    "Tham gia cong tac xa hoi nhu: hien mau nhan dao, ung ho nguoi ngheo, bao lut",
    "Tuyen truyen tich cuc hinh anh ve Truong/Khoa tren mang xa hoi",
    CLASS_MONITOR_ROLE_CRITERION_TITLE,
    "Sinh vien dat thanh tich dac biet trong hoc tap, ren luyen",
}


HISTORICAL_SCORE_PRESETS = [
    {
        "Y thuc va thai do trong hoc tap": 3.0,
        "Ket qua hoc tap trong ky hoc": 7.0,
        "Y thuc chap hanh tot noi quy ve cac ky thi": 3.0,
        STUDY_ACTIVITY_EVENT_CRITERION_TITLE: 3.0,
        RISING_SPIRIT_CRITERION_TITLE: 1.0,
        "Thuc hien nghiem tuc cac noi quy, quy che, cac quy dinh hien hanh trong Hoc vien.": 12.0,
        "Thuc hien quy dinh ve cong tac noi tru, ngoai tru": 0.0,
        CLASS_MEETING_EVENT_CRITERION_TITLE: 4.0,
        CAREER_WORKSHOP_EVENT_CRITERION_TITLE: 3.0,
        "Tham gia day du cac hoat dong chinh tri, xa hoi, the thao, tinh nguyen, cac buoi sinh hoat chuyen de": 7.0,
        EVIDENCE_CRITERION_MAP["social_work"]: 2.0,
        EVIDENCE_CRITERION_MAP["positive_promotion"]: 2.0,
        "Tich cuc tham gia hoat dong phong chong toi pham, bao cao hanh vi lien quan toi ma tuy, te nan xa hoi": 2.0,
        "Dua tin sai lech, thieu kiem chung, binh luan tieu cuc ve Hoc vien/Khoa": 0.0,
        "Chap hanh nghiem chinh chu truong cua Dang, phap luat cua Nha nuoc va dia phuong": 7.0,
        "Tich cuc tham gia tuyen truyen phap luat, co y thuc giu gin ve sinh chung": 4.0,
        "Co moi quan he dung muc voi Thay/Co, can bo, nhan vien Hoc vien": 4.0,
        "Co moi quan he tot voi ban be trong lop; tinh than doan ket, chia se, giup do": 4.0,
        "Duoc bieu duong khen thuong trong cac hoat dong y thuc cong dan": 1.0,
        "Vi pham an ninh, trat tu xa hoi, an toan giao thong": 0.0,
        CLASS_MONITOR_ROLE_CRITERION_TITLE: 0.0,
        EVIDENCE_CRITERION_MAP["special_achievement"]: 3.0,
    },
    {
        "Y thuc va thai do trong hoc tap": 3.0,
        "Ket qua hoc tap trong ky hoc": 8.0,
        "Y thuc chap hanh tot noi quy ve cac ky thi": 4.0,
        STUDY_ACTIVITY_EVENT_CRITERION_TITLE: 4.0,
        RISING_SPIRIT_CRITERION_TITLE: 1.0,
        "Thuc hien nghiem tuc cac noi quy, quy che, cac quy dinh hien hanh trong Hoc vien.": 13.0,
        "Thuc hien quy dinh ve cong tac noi tru, ngoai tru": 0.0,
        CLASS_MEETING_EVENT_CRITERION_TITLE: 4.0,
        CAREER_WORKSHOP_EVENT_CRITERION_TITLE: 4.0,
        "Tham gia day du cac hoat dong chinh tri, xa hoi, the thao, tinh nguyen, cac buoi sinh hoat chuyen de": 8.0,
        EVIDENCE_CRITERION_MAP["social_work"]: 3.0,
        EVIDENCE_CRITERION_MAP["positive_promotion"]: 2.0,
        "Tich cuc tham gia hoat dong phong chong toi pham, bao cao hanh vi lien quan toi ma tuy, te nan xa hoi": 2.0,
        "Dua tin sai lech, thieu kiem chung, binh luan tieu cuc ve Hoc vien/Khoa": 0.0,
        "Chap hanh nghiem chinh chu truong cua Dang, phap luat cua Nha nuoc va dia phuong": 7.0,
        "Tich cuc tham gia tuyen truyen phap luat, co y thuc giu gin ve sinh chung": 5.0,
        "Co moi quan he dung muc voi Thay/Co, can bo, nhan vien Hoc vien": 5.0,
        "Co moi quan he tot voi ban be trong lop; tinh than doan ket, chia se, giup do": 4.0,
        "Duoc bieu duong khen thuong trong cac hoat dong y thuc cong dan": 1.0,
        "Vi pham an ninh, trat tu xa hoi, an toan giao thong": 0.0,
        CLASS_MONITOR_ROLE_CRITERION_TITLE: 0.0,
        EVIDENCE_CRITERION_MAP["special_achievement"]: 0.0,
    },
    {
        "Y thuc va thai do trong hoc tap": 3.0,
        "Ket qua hoc tap trong ky hoc": 8.0,
        "Y thuc chap hanh tot noi quy ve cac ky thi": 4.0,
        STUDY_ACTIVITY_EVENT_CRITERION_TITLE: 5.0,
        RISING_SPIRIT_CRITERION_TITLE: 1.0,
        "Thuc hien nghiem tuc cac noi quy, quy che, cac quy dinh hien hanh trong Hoc vien.": 14.0,
        "Thuc hien quy dinh ve cong tac noi tru, ngoai tru": 0.0,
        CLASS_MEETING_EVENT_CRITERION_TITLE: 4.0,
        CAREER_WORKSHOP_EVENT_CRITERION_TITLE: 4.0,
        "Tham gia day du cac hoat dong chinh tri, xa hoi, the thao, tinh nguyen, cac buoi sinh hoat chuyen de": 8.0,
        EVIDENCE_CRITERION_MAP["social_work"]: 3.0,
        EVIDENCE_CRITERION_MAP["positive_promotion"]: 3.0,
        "Tich cuc tham gia hoat dong phong chong toi pham, bao cao hanh vi lien quan toi ma tuy, te nan xa hoi": 3.0,
        "Dua tin sai lech, thieu kiem chung, binh luan tieu cuc ve Hoc vien/Khoa": 0.0,
        "Chap hanh nghiem chinh chu truong cua Dang, phap luat cua Nha nuoc va dia phuong": 7.0,
        "Tich cuc tham gia tuyen truyen phap luat, co y thuc giu gin ve sinh chung": 5.0,
        "Co moi quan he dung muc voi Thay/Co, can bo, nhan vien Hoc vien": 5.0,
        "Co moi quan he tot voi ban be trong lop; tinh than doan ket, chia se, giup do": 4.0,
        "Duoc bieu duong khen thuong trong cac hoat dong y thuc cong dan": 1.0,
        "Vi pham an ninh, trat tu xa hoi, an toan giao thong": 0.0,
        CLASS_MONITOR_ROLE_CRITERION_TITLE: 0.0,
        EVIDENCE_CRITERION_MAP["special_achievement"]: 2.0,
    },
    {
        "Y thuc va thai do trong hoc tap": 3.0,
        "Ket qua hoc tap trong ky hoc": 10.0,
        "Y thuc chap hanh tot noi quy ve cac ky thi": 4.0,
        STUDY_ACTIVITY_EVENT_CRITERION_TITLE: 5.0,
        RISING_SPIRIT_CRITERION_TITLE: 1.0,
        "Thuc hien nghiem tuc cac noi quy, quy che, cac quy dinh hien hanh trong Hoc vien.": 15.0,
        "Thuc hien quy dinh ve cong tac noi tru, ngoai tru": 0.0,
        CLASS_MEETING_EVENT_CRITERION_TITLE: 5.0,
        CAREER_WORKSHOP_EVENT_CRITERION_TITLE: 5.0,
        "Tham gia day du cac hoat dong chinh tri, xa hoi, the thao, tinh nguyen, cac buoi sinh hoat chuyen de": 8.0,
        EVIDENCE_CRITERION_MAP["social_work"]: 4.0,
        EVIDENCE_CRITERION_MAP["positive_promotion"]: 3.0,
        "Tich cuc tham gia hoat dong phong chong toi pham, bao cao hanh vi lien quan toi ma tuy, te nan xa hoi": 3.0,
        "Dua tin sai lech, thieu kiem chung, binh luan tieu cuc ve Hoc vien/Khoa": 0.0,
        "Chap hanh nghiem chinh chu truong cua Dang, phap luat cua Nha nuoc va dia phuong": 8.0,
        "Tich cuc tham gia tuyen truyen phap luat, co y thuc giu gin ve sinh chung": 5.0,
        "Co moi quan he dung muc voi Thay/Co, can bo, nhan vien Hoc vien": 5.0,
        "Co moi quan he tot voi ban be trong lop; tinh than doan ket, chia se, giup do": 5.0,
        "Duoc bieu duong khen thuong trong cac hoat dong y thuc cong dan": 1.0,
        "Vi pham an ninh, trat tu xa hoi, an toan giao thong": 0.0,
        CLASS_MONITOR_ROLE_CRITERION_TITLE: 0.0,
        EVIDENCE_CRITERION_MAP["special_achievement"]: 0.0,
    },
]


HISTORICAL_GPA_VALUES = [3.04, 3.18, 3.34, 3.68]


SEMESTER_STAGE_OVERRIDES = {
    "Hoc ky 1 nam hoc 2025-2026": [
        (datetime(2025, 8, 1, 0, 0), datetime(2026, 1, 31, 23, 45), "Cập nhật, duyệt minh chứng"),
        (datetime(2026, 4, 3, 0, 0), datetime(2026, 4, 9, 23, 45), "Sinh viên đánh giá"),
        (datetime(2026, 4, 10, 0, 0), datetime(2026, 4, 16, 23, 45), "Ban cán sự đánh giá"),
        (datetime(2026, 4, 17, 0, 0), datetime(2026, 4, 21, 23, 45), "Chủ nhiệm lớp xác nhận"),
    ],
    "Hoc ky 2 nam hoc 2025-2026": [
        (datetime(2026, 2, 1, 0, 0), datetime(2026, 7, 31, 23, 45), "Cập nhật, duyệt minh chứng"),
        (datetime(2026, 10, 12, 0, 0), datetime(2026, 10, 16, 23, 45), "Sinh viên đánh giá"),
        (datetime(2026, 10, 17, 0, 0), datetime(2026, 10, 21, 23, 45), "Ban cán sự đánh giá"),
        (datetime(2026, 10, 22, 0, 0), datetime(2026, 10, 27, 23, 45), "Chủ nhiệm lớp xác nhận"),
    ],
}


DEFAULT_EVENT_BLUEPRINTS = [
    {
        "name": "Seminar An toàn hệ thống 2026",
        "criterion_title": STUDY_ACTIVITY_EVENT_CRITERION_TITLE,
        "points": 2.0,
        "start_time": "08:00 20/04/2026",
        "end_time": "11:00 20/04/2026",
        "location": "Hội trường A1",
        "type_label": "Học thuật",
        "note": "Tính điểm tiêu chí học thuật và ngoại khóa.",
    },
    {
        "name": "Tọa đàm nghiên cứu khoa học sinh viên",
        "criterion_title": STUDY_ACTIVITY_EVENT_CRITERION_TITLE,
        "points": 3.0,
        "start_time": "13:30 24/04/2026",
        "end_time": "16:30 24/04/2026",
        "location": "Phòng họp B3",
        "type_label": "Học thuật",
        "note": "Sự kiện học thuật dành cho sinh viên toàn khoa.",
    },
    {
        "name": "Sinh hoạt lớp đầu tháng 4",
        "criterion_title": CLASS_MEETING_EVENT_CRITERION_TITLE,
        "points": 1.0,
        "start_time": "09:00 15/04/2026",
        "end_time": "10:30 15/04/2026",
        "location": "Phòng C201",
        "type_label": "Họp lớp",
        "note": "Điểm danh sinh hoạt lớp định kỳ.",
    },
    {
        "name": "Sinh hoạt lớp giữa học kỳ",
        "criterion_title": CLASS_MEETING_EVENT_CRITERION_TITLE,
        "points": 1.0,
        "start_time": "09:00 08/05/2026",
        "end_time": "10:30 08/05/2026",
        "location": "Phòng C202",
        "type_label": "Họp lớp",
        "note": "Tổng hợp tiến độ học tập và công tác lớp.",
    },
    {
        "name": "Hội thảo kỹ năng CV và phỏng vấn",
        "criterion_title": CAREER_WORKSHOP_EVENT_CRITERION_TITLE,
        "points": 2.0,
        "start_time": "14:00 18/05/2026",
        "end_time": "17:00 18/05/2026",
        "location": "Hội trường lớn",
        "type_label": "Hội thảo việc làm",
        "note": "Hướng dẫn viết CV và luyện phỏng vấn tuyển dụng.",
    },
    {
        "name": "Ngày hội việc làm PTIT 2026",
        "criterion_title": CAREER_WORKSHOP_EVENT_CRITERION_TITLE,
        "points": 3.0,
        "start_time": "08:00 25/05/2026",
        "end_time": "16:00 25/05/2026",
        "location": "Sân trung tâm",
        "type_label": "Hội thảo việc làm",
        "note": "Ngày hội tuyển dụng, kết nối doanh nghiệp và sinh viên.",
    },
]


REGISTERED_EVENT_DETAILS: dict[str, dict[str, str]] = {
    item["name"]: {
        "type_label": item["type_label"],
        "start_time": item["start_time"],
        "end_time": item["end_time"],
        "location": item["location"],
        "counts_to_score": "Có",
        "note": item["note"],
    }
    for item in DEFAULT_EVENT_BLUEPRINTS
}


@contextmanager
def get_reflex_session() -> Session:
    session = ReflexSessionLocal()
    try:
        yield session
        session.commit()
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()


def vi(text: str | None) -> str:
    if not text:
        return ""
    return TEXT_MAP.get(text, text)


def role_label(role: str | None) -> str:
    return ROLE_LABELS.get(role or "", role or "")


def _clean_optional(value: str | None) -> str | None:
    cleaned = (value or "").strip()
    return cleaned or None


def normalize_birth_date_input(value: str | None) -> str:
    raw = (value or "").strip()
    if not raw:
        return ""
    for parser in (date.fromisoformat,):
        try:
            return parser(raw).isoformat()
        except ValueError:
            pass
    for fmt in ("%d/%m/%Y", "%d-%m-%Y"):
        try:
            return datetime.strptime(raw, fmt).date().isoformat()
        except ValueError:
            pass
    raise ValueError("Ngày sinh không hợp lệ.")


def format_birth_date_display(value: str | None) -> str:
    raw = (value or "").strip()
    if not raw:
        return ""
    try:
        return datetime.strptime(normalize_birth_date_input(raw), "%Y-%m-%d").strftime("%d/%m/%Y")
    except ValueError:
        return raw


def load_suppressed_seed_usernames() -> set[str]:
    if not SUPPRESSED_SEED_USERS_PATH.exists():
        return set()
    try:
        data = json.loads(SUPPRESSED_SEED_USERS_PATH.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return set()
    if not isinstance(data, list):
        return set()
    return {str(item).strip() for item in data if str(item).strip()}


def ensure_data_dir_exists() -> None:
    if DATA_DIR.is_dir():
        return
    if DATA_DIR.exists():
        raise NotADirectoryError(f"Đường dẫn dữ liệu không phải thư mục: {DATA_DIR}")
    DATA_DIR.mkdir(parents=True, exist_ok=True)


def save_suppressed_seed_usernames(usernames: set[str]) -> None:
    ensure_data_dir_exists()
    SUPPRESSED_SEED_USERS_PATH.write_text(
        json.dumps(sorted(usernames), ensure_ascii=False, indent=2),
        encoding="utf-8",
    )


def auto_event_criteria(session: Session) -> list[Criterion]:
    return list(
        session.scalars(
            select(Criterion)
            .where(Criterion.title.in_(AUTO_EVENT_CRITERIA_TITLES))
            .order_by(Criterion.group_id, Criterion.display_order, Criterion.id)
        )
    )


def format_points(value: float | int | None, hide_zero: bool = False) -> str:
    if value is None:
        return ""
    if abs(float(value)) < 1e-9 and hide_zero:
        return ""
    if float(value).is_integer():
        return str(int(float(value)))
    return f"{float(value):g}"


def effective_conduct_total(submission: ReflexSubmission | None) -> float:
    """Điểm tổng đang hiểu lực theo bước duyệt (SV / BCS / CVHT)."""
    if not submission:
        return 0.0
    if submission.status == "advisor_reviewed":
        return float(submission.advisor_total)
    if submission.status == "class_reviewed":
        return float(submission.class_total)
    return float(submission.self_total)


def conduct_grade_label(total: float) -> str:
    """Xếp loại tham khảo thang 100 điểm (thông lệ ĐGRL đại học VN; ngưỡng có thể chỉnh theo quy định trường)."""
    if total >= 90:
        return "Xuất sắc"
    if total >= 80:
        return "Tốt"
    if total >= 65:
        return "Khá"
    if total >= 50:
        return "Trung bình khá"
    if total >= 35:
        return "Trung bình"
    return "Yếu"


def _rounded_clamp(value: float | int | None, min_points: float, max_points: float) -> float:
    parsed = float(value or 0.0)
    return round(max(min_points, min(parsed, max_points)), 2)


def sync_criteria_blueprint(session: Session) -> None:
    groups = list(
        session.scalars(select(CriterionGroup).options(joinedload(CriterionGroup.criteria)).order_by(CriterionGroup.display_order)).unique()
    )
    groups_by_title = {group.title: group for group in groups}
    expected_group_titles = {str(group_blueprint["title"]) for group_blueprint in CRITERION_BLUEPRINT}
    obsolete_groups = [group for group in groups if group.title not in expected_group_titles]
    obsolete_criteria: list[Criterion] = []

    for group_order, group_blueprint in enumerate(CRITERION_BLUEPRINT, start=1):
        group_title = str(group_blueprint["title"])
        group = groups_by_title.get(group_title)
        if group is None:
            group = CriterionGroup(title=group_title, display_order=group_order, max_points=float(group_blueprint["max_points"]))
            session.add(group)
            session.flush()
        group.display_order = group_order
        group.max_points = float(group_blueprint["max_points"])

        existing_criteria = {criterion.title: criterion for criterion in group.criteria}
        expected_titles: set[str] = set()
        for criterion_order, (title, description, min_points, max_points) in enumerate(group_blueprint["criteria"], start=1):
            expected_titles.add(title)
            criterion = existing_criteria.get(title)
            if criterion is None:
                criterion = Criterion(
                    group_id=group.id,
                    title=title,
                    description=description,
                    min_points=float(min_points),
                    max_points=float(max_points),
                    display_order=criterion_order,
                )
                session.add(criterion)
                session.flush()
            criterion.group_id = group.id
            criterion.description = description
            criterion.min_points = float(min_points)
            criterion.max_points = float(max_points)
            criterion.display_order = criterion_order

        obsolete_criteria.extend([criterion for criterion in group.criteria if criterion.title not in expected_titles])

    obsolete_criterion_ids = {criterion.id for criterion in obsolete_criteria if criterion.id}
    for group in obsolete_groups:
        obsolete_criterion_ids.update(criterion.id for criterion in group.criteria if criterion.id)

    if obsolete_criterion_ids:
        for event in list(session.scalars(select(Event).where(Event.criterion_id.in_(obsolete_criterion_ids)))):
            session.delete(event)
        for score in list(session.scalars(select(LegacyScoreEntry).where(LegacyScoreEntry.criterion_id.in_(obsolete_criterion_ids)))):
            session.delete(score)
        for score in list(session.scalars(select(ReflexScore).where(ReflexScore.criterion_id.in_(obsolete_criterion_ids)))):
            session.delete(score)

    for criterion in obsolete_criteria:
        session.delete(criterion)
    for group in obsolete_groups:
        session.delete(group)
    session.flush()


def sync_reflex_scores_with_criteria(session: Session, criteria: list[Criterion]) -> None:
    criteria_by_id = {criterion.id: criterion for criterion in criteria}
    submissions = list(
        session.scalars(
            select(ReflexSubmission).options(joinedload(ReflexSubmission.scores).joinedload(ReflexScore.criterion))
        ).unique()
    )
    for submission in submissions:
        score_map = {score.criterion_id: score for score in submission.scores}
        for criterion in criteria:
            if criterion.id not in score_map:
                session.add(
                    ReflexScore(
                        submission_id=submission.id,
                        criterion_id=criterion.id,
                        self_score=0.0,
                        class_score=0.0,
                        advisor_score=0.0,
                    )
                )
        for score in list(submission.scores):
            criterion = criteria_by_id.get(score.criterion_id)
            if criterion is None:
                session.delete(score)
                continue
            score.self_score = _rounded_clamp(score.self_score, criterion.min_points, criterion.max_points)
            score.class_score = _rounded_clamp(score.class_score, criterion.min_points, criterion.max_points)
            score.advisor_score = _rounded_clamp(score.advisor_score, criterion.min_points, criterion.max_points)
    session.flush()


def ensure_semester(
    session: Session,
    name: str,
    academic_year: str,
    start_date: date,
    end_date: date,
    is_active: bool = False,
) -> Semester:
    semester = session.scalar(select(Semester).where(Semester.name == name))
    if semester:
        if is_active:
            semester.is_active = True
        return semester
    semester = Semester(
        name=name,
        academic_year=academic_year,
        start_date=start_date,
        end_date=end_date,
        is_active=is_active,
    )
    session.add(semester)
    session.flush()
    return semester


def ensure_semester_metric(session: Session, student_id: int, semester_id: int, gpa: float) -> ReflexSemesterMetric:
    metric = session.scalar(
        select(ReflexSemesterMetric).where(
            ReflexSemesterMetric.student_id == student_id,
            ReflexSemesterMetric.semester_id == semester_id,
        )
    )
    if metric is None:
        metric = ReflexSemesterMetric(student_id=student_id, semester_id=semester_id, gpa=round(gpa, 2))
        session.add(metric)
    else:
        metric.gpa = round(gpa, 2)
        metric.updated_at = current_app_time()
    session.flush()
    return metric


def ensure_user(
    session: Session,
    username: str,
    password: str,
    full_name: str,
    role: UserRole,
    **extra: str,
) -> User:
    user = session.scalar(select(User).where(User.username == username))
    if user:
        # Không ghi đè role: mỗi lần load app đều chạy ensure_reflex_demo_data(); nếu sync role
        # từ seed sẽ xóa phân quyền đã lưu (admin/cố vấn đổi quyền xong refresh là mất).
        user.password_hash = _store_password_plain(password)
        user.full_name = full_name
        for key, value in extra.items():
            setattr(user, key, value)
        return user

    user = User(
        username=username,
        password_hash=_store_password_plain(password),
        full_name=full_name,
        role=role,
        **extra,
    )
    session.add(user)
    session.flush()
    return user


def update_user_profile(
    current_user_id: int,
    full_name: str,
    email: str,
    phone: str,
    birth_date: str,
    gender: str,
    address: str,
) -> None:
    ensure_reflex_demo_data()
    resolved_full_name = (full_name or "").strip()
    resolved_email = (email or "").strip().lower()
    resolved_phone = (phone or "").strip()
    resolved_gender = (gender or "").strip()
    resolved_address = (address or "").strip()
    normalized_birth_date = normalize_birth_date_input(birth_date)
    if not resolved_full_name:
        raise ValueError("Họ tên không được để trống.")
    if not resolved_email:
        raise ValueError("Email không được để trống.")
    if not resolved_phone:
        raise ValueError("Số điện thoại không được để trống.")
    if not normalized_birth_date:
        raise ValueError("Ngày sinh không được để trống.")
    if resolved_gender not in REGISTER_GENDER_OPTIONS:
        raise ValueError("Giới tính được chọn không hợp lệ.")
    if not resolved_address:
        raise ValueError("Địa chỉ không được để trống.")

    with get_reflex_session() as session:
        user = session.get(User, current_user_id)
        if not user:
            raise ValueError("Không tìm thấy tài khoản.")
        conflict = session.scalar(select(User).where(User.email == resolved_email, User.id != user.id))
        if conflict:
            raise ValueError("Email đã được tài khoản khác sử dụng.")
        user.full_name = resolved_full_name
        user.email = resolved_email
        user.phone = resolved_phone
        user.birth_date = normalized_birth_date
        user.gender = resolved_gender
        user.address = resolved_address


def save_student_gpa(current_user_id: int, target_student_id: int, semester_id: int, gpa_value: str) -> None:
    ensure_reflex_demo_data()
    raw_value = (gpa_value or "").strip().replace(",", ".")
    try:
        gpa = float(raw_value)
    except ValueError as exc:
        raise ValueError("GPA không hợp lệ.") from exc
    if gpa < 0 or gpa > 4:
        raise ValueError("GPA phải nằm trong khoảng 0 đến 4.")

    with get_reflex_session() as session:
        current_user = session.get(User, current_user_id)
        target_student = session.get(User, target_student_id)
        semester = session.get(Semester, semester_id)
        if not current_user or current_user.role != UserRole.ADVISOR:
            raise ValueError("Chỉ cố vấn học tập được nhập GPA.")
        if not target_student or target_student.role not in STUDENT_LIKE_ROLES:
            raise ValueError("Không tìm thấy sinh viên cần nhập GPA.")
        if not semester:
            raise ValueError("Không tìm thấy học kỳ.")
        if not can_manage_student(current_user, target_student):
            raise ValueError("Sinh viên này không thuộc lớp do bạn phụ trách.")

        metric = session.scalar(
            select(ReflexSemesterMetric).where(
                ReflexSemesterMetric.student_id == target_student.id,
                ReflexSemesterMetric.semester_id == semester.id,
            )
        )
        if not metric:
            metric = ReflexSemesterMetric(student_id=target_student.id, semester_id=semester.id, gpa=round(gpa, 2))
            session.add(metric)
        else:
            metric.gpa = round(gpa, 2)
            metric.updated_at = current_app_time()

        criteria = list(session.scalars(select(Criterion).order_by(Criterion.group_id, Criterion.display_order)))
        submission = ensure_reflex_submission(session, target_student, semester, criteria, status="draft", copy_legacy=True)
        apply_automatic_scores(session, submission, target_student, semester)
        recompute_totals(submission)


def load_payload(evidence: ReflexEvidence) -> dict[str, str]:
    try:
        return json.loads(evidence.payload_json or "{}")
    except json.JSONDecodeError:
        return {}


def summary_from_payload(category_key: str, payload: dict[str, str]) -> str:
    if category_key == "special_achievement":
        return " - ".join(part for part in [payload.get("award_level"), payload.get("activity_content")] if part).strip() or "Thành tích đặc biệt"
    if category_key == "positive_promotion":
        return payload.get("activity_content") or "Tuyên truyền tích cực về Trường/Khoa"
    if category_key == "social_work":
        return payload.get("social_type") or "Tham gia công tác xã hội"
    if category_key == "residence":
        if payload.get("residence_type") == "Nội trú":
            return (
                " - ".join(part for part in [payload.get("residence_type"), payload.get("dormitory"), payload.get("room_number")] if part).strip()
                or "Công tác nội trú, ngoại trú"
            )
        return (
            " - ".join(part for part in [payload.get("residence_type"), payload.get("city"), payload.get("street_address")] if part).strip()
            or "Công tác nội trú, ngoại trú"
        )
    return CATEGORY_LABELS.get(category_key, "Minh chứng")


def parse_stage_datetime(value: str) -> datetime | None:
    v = (value or "").strip()
    if not v:
        return None
    if "T" in v:
        try:
            return datetime.fromisoformat(v.replace("Z", "").split("+")[0])
        except ValueError:
            pass
    for pattern in ("%d/%m/%Y %H:%M", "%d/%m/%Y %H:%M:%S"):
        try:
            return datetime.strptime(v, pattern)
        except ValueError:
            continue
    return None


def _windows_from_semester_json(raw: str | None) -> list[tuple[datetime, datetime, str]] | None:
    if not (raw or "").strip():
        return None
    try:
        data = json.loads(raw)
    except json.JSONDecodeError:
        return None
    if not isinstance(data, list) or len(data) != 4:
        return None
    out: list[tuple[datetime, datetime, str]] = []
    for index, item in enumerate(data):
        if not isinstance(item, dict):
            return None
        st = parse_stage_datetime(str(item.get("start", "")))
        en = parse_stage_datetime(str(item.get("end", "")))
        if st is None or en is None or st > en:
            return None
        label = str(item.get("label") or DEFAULT_CONDUCT_STAGE_LABELS[index])
        out.append((st, en, label))
    return out


def _default_semester_stage_windows(semester: Semester) -> list[tuple[datetime, datetime, str]]:
    start_dt = datetime.combine(semester.start_date, time(0, 0))
    end_dt = datetime.combine(semester.end_date, time(23, 45))
    total_days = max(8, (end_dt.date() - start_dt.date()).days)
    step = max(1, total_days // 8)
    checkpoints = [start_dt + timedelta(days=step * index) for index in [0, 2, 4, 6]]
    result: list[tuple[datetime, datetime, str]] = []
    for index, start_point in enumerate(checkpoints):
        end_point = checkpoints[index + 1] - timedelta(minutes=15) if index < len(checkpoints) - 1 else end_dt
        result.append((start_point, end_point, DEFAULT_CONDUCT_STAGE_LABELS[index]))
    return result


def semester_stage_windows(semester: Semester) -> list[tuple[datetime, datetime, str]]:
    raw = getattr(semester, "conduct_stage_windows_json", None)
    parsed = _windows_from_semester_json(raw)
    if parsed:
        return parsed
    if semester.name in SEMESTER_STAGE_OVERRIDES:
        return SEMESTER_STAGE_OVERRIDES[semester.name]
    return _default_semester_stage_windows(semester)


def serialize_stage_windows_for_admin_editor(semester: Semester) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    for index, (st, en, label) in enumerate(semester_stage_windows(semester)):
        rows.append(
            {
                "i": str(index),
                "label": label,
                "start": st.strftime("%d/%m/%Y %H:%M"),
                "end": en.strftime("%d/%m/%Y %H:%M"),
            }
        )
    return rows


def update_semester_stage_windows(current_user_id: int, semester_id: int, rows: list[dict[str, str]]) -> None:
    ensure_reflex_demo_data()
    if len(rows) != 4:
        raise ValueError("Cần đủ 4 mốc thời gian.")
    with get_reflex_session() as session:
        current_user = session.get(User, current_user_id)
        if not current_user or current_user.role != UserRole.ADMIN:
            raise ValueError("Chỉ quản trị viên được cấu hình mốc thời gian.")
        semester = session.get(Semester, semester_id)
        if not semester:
            raise ValueError("Không tìm thấy học kỳ.")
        parsed: list[dict[str, str]] = []
        for index, row in enumerate(rows):
            st = parse_stage_datetime(str(row.get("start", "")))
            en = parse_stage_datetime(str(row.get("end", "")))
            if st is None or en is None:
                raise ValueError(f"Dòng {index + 1}: định dạng thời gian không hợp lệ (dùng dd/mm/yyyy hh:mm).")
            if st > en:
                raise ValueError(f"Dòng {index + 1}: thời điểm bắt đầu phải trước thời điểm kết thúc.")
            label = str(row.get("label") or DEFAULT_CONDUCT_STAGE_LABELS[index]).strip() or DEFAULT_CONDUCT_STAGE_LABELS[index]
            parsed.append(
                {
                    "start": st.strftime("%Y-%m-%dT%H:%M:%S"),
                    "end": en.strftime("%Y-%m-%dT%H:%M:%S"),
                    "label": label,
                }
            )
        semester.conduct_stage_windows_json = json.dumps(parsed, ensure_ascii=False)


def current_window_index(semester: Semester) -> int:
    now = current_app_time()
    for index, (start_time, end_time, _) in enumerate(semester_stage_windows(semester)):
        if start_time <= now <= end_time:
            return index
    return -1


def semester_evaluation_calendar_open(semester: Semester) -> bool:
    """Có ít nhất một mốc thời gian đánh giá đang mở cho học kỳ này."""
    return current_window_index(semester) >= 0


def timeline_stage_index(semester: Semester) -> int:
    windows = semester_stage_windows(semester)
    if not windows:
        return -1
    now = current_app_time()
    if now < windows[0][0]:
        return -1
    last_index = -1
    for index, (start_time, end_time, _) in enumerate(windows):
        if now >= start_time:
            last_index = index
        if start_time <= now <= end_time:
            return index
        if now < start_time:
            return last_index
    return last_index


def progress_count(status: str) -> int:
    return {
        "draft": 0,
        "student_submitted": 2,
        "class_reviewed": 3,
        "advisor_reviewed": 4,
    }.get(status, 0)


def timeline_from_submission(semester: Semester, status: str) -> list[dict[str, str]]:
    windows = semester_stage_windows(semester)
    now = current_app_time()
    timeline: list[dict[str, str]] = []
    for index, (start_time, end_time, label) in enumerate(windows):
        if now > end_time:
            state = "done"
        elif start_time <= now <= end_time:
            state = "current"
        else:
            state = "upcoming"
        timeline.append(
            {
                "id": str(index),
                "start": start_time.strftime("%d/%m/%Y %H:%M"),
                "end": end_time.strftime("%d/%m/%Y %H:%M"),
                "label": label,
                "state": state,
                "line_after": "done" if now > end_time else "upcoming",
            }
        )
    return timeline


def is_outside_score_window(current_user: User, target_student: User, semester: Semester) -> bool:
    """Cảnh báo «ngoài thời gian chấm điểm» trên phiếu: theo vai trò và theo đang xem bản thân hay sinh viên khác."""
    if current_user.role == UserRole.ADMIN:
        return False
    win = current_window_index(semester)
    if win < 0:
        return True
    if current_user.role == UserRole.STUDENT:
        return win != 1
    if current_user.role == UserRole.CLASS_MONITOR:
        if current_user.id == target_student.id:
            return win not in {1, 2}
        return win != 2
    if current_user.role == UserRole.ADVISOR:
        return win != 3
    return False


def clamp_score(value: str | float | int | None, criterion: Criterion) -> float:
    raw = str(value or "").strip()
    if raw == "":
        return 0.0
    try:
        parsed = float(raw)
    except ValueError:
        parsed = 0.0
    return round(max(criterion.min_points, min(parsed, criterion.max_points)), 2)


def _list_total_from_submission(submission: ReflexSubmission | None) -> str:
    if not submission:
        return "0"
    return format_points(effective_conduct_total(submission))


def serialize_student(
    user: User,
    submission: ReflexSubmission | None = None,
    pending_evidence_count: int = 0,
    pending_event_count: int = 0,
    gpa: str = "",
) -> dict[str, str | int | bool]:
    eff = effective_conduct_total(submission)
    status = submission.status if submission else ""
    return {
        "id": user.id,
        "full_name": vi(user.full_name),
        "student_code": user.student_code or "",
        "class_name": user.class_name or "",
        "label": f"{vi(user.full_name)} - {user.student_code or ''}",
        "score_total": _list_total_from_submission(submission),
        "score_status": status,
        "score_status_label": SUBMISSION_LABELS.get(status, status) if submission else "Chưa có phiếu",
        "conduct_grade": conduct_grade_label(eff) if submission else "—",
        "gpa": gpa,
        "can_direct_review_score": status == "student_submitted",
        "pending_evidence_count": pending_evidence_count,
        "pending_event_count": pending_event_count,
    }


def role_assignment_permissions(current_user: User, target_user: User) -> dict[str, bool]:
    permissions = {
        "can_set_student": False,
        "can_set_class_monitor": False,
        "can_set_advisor": False,
        "can_set_admin": False,
        "can_delete_account": False,
    }
    if current_user.id == target_user.id:
        return permissions
    if current_user.role == UserRole.ADMIN:
        return {
            "can_set_student": True,
            "can_set_class_monitor": True,
            "can_set_advisor": True,
            "can_set_admin": True,
            "can_delete_account": True,
        }
    if current_user.role != UserRole.ADVISOR:
        return permissions
    if (target_user.class_name or "") not in managed_classes_for_user(current_user):
        return permissions
    if target_user.role == UserRole.STUDENT:
        permissions["can_set_class_monitor"] = True
        permissions["can_delete_account"] = True
    elif target_user.role == UserRole.CLASS_MONITOR:
        permissions["can_set_student"] = True
        permissions["can_delete_account"] = True
    return permissions


def role_management_scope_users(session: Session, current_user: User) -> list[User]:
    if current_user.role == UserRole.ADMIN:
        return list(
            session.scalars(
                select(User)
                .where(User.role.in_([UserRole.ADMIN, UserRole.ADVISOR, UserRole.CLASS_MONITOR, UserRole.STUDENT]))
                .order_by(User.id)
            )
        )
    if current_user.role == UserRole.ADVISOR:
        managed_classes = managed_classes_for_user(current_user)
        return list(
            session.scalars(
                select(User)
                .where(
                    (User.id == current_user.id)
                    | (
                        User.role.in_([UserRole.STUDENT, UserRole.CLASS_MONITOR])
                        & User.class_name.in_(managed_classes)
                    )
                )
                .order_by(User.id)
            )
        )
    return []


def role_management_group_label(user: User) -> str:
    if user.role == UserRole.ADMIN or not (user.class_name or "").strip():
        return ROLE_MANAGEMENT_SYSTEM_GROUP_LABEL
    return user.class_name or ROLE_MANAGEMENT_SYSTEM_GROUP_LABEL


def role_management_sort_key(user: User) -> tuple[int, str, int, str, int]:
    group_label = role_management_group_label(user)
    return (
        1 if group_label == ROLE_MANAGEMENT_SYSTEM_GROUP_LABEL else 0,
        vi(group_label),
        ROLE_MANAGEMENT_ROLE_ORDER.get(user.role.value, 99),
        vi(user.full_name).casefold(),
        int(user.id),
    )


def role_management_role_options(current_user: User, target_user: User, perms: dict[str, bool]) -> list[str]:
    if current_user.id == target_user.id:
        return [role_label(target_user.role.value)]
    allowed_roles = {target_user.role.value}
    if perms["can_set_student"]:
        allowed_roles.add(UserRole.STUDENT.value)
    if perms["can_set_class_monitor"]:
        allowed_roles.add(UserRole.CLASS_MONITOR.value)
    if perms["can_set_advisor"]:
        allowed_roles.add(UserRole.ADVISOR.value)
    if perms["can_set_admin"]:
        allowed_roles.add(UserRole.ADMIN.value)
    ordered_roles = sorted(allowed_roles, key=lambda item: ROLE_MANAGEMENT_ROLE_ORDER.get(item, 99))
    return [role_label(item) for item in ordered_roles]


def build_role_management_classes(rows: list[dict[str, str | int | bool | list[str]]]) -> list[str]:
    labels = {str(row.get("management_group_label", "")).strip() for row in rows if str(row.get("management_group_label", "")).strip()}
    return sorted(labels, key=lambda item: (item == ROLE_MANAGEMENT_SYSTEM_GROUP_LABEL, item.casefold()))


def build_role_management_rows(session: Session, current_user: User) -> list[dict[str, str | int | bool | list[str]]]:
    rows: list[dict[str, str | int | bool | list[str]]] = []
    for user in sorted(role_management_scope_users(session, current_user), key=role_management_sort_key):
        perms = role_assignment_permissions(current_user, user)
        rows.append(
            {
                "id": user.id,
                "username": user.username,
                "full_name": vi(user.full_name),
                "email": user.email or "",
                "class_name": user.class_name or "",
                "student_code": user.student_code or "",
                "role": user.role.value,
                "role_label": role_label(user.role.value),
                "is_self": user.id == current_user.id,
                "management_group_label": role_management_group_label(user),
                "role_select_options": role_management_role_options(current_user, user, perms),
                "role_select_disabled": user.id == current_user.id or not any(
                    [perms["can_set_student"], perms["can_set_class_monitor"], perms["can_set_advisor"], perms["can_set_admin"]]
                ),
                "can_set_student": perms["can_set_student"],
                "can_set_class_monitor": perms["can_set_class_monitor"],
                "can_set_advisor": perms["can_set_advisor"],
                "can_set_admin": perms["can_set_admin"],
                "can_delete_account": perms["can_delete_account"],
            }
        )
    return rows


def authenticate_user(username: str, password: str) -> dict[str, str | int]:
    ensure_reflex_demo_data()
    with get_reflex_session() as session:
        user = session.scalar(select(User).where(User.username == username.strip()))
        if not user or not _password_matches(password, user.password_hash):
            raise ValueError("Sai tên đăng nhập hoặc mật khẩu.")
        return {
            "id": user.id,
            "role": user.role.value,
            "role_label": role_label(user.role.value),
            "full_name": vi(user.full_name),
        }


def managed_classes_for_user(current_user: User) -> list[str]:
    if current_user.role == UserRole.CLASS_MONITOR and current_user.class_name:
        return [current_user.class_name]
    if current_user.role == UserRole.ADVISOR:
        if current_user.class_name:
            return [current_user.class_name]
        return [class_name for class_name, config in CLASSROOMS.items() if config["advisor_username"] == current_user.username]
    if current_user.role == UserRole.ADMIN:
        return list(CLASSROOMS.keys())
    return [current_user.class_name] if current_user.class_name else []


def can_manage_student(current_user: User, target_student: User) -> bool:
    if current_user.role == UserRole.ADMIN:
        return True
    if current_user.role == UserRole.STUDENT:
        return current_user.id == target_student.id
    return (target_student.class_name or "") in managed_classes_for_user(current_user)


def profile_for_user(user: User) -> dict[str, str | dict]:
    profile = STUDENT_PROFILES.get(user.username, {})
    return {
        "student_code": user.student_code or profile.get("student_code", ""),
        "full_name": vi(user.full_name or profile.get("full_name", "")),
        "class_name": user.class_name or profile.get("class_name", ""),
        "email": user.email or profile.get("email", ""),
        "phone": user.phone or profile.get("phone", ""),
        "gender": user.gender or profile.get("gender", ""),
        "birth_date": user.birth_date or profile.get("birth_date", ""),
        "status": profile.get("status", "Đang học"),
        "faculty": user.faculty or profile.get("faculty", ""),
        "major": user.major or profile.get("major", ""),
        "address": user.address or profile.get("address", ""),
        "citizen_id": profile.get("citizen_id", ""),
        "semester_metrics": profile.get("semester_metrics", {}),
    }


def semester_metrics_for_user(session: Session, user: User, semester: Semester) -> dict[str, float | str]:
    metrics = dict(profile_for_user(user)["semester_metrics"].get(semester.name, {}))
    override = session.scalar(
        select(ReflexSemesterMetric).where(
            ReflexSemesterMetric.student_id == user.id,
            ReflexSemesterMetric.semester_id == semester.id,
        )
    )
    if override:
        metrics["gpa"] = float(override.gpa or 0.0)
    return metrics


def normalize_event_datetime_input(value: str) -> str:
    raw = (value or "").strip()
    if not raw:
        return ""
    for pattern in ("%Y-%m-%dT%H:%M", "%Y-%m-%d %H:%M", "%H:%M %d/%m/%Y"):
        try:
            return datetime.strptime(raw, pattern).strftime("%H:%M %d/%m/%Y")
        except ValueError:
            continue
    return raw


def parse_event_datetime(value: str) -> datetime | None:
    normalized = normalize_event_datetime_input(value)
    for pattern in ("%H:%M %d/%m/%Y",):
        try:
            return datetime.strptime(normalized, pattern)
        except ValueError:
            continue
    return None


def class_contacts_for_student(session: Session, class_name: str) -> tuple[str, str]:
    classroom = CLASSROOMS.get(class_name, {})
    advisor = session.scalar(
        select(User)
        .where(User.role == UserRole.ADVISOR, User.class_name == class_name)
        .order_by(User.id)
    )
    class_monitor = session.scalar(
        select(User)
        .where(User.role == UserRole.CLASS_MONITOR, User.class_name == class_name)
        .order_by(User.id)
    )
    advisor_name = advisor.full_name if advisor else classroom.get("advisor_name", "")
    class_monitor_name = class_monitor.full_name if class_monitor else classroom.get("class_monitor_name", "")
    return vi(advisor_name), vi(class_monitor_name)


def student_profile_snapshot(session: Session, target_student: User, semester_name: str) -> dict[str, str]:
    profile = profile_for_user(target_student)
    semester = session.scalar(select(Semester).where(Semester.name == semester_name))
    metrics = semester_metrics_for_user(session, target_student, semester) if semester else dict(profile["semester_metrics"].get(semester_name, {}))
    advisor_name, class_monitor_name = class_contacts_for_student(session, str(profile["class_name"]))
    return {
        "student_code": str(profile["student_code"]),
        "full_name": str(profile["full_name"]),
        "class_name": str(profile["class_name"]),
        "email": str(profile["email"]),
        "phone": str(profile["phone"]),
        "gender": str(profile["gender"]),
        "birth_date": format_birth_date_display(str(profile["birth_date"])),
        "birth_date_input": normalize_birth_date_input(str(profile["birth_date"])),
        "status": str(profile["status"]),
        "faculty": str(profile["faculty"]),
        "major": str(profile["major"]),
        "address": str(profile["address"]),
        "citizen_id": str(profile["citizen_id"]),
        "advisor_name": advisor_name,
        "class_monitor_name": class_monitor_name,
        "gpa": format_points(metrics.get("gpa", 0.0)),
        "conduct_rank": str(metrics.get("conduct_rank", "Chưa xếp loại")),
    }


def previous_semester_metrics(student: User, semester_name: str) -> dict[str, float | str]:
    profile = profile_for_user(student)
    metrics_map = profile["semester_metrics"]
    semester_names = list(metrics_map.keys())
    if semester_name not in semester_names:
        return {}
    index = semester_names.index(semester_name)
    if index == 0:
        return {}
    return metrics_map.get(semester_names[index - 1], {})


def gpa_to_conduct_score(gpa: float | int | None) -> float:
    if gpa is None:
        return 0.0
    gpa_value = float(gpa or 0.0)
    if gpa_value > 3.6:
        return 10.0
    if gpa_value > 3.2:
        return 8.0
    if gpa_value > 3.0:
        return 6.0
    return 0.0


def rising_spirit_score(student: User, semester_name: str) -> float:
    return 1.0


def student_window_deadline_passed(semester: Semester) -> bool:
    windows = semester_stage_windows(semester)
    if len(windows) < 2:
        return False
    return current_app_time() > windows[1][1]


def auto_submit_submission_as_student(submission: ReflexSubmission) -> None:
    if submission.status != "draft":
        return
    now = current_app_time()
    submission.status = "student_submitted"
    submission.submitted_at = submission.submitted_at or now
    for score in submission.scores:
        score.class_score = score.self_score
        score.advisor_score = score.self_score
    recompute_totals(submission)


def auto_submit_overdue_student_submissions(session: Session, semester: Semester) -> None:
    if not student_window_deadline_passed(semester):
        return
    criteria = list(session.scalars(select(Criterion).order_by(Criterion.group_id, Criterion.display_order)))
    students = list(session.scalars(select(User).where(User.role.in_(STUDENT_LIKE_ROLES)).order_by(User.id)))
    for student in students:
        submission = ensure_reflex_submission(session, student, semester, criteria, status="draft", copy_legacy=True)
        apply_automatic_scores(session, submission, student, semester)
        auto_submit_submission_as_student(submission)


def note_permissions(current_user: User, target_student: User, submission: ReflexSubmission, semester: Semester) -> dict[str, bool]:
    is_owner = current_user.id == target_student.id and current_user.role in {UserRole.STUDENT, UserRole.CLASS_MONITOR}
    can_manage = can_manage_student(current_user, target_student)
    perms = {
        "student_note_editable": is_owner and submission.status == "draft",
        "class_note_editable": current_user.role == UserRole.CLASS_MONITOR
        and can_manage
        and submission.status == "student_submitted",
        "advisor_note_editable": current_user.role == UserRole.ADVISOR and can_manage and submission.status == "class_reviewed",
    }
    if current_user.role == UserRole.ADMIN:
        return perms
    if not semester_evaluation_calendar_open(semester):
        if current_user.id == target_student.id and current_user.role in {UserRole.STUDENT, UserRole.CLASS_MONITOR}:
            return {k: False for k in perms}
        if current_user.role not in {UserRole.CLASS_MONITOR, UserRole.ADVISOR} or not can_manage:
            return {k: False for k in perms}
    win = current_window_index(semester)
    if win != 1:
        perms["student_note_editable"] = False
    if win != 2:
        perms["class_note_editable"] = False
    if win != 3:
        perms["advisor_note_editable"] = False
    return perms


def approved_evidence_counts(session: Session, student_id: int, semester_id: int) -> dict[str, int]:
    counts = {title: 0 for title in EVIDENCE_CRITERION_MAP.values()}
    evidences = list(
        session.scalars(
            select(ReflexEvidence).where(
                ReflexEvidence.student_id == student_id,
                ReflexEvidence.semester_id == semester_id,
                ReflexEvidence.status.in_(["class_approved", "advisor_approved"]),
            )
        )
    )
    for evidence in evidences:
        criterion_title = EVIDENCE_CRITERION_MAP.get(evidence.category_key)
        if criterion_title and evidence.category_key != "residence":
            counts[criterion_title] = counts.get(criterion_title, 0) + 1
    return counts


def residence_compliance_score(session: Session, student_id: int, semester_id: int) -> float:
    residence_evidence = session.scalar(
        select(ReflexEvidence.id).where(
            ReflexEvidence.student_id == student_id,
            ReflexEvidence.semester_id == semester_id,
            ReflexEvidence.category_key == "residence",
        )
    )
    return 0.0 if residence_evidence else -5.0


def approved_event_counts(session: Session, student_id: int, semester_id: int) -> dict[int, float]:
    counts: dict[int, float] = {}
    participations = list(
        session.scalars(
            select(EventParticipation)
            .where(EventParticipation.student_id == student_id, EventParticipation.status == ParticipationStatus.APPROVED)
            .options(joinedload(EventParticipation.event).joinedload(Event.criterion))
        )
    )
    for participation in participations:
        event = participation.event
        if not event or event.semester_id != semester_id:
            continue
        criterion = event.criterion
        if not criterion or criterion.title not in AUTO_EVENT_CRITERIA_TITLES:
            continue
        counts[event.criterion_id] = round(counts.get(event.criterion_id, 0.0) + float(event.points or 0.0), 2)
    return counts


def auto_locked_titles(session: Session, semester_id: int) -> set[str]:
    titles = {AUTO_GPA_CRITERION_TITLE, RISING_SPIRIT_CRITERION_TITLE, CLASS_MONITOR_ROLE_CRITERION_TITLE, *EVIDENCE_CRITERION_MAP.values()}
    titles.update(
        criterion.title
        for criterion in session.scalars(
            select(Criterion)
            .join(Event, Event.criterion_id == Criterion.id)
            .where(Event.semester_id == semester_id, Criterion.title.in_(AUTO_EVENT_CRITERIA_TITLES))
        )
    )
    return titles


def apply_automatic_scores(
    session: Session, submission: ReflexSubmission, target_student: User, semester: Semester | None = None
) -> None:
    sem = semester if semester is not None else submission.semester
    semester_name = sem.name if sem else ""
    metrics = semester_metrics_for_user(session, target_student, sem) if sem else {}
    evidence_counts = approved_evidence_counts(session, target_student.id, submission.semester_id)
    event_counts = approved_event_counts(session, target_student.id, submission.semester_id)
    residence_score = residence_compliance_score(session, target_student.id, submission.semester_id)
    for score in submission.scores:
        criterion = score.criterion
        if not criterion:
            continue
        title = criterion.title
        auto_value: float | None = None
        if title == AUTO_GPA_CRITERION_TITLE:
            auto_value = gpa_to_conduct_score(metrics.get("gpa", 0.0))
        elif title == RISING_SPIRIT_CRITERION_TITLE:
            auto_value = rising_spirit_score(target_student, semester_name)
        elif title == EVIDENCE_CRITERION_MAP["residence"]:
            auto_value = residence_score
        elif title == CLASS_MONITOR_ROLE_CRITERION_TITLE:
            auto_value = float(criterion.max_points) if target_student.role == UserRole.CLASS_MONITOR else 0.0
        elif title in evidence_counts:
            if title == EVIDENCE_CRITERION_MAP["residence"]:
                auto_value = 0.0
            else:
                auto_value = float(evidence_counts.get(title, 0))
        elif title in AUTO_EVENT_CRITERIA_TITLES:
            auto_value = float(event_counts.get(criterion.id, 0.0))

        if auto_value is None:
            continue
        clamped = round(max(criterion.min_points, min(auto_value, criterion.max_points)), 2)
        score.self_score = clamped
        score.class_score = clamped
        score.advisor_score = clamped


def refresh_all_submission_automatic_scores(session: Session) -> None:
    submissions = list(
        session.scalars(
            select(ReflexSubmission).options(
                joinedload(ReflexSubmission.student),
                joinedload(ReflexSubmission.semester),
                joinedload(ReflexSubmission.scores).joinedload(ReflexScore.criterion),
            )
        ).unique()
    )
    for submission in submissions:
        if not submission.student or not submission.semester:
            continue
        if submission.status == "advisor_reviewed":
            continue
        apply_automatic_scores(session, submission, submission.student, submission.semester)
        recompute_totals(submission)
    session.flush()


def recompute_totals(submission: ReflexSubmission) -> None:
    submission.self_total = round(sum(score.self_score for score in submission.scores), 2)
    submission.class_total = round(sum(score.class_score for score in submission.scores), 2)
    submission.advisor_total = round(sum(score.advisor_score for score in submission.scores), 2)
    submission.updated_at = current_app_time()


def ensure_reflex_submission(
    session: Session,
    student: User,
    semester: Semester,
    criteria: list[Criterion],
    status: str,
    preset: dict[str, float] | None = None,
    copy_legacy: bool = False,
    submitted_at: datetime | None = None,
    class_reviewed_at: datetime | None = None,
    advisor_reviewed_at: datetime | None = None,
) -> ReflexSubmission:
    submission = session.scalar(
        select(ReflexSubmission)
        .where(ReflexSubmission.student_id == student.id, ReflexSubmission.semester_id == semester.id)
        .options(joinedload(ReflexSubmission.scores).joinedload(ReflexScore.criterion))
    )
    if submission:
        return submission

    legacy_submission = None
    legacy_scores: dict[int, LegacyScoreEntry] = {}
    if copy_legacy:
        legacy_submission = session.scalar(
            select(LegacySubmission)
            .where(LegacySubmission.student_id == student.id, LegacySubmission.semester_id == semester.id)
            .options(joinedload(LegacySubmission.scores).joinedload(LegacyScoreEntry.criterion))
        )
        if legacy_submission:
            legacy_scores = {score.criterion_id: score for score in legacy_submission.scores}

    submission = ReflexSubmission(
        student_id=student.id,
        semester_id=semester.id,
        status=status,
        student_note=legacy_submission.student_note if legacy_submission else "",
        class_note="Đã xem xét và đối chiếu minh chứng." if status in {"class_reviewed", "advisor_reviewed"} else "",
        advisor_note=legacy_submission.advisor_note if legacy_submission else "",
        submitted_at=submitted_at,
        class_reviewed_at=class_reviewed_at,
        advisor_reviewed_at=advisor_reviewed_at,
        updated_at=current_app_time(),
    )
    session.add(submission)
    session.flush()

    for criterion in criteria:
        if preset and criterion.title in preset:
            self_score = round(float(preset[criterion.title]), 2)
            class_score = self_score
            advisor_score = self_score
        elif criterion.id in legacy_scores:
            legacy = legacy_scores[criterion.id]
            self_score = legacy.self_score
            class_score = legacy.advisor_score
            advisor_score = legacy.advisor_score
        else:
            self_score = 0.0
            class_score = 0.0
            advisor_score = 0.0

        if status == "draft":
            class_score = self_score
            advisor_score = self_score
        elif status == "student_submitted":
            advisor_score = class_score

        session.add(
            ReflexScore(
                submission_id=submission.id,
                criterion_id=criterion.id,
                self_score=self_score,
                class_score=class_score,
                advisor_score=advisor_score,
            )
        )

    session.flush()
    recompute_totals(submission)
    return submission


def ensure_default_events(session: Session, semesters: list[Semester]) -> None:
    active_semester = next((semester for semester in semesters if semester.is_active), None)
    if active_semester is None:
        return
    criteria_by_title = {
        criterion.title: criterion
        for criterion in session.scalars(select(Criterion).where(Criterion.title.in_(AUTO_EVENT_CRITERIA_TITLES)))
    }
    existing_events = {
        event.name: event
        for event in session.scalars(select(Event).where(Event.semester_id == active_semester.id))
    }
    for blueprint in DEFAULT_EVENT_BLUEPRINTS:
        criterion = criteria_by_title.get(str(blueprint["criterion_title"]))
        if criterion is None:
            continue
        event = existing_events.get(str(blueprint["name"]))
        normalized_start = normalize_event_datetime_input(str(blueprint["start_time"]))
        normalized_end = normalize_event_datetime_input(str(blueprint["end_time"]))
        if event is None:
            event = Event(
                semester_id=active_semester.id,
                criterion_id=criterion.id,
                name=str(blueprint["name"]),
                points=float(blueprint["points"]),
                start_time=normalized_start,
                end_time=normalized_end,
                location=str(blueprint["location"]),
                is_active=True,
            )
            session.add(event)
            continue
        event.criterion_id = criterion.id
        event.points = float(blueprint["points"])
        event.start_time = normalized_start
        event.end_time = normalized_end
        event.location = str(blueprint["location"])
        event.is_active = True
    session.flush()


def ensure_historical_reflex_submissions(session: Session, students: list[User], semesters: list[Semester], criteria: list[Criterion]) -> None:
    completed_semesters = [semester for semester in semesters if not semester.is_active]
    target_semesters = completed_semesters[-4:]
    for student_index, student in enumerate(students):
        for semester_index, semester in enumerate(target_semesters):
            existing = session.scalar(
                select(ReflexSubmission.id).where(
                    ReflexSubmission.student_id == student.id,
                    ReflexSubmission.semester_id == semester.id,
                )
            )
            if existing:
                continue
            reviewed_at = datetime.combine(semester.end_date, time(16, 0))
            preset = dict(HISTORICAL_SCORE_PRESETS[(semester_index + student_index) % len(HISTORICAL_SCORE_PRESETS)])
            preset[CLASS_MONITOR_ROLE_CRITERION_TITLE] = 4.0 if student.role == UserRole.CLASS_MONITOR else 0.0
            ensure_semester_metric(
                session,
                student_id=student.id,
                semester_id=semester.id,
                gpa=HISTORICAL_GPA_VALUES[(semester_index + student_index) % len(HISTORICAL_GPA_VALUES)],
            )
            ensure_reflex_submission(
                session,
                student,
                semester,
                criteria,
                status="advisor_reviewed",
                preset=preset,
                submitted_at=reviewed_at - timedelta(days=2),
                class_reviewed_at=reviewed_at - timedelta(days=1),
                advisor_reviewed_at=reviewed_at,
            )


def ensure_reflex_demo_data() -> None:
    ensure_data_dir_exists()
    Base.metadata.create_all(reflex_engine)
    ensure_semester_stage_windows_column()
    ensure_user_profile_columns()
    ensure_event_detail_columns()
    with get_reflex_session() as session:
        seed_default_data(session)
        sync_criteria_blueprint(session)
        suppressed_seed_usernames = load_suppressed_seed_usernames()

        ensure_semester(
            session,
            name="Hoc ky 1 nam hoc 2023 - 2024",
            academic_year="2023-2024",
            start_date=date(2023, 9, 1),
            end_date=date(2024, 1, 15),
            is_active=False,
        )
        ensure_semester(
            session,
            name="Hoc ky 2 nam hoc 2023 - 2024",
            academic_year="2023-2024",
            start_date=date(2024, 2, 1),
            end_date=date(2024, 6, 15),
            is_active=False,
        )

        if DEFAULT_ADMIN_USERNAME not in suppressed_seed_usernames:
            ensure_user(
                session,
                username=DEFAULT_ADMIN_USERNAME,
                password="admin123",
                full_name="Quản trị hệ thống",
                role=UserRole.ADMIN,
                faculty="PTIT",
                email="admin@ptit.edu.vn",
            )
        for class_name, config in CLASSROOMS.items():
            username = str(config["advisor_username"])
            if username in suppressed_seed_usernames:
                continue
            ensure_user(
                session,
                username=username,
                password=username,
                full_name=str(config["advisor_name"]),
                role=UserRole.ADVISOR,
                student_code=username,
                class_name=class_name,
                faculty=str(config["faculty"]),
                major=str(config["major"]),
                email=f"{username}@ptit.edu.vn",
            )
        for username, profile in STUDENT_PROFILES.items():
            if username in suppressed_seed_usernames:
                continue
            student_role = UserRole.CLASS_MONITOR if username in CLASS_MONITOR_USERNAMES else UserRole.STUDENT
            ensure_user(
                session,
                username=username,
                password=str(profile["student_code"]),
                full_name=str(profile["full_name"]),
                role=student_role,
                student_code=str(profile["student_code"]),
                email=str(profile["email"]),
                class_name=str(profile["class_name"]),
                faculty=str(profile["faculty"]),
                major=str(profile["major"]),
                phone=str(profile.get("phone", "")),
                birth_date=normalize_birth_date_input(str(profile.get("birth_date", ""))),
                gender=str(profile.get("gender", "")),
                address=str(profile.get("address", "")),
            )

        semesters = list(session.scalars(select(Semester).order_by(Semester.start_date)))
        criteria = list(session.scalars(select(Criterion).order_by(Criterion.group_id, Criterion.display_order)))
        sync_reflex_scores_with_criteria(session, criteria)
        students = list(session.scalars(select(User).where(User.role.in_(STUDENT_LIKE_ROLES)).order_by(User.student_code)))
        ensure_historical_reflex_submissions(session, students, semesters, criteria)
        ensure_default_events(session, semesters)


def account_scope_students(session: Session, current_user: User) -> list[User]:
    if current_user.role == UserRole.STUDENT:
        return [current_user]
    if current_user.role in {UserRole.CLASS_MONITOR, UserRole.ADVISOR}:
        managed_classes = managed_classes_for_user(current_user)
        students = list(
            session.scalars(
                select(User)
                .where(User.role.in_(STUDENT_LIKE_ROLES), User.class_name.in_(managed_classes))
                .order_by(User.student_code)
            )
        )
        if current_user.role == UserRole.CLASS_MONITOR and current_user.id not in {s.id for s in students}:
            return [current_user, *students]
        return students
    return list(session.scalars(select(User).where(User.role.in_(STUDENT_LIKE_ROLES)).order_by(User.student_code)))


def preferred_student(session: Session, current_user: User, students: list[User], target_student_id: int | None) -> User:
    if current_user.role == UserRole.STUDENT:
        return current_user
    if not students:
        return current_user
    if target_student_id:
        found = next((student for student in students if student.id == target_student_id), None)
        if found:
            return found
    if current_user.role == UserRole.CLASS_MONITOR:
        self_student = next((student for student in students if student.id == current_user.id), None)
        if self_student:
            own_draft = session.scalar(
                select(ReflexSubmission).where(ReflexSubmission.student_id == current_user.id, ReflexSubmission.status == "draft")
            )
            if own_draft:
                return self_student
            own_submitted = session.scalar(
                select(ReflexSubmission).where(
                    ReflexSubmission.student_id == current_user.id, ReflexSubmission.status == "student_submitted"
                )
            )
            if own_submitted:
                return self_student
        managed_student_ids = [student.id for student in students if student.id != current_user.id]
        pending = session.scalar(
            select(ReflexSubmission)
            .where(ReflexSubmission.status == "student_submitted", ReflexSubmission.student_id.in_(managed_student_ids))
            .order_by(ReflexSubmission.updated_at.desc())
        )
        if pending:
            return next(student for student in students if student.id == pending.student_id)
        if self_student:
            return self_student
    if current_user.role == UserRole.ADVISOR:
        pending = session.scalar(
            select(ReflexSubmission)
            .where(ReflexSubmission.status == "class_reviewed", ReflexSubmission.student_id.in_([student.id for student in students]))
            .order_by(ReflexSubmission.updated_at.desc())
        )
        if pending:
            return next(student for student in students if student.id == pending.student_id)
    return students[0]


def preferred_semester(
    session: Session,
    current_user: User,
    target_student: User,
    semesters: list[Semester],
    selected_semester_id: int | None,
) -> Semester:
    if selected_semester_id:
        found = next((semester for semester in semesters if semester.id == selected_semester_id), None)
        if found:
            return found
    if current_user.id == target_student.id and current_user.role in {UserRole.STUDENT, UserRole.CLASS_MONITOR}:
        for semester in semesters:
            if semester_evaluation_calendar_open(semester):
                return semester
        active_semester = next((semester for semester in semesters if semester.is_active), None)
        if active_semester:
            return active_semester
    if current_user.role == UserRole.CLASS_MONITOR:
        pending = session.scalar(
            select(ReflexSubmission)
            .where(ReflexSubmission.student_id == target_student.id, ReflexSubmission.status == "student_submitted")
            .order_by(ReflexSubmission.updated_at.desc())
        )
        if pending:
            return next(semester for semester in semesters if semester.id == pending.semester_id)
    if current_user.role == UserRole.ADVISOR:
        pending = session.scalar(
            select(ReflexSubmission)
            .where(ReflexSubmission.student_id == target_student.id, ReflexSubmission.status == "class_reviewed")
            .order_by(ReflexSubmission.updated_at.desc())
        )
        if pending:
            return next(semester for semester in semesters if semester.id == pending.semester_id)
    return semesters[0]


def score_permissions(current_user: User, target_student: User, submission: ReflexSubmission, semester: Semester) -> dict[str, bool]:
    is_owner = current_user.id == target_student.id and current_user.role in {UserRole.STUDENT, UserRole.CLASS_MONITOR}
    can_manage = can_manage_student(current_user, target_student)
    class_monitor_reviewable = (
        current_user.role == UserRole.CLASS_MONITOR
        and can_manage
        and submission.status == "student_submitted"
    )
    perms = {
        "self_editable": is_owner and submission.status == "draft",
        "class_editable": class_monitor_reviewable,
        "advisor_editable": current_user.role == UserRole.ADVISOR and can_manage and submission.status == "class_reviewed",
    }
    if current_user.role == UserRole.ADMIN:
        return {"self_editable": True, "class_editable": True, "advisor_editable": True}
    if not semester_evaluation_calendar_open(semester):
        if current_user.id == target_student.id and current_user.role in {UserRole.STUDENT, UserRole.CLASS_MONITOR}:
            return {"self_editable": False, "class_editable": False, "advisor_editable": False}
        if current_user.role not in {UserRole.CLASS_MONITOR, UserRole.ADVISOR} or not can_manage:
            return {"self_editable": False, "class_editable": False, "advisor_editable": False}
    win = current_window_index(semester)
    if win == 0:
        return {"self_editable": False, "class_editable": False, "advisor_editable": False}
    if win == 1:
        return {**perms, "class_editable": False, "advisor_editable": False}
    if win == 2:
        return {**perms, "self_editable": False, "advisor_editable": False}
    if win == 3:
        return {**perms, "self_editable": False, "class_editable": False}
    return {"self_editable": False, "class_editable": False, "advisor_editable": False}


def evidence_permissions(current_user: User, target_student: User, evidence: ReflexEvidence, semester: Semester) -> dict[str, bool]:
    is_owner = current_user.id == target_student.id and current_user.role in {UserRole.STUDENT, UserRole.CLASS_MONITOR}
    can_manage = can_manage_student(current_user, target_student)
    perms = {
        "can_delete": is_owner and evidence.status == "pending_class",
        "can_class_review": current_user.role == UserRole.CLASS_MONITOR and can_manage and evidence.status == "pending_class",
        "can_advisor_review": False,
    }
    if current_user.role == UserRole.ADMIN:
        return perms
    if not semester_evaluation_calendar_open(semester):
        if is_owner:
            return {"can_delete": False, "can_class_review": False, "can_advisor_review": False}
        if current_user.role != UserRole.CLASS_MONITOR or not can_manage:
            return {"can_delete": False, "can_class_review": False, "can_advisor_review": False}
    win = current_window_index(semester)
    if win != 0 and perms["can_delete"]:
        perms["can_delete"] = False
    if win != 0 and perms["can_class_review"]:
        perms["can_class_review"] = False
    return perms


def serialize_evidence_detail(evidence: ReflexEvidence, current_user: User, target_student: User, semester: Semester) -> dict:
    payload = load_payload(evidence)
    perms = evidence_permissions(current_user, target_student, evidence, semester)
    if evidence.category_key == "residence":
        if payload.get("residence_type") == "Nội trú":
            field_defs = [
                ("residence_type", "Phân loại cư trú"),
                ("dormitory", "Ký túc xá"),
                ("room_number", "Số phòng"),
                ("file_name", "Tập tin minh chứng"),
            ]
        else:
            field_defs = [
                ("residence_type", "Phân loại cư trú"),
                ("city", "Tỉnh/Thành phố"),
                ("district", "Quận/Huyện"),
                ("ward", "Xã/Phường"),
                ("street_address", "Số nhà, đường phố"),
                ("host_name", "Họ tên chủ nhà/trọ/người thân"),
                ("host_phone", "SĐT của chủ nhà/trọ/người thân"),
                ("file_name", "Tập tin minh chứng"),
            ]
    else:
        field_defs = DETAIL_FIELDS.get(evidence.category_key, [])
    fields = []
    for key, label in field_defs:
        val = str(payload.get(key, "") or "")
        file_path = resolve_evidence_upload(str(payload.get("file_path", "") or ""), val) if key == "file_name" else ""
        is_link = key == "url" and val.startswith(("http://", "https://"))
        is_file = key == "file_name" and bool(file_path)
        fields.append(
            {
                "label": label,
                "value": val
                or (
                    "Mở tệp minh chứng"
                    if is_file
                    else ("Không tìm thấy tệp minh chứng" if key == "file_name" else "")
                ),
                "is_link": is_link,
                "is_file": is_file,
                "file_path": file_path,
                "is_image": is_file and is_image_file(val or file_path),
                "is_missing_file": key == "file_name" and bool(val) and not is_file,
            }
        )
    return {
        "id": evidence.id,
        "title": CATEGORY_LABELS.get(evidence.category_key, "Chi tiết minh chứng"),
        "status_label": EVIDENCE_STATUS_LABELS.get(evidence.status, evidence.status),
        "fields": fields,
        "summary": evidence.summary,
        "can_class_review": perms["can_class_review"],
        "can_advisor_review": perms["can_advisor_review"],
    }


def event_detail_for_registered(event: Event) -> dict[str, str]:
    detail = REGISTERED_EVENT_DETAILS.get(event.name, {})
    criterion_title = event.criterion.title if event.criterion else ""
    type_label = detail.get("type_label", "Sự kiện")
    if not detail and criterion_title == CLASS_MEETING_EVENT_CRITERION_TITLE:
        type_label = "Họp lớp"
    elif not detail and criterion_title == CAREER_WORKSHOP_EVENT_CRITERION_TITLE:
        type_label = "Hội thảo việc làm"
    elif not detail and criterion_title == STUDY_ACTIVITY_EVENT_CRITERION_TITLE:
        type_label = "Học thuật"
    return {
        "type_label": type_label,
        "event_name": event.name,
        "start_time": event.start_time or detail.get("start_time", ""),
        "end_time": event.end_time or detail.get("end_time", ""),
        "location": event.location or detail.get("location", "PTIT"),
        "counts_to_score": detail.get("counts_to_score", "Có"),
        "note": detail.get("note", ""),
    }


def _parse_event_time(value: str) -> datetime | None:
    if not value:
        return None
    return parse_event_datetime(value)


def _weekday_label(moment: datetime) -> str:
    labels = ["Thứ hai", "Thứ ba", "Thứ tư", "Thứ năm", "Thứ sáu", "Thứ bảy", "Chủ nhật"]
    return labels[moment.weekday()]


def serialize_event_item(event: Event, participation: EventParticipation | None = None) -> dict[str, str | bool | int]:
    detail = event_detail_for_registered(event)
    start_moment = _parse_event_time(detail["start_time"])
    return {
        "id": str(event.id),
        "participation_id": participation.id if participation else 0,
        "title": vi(event.name),
        "points": format_points(event.points),
        "type_label": detail["type_label"],
        "event_name": vi(detail["event_name"]),
        "start_time": detail["start_time"],
        "end_time": detail["end_time"],
        "location": detail["location"],
        "counts_to_score": detail["counts_to_score"],
        "note": detail["note"],
        "date": _weekday_label(start_moment) + f", ngày {start_moment.strftime('%d/%m/%Y')}" if start_moment else "",
        "count": "1",
        "time": start_moment.strftime("%H:%M") if start_moment else "",
        "accent": "#53b8dc" if detail["type_label"] != "Họp lớp" else "#b774ff",
        "status_label": PARTICIPATION_STATUS_LABELS.get(participation.status, "") if participation else "",
    }


def build_event_lists(
    session: Session,
    current_user: User,
    target_student: User,
    selected_semester: Semester,
) -> tuple[list[dict], list[dict], list[dict]]:
    active_events = get_active_events(session, selected_semester.id)
    participations = list(
        session.scalars(
            select(EventParticipation)
            .where(EventParticipation.student_id == target_student.id)
            .options(joinedload(EventParticipation.event).joinedload(Event.criterion))
        )
    )
    participation_map = {participation.event_id: participation for participation in participations if participation.event}

    joined_events: list[dict] = []
    registered_events: list[dict] = []
    open_events: list[dict] = []
    registration_context = selected_semester.is_active and (
        current_user.role == UserRole.ADMIN
        or (current_user.role in {UserRole.STUDENT, UserRole.CLASS_MONITOR} and current_user.id == target_student.id)
    )
    can_register = registration_context
    can_approve = (
        (
            current_user.role == UserRole.ADMIN
            or (
                current_user.role == UserRole.CLASS_MONITOR
                and current_window_index(selected_semester) == 0
            )
        )
        and can_manage_student(current_user, target_student)
    )

    for event in active_events:
        participation = participation_map.get(event.id)
        item = serialize_event_item(event, participation)
        if participation and participation.status == ParticipationStatus.APPROVED:
            joined_events.append(item)
            registered_events.append(
                {
                    **item,
                    "action_label": "Đã duyệt",
                    "can_register": False,
                    "can_approve": False,
                }
            )
            continue
        if participation:
            registered_events.append(
                {
                    **item,
                    "action_label": "Chờ duyệt",
                    "can_register": False,
                    "can_approve": can_approve and participation.status == ParticipationStatus.PENDING,
                }
            )
            continue
        if not registration_context:
            continue
        open_events.append(
            {
                **item,
                "action_label": "Đăng ký",
                "can_register": bool(can_register),
                "can_approve": False,
            }
        )

    now = current_app_time()
    joined_events.sort(key=lambda item: _parse_event_time(str(item.get("start_time", ""))) or now, reverse=False)
    registered_events.sort(key=lambda item: _parse_event_time(str(item.get("start_time", ""))) or now, reverse=False)
    open_events.sort(key=lambda item: _parse_event_time(str(item.get("start_time", ""))) or now, reverse=False)
    return joined_events, registered_events, open_events


def build_snapshot(
    current_user_id: int | None = None,
    selected_semester_id: int | None = None,
    target_student_id: int | None = None,
    selected_category_key: str | None = None,
) -> dict:
    ensure_reflex_demo_data()
    with get_reflex_session() as session:
        accounts = list(
            session.scalars(
                select(User)
                .where(User.role.in_([UserRole.ADMIN, UserRole.ADVISOR, UserRole.CLASS_MONITOR, UserRole.STUDENT]))
                .order_by(User.id)
            )
        )
        current_user = next((user for user in accounts if user.id == current_user_id), None)
        if current_user is None:
            current_user = next((user for user in accounts if user.username == DEFAULT_ADMIN_USERNAME), accounts[0])

        students = account_scope_students(session, current_user)
        target_student = preferred_student(session, current_user, students, target_student_id)
        semesters = get_semesters(session)
        selected_semester = preferred_semester(session, current_user, target_student, semesters, selected_semester_id)
        auto_submit_overdue_student_submissions(session, selected_semester)

        category_key = selected_category_key or EVIDENCE_CATEGORIES[0]["key"]
        if category_key not in CATEGORY_LABELS:
            category_key = EVIDENCE_CATEGORIES[0]["key"]

        criteria = list(session.scalars(select(Criterion).order_by(Criterion.group_id, Criterion.display_order)))
        target_is_student = target_student.role in STUDENT_LIKE_ROLES
        if target_is_student:
            submission = ensure_reflex_submission(
                session,
                target_student,
                selected_semester,
                criteria,
                status="draft",
                copy_legacy=True,
            )
            if submission.status != "advisor_reviewed":
                apply_automatic_scores(session, submission, target_student, selected_semester)
            recompute_totals(submission)
            permissions = score_permissions(current_user, target_student, submission, selected_semester)
            note_perms = note_permissions(current_user, target_student, submission, selected_semester)
            score_map = {score.criterion_id: score for score in submission.scores}
        else:
            submission = None
            permissions = {"self_editable": False, "class_editable": False, "advisor_editable": False}
            note_perms = {
                "student_note_editable": False,
                "class_note_editable": False,
                "advisor_note_editable": False,
            }
            score_map = {}
        locked_titles = auto_locked_titles(session, selected_semester.id)
        groups = get_criteria_tree(session)
        score_rows: list[dict] = []
        for group in groups:
            score_rows.append(
                {
                    "kind": "group",
                    "id": f"group-{group.id}",
                    "criterion_id": 0,
                    "title": vi(group.title),
                    "max_points": format_points(group.max_points),
                    "min_points": 0.0,
                    "max_points_value": float(group.max_points),
                    "range": "",
                    "self_score": "",
                    "class_score": "",
                    "advisor_score": "",
                    "self_editable": False,
                    "class_editable": False,
                    "advisor_editable": False,
                }
            )
            for criterion in group.criteria:
                score = score_map.get(criterion.id)
                hide_zero = (
                    submission is not None
                    and semester_evaluation_calendar_open(selected_semester)
                    and submission.status == "draft"
                    and criterion.title not in VISIBLE_ZEROS
                )
                auto_locked = criterion.title in locked_titles
                score_rows.append(
                    {
                        "kind": "item",
                        "id": f"criterion-{criterion.id}",
                        "criterion_id": criterion.id,
                        "title": vi(criterion.title),
                        "min_points": float(criterion.min_points),
                        "max_points_value": float(criterion.max_points),
                        "range": f"[{criterion.min_points:g} - {criterion.max_points:g}]",
                        "self_score": format_points(score.self_score if score else 0.0, hide_zero=hide_zero),
                        "class_score": format_points(score.class_score if score else 0.0, hide_zero=hide_zero),
                        "advisor_score": format_points(score.advisor_score if score else 0.0, hide_zero=hide_zero),
                        "self_editable": permissions["self_editable"] and not auto_locked,
                        "class_editable": permissions["class_editable"] and not auto_locked,
                        "advisor_editable": permissions["advisor_editable"] and not auto_locked,
                        "auto_locked": auto_locked,
                    }
                )

        evidences = []
        if target_is_student:
            evidences = list(
                session.scalars(
                    select(ReflexEvidence)
                    .where(
                        ReflexEvidence.student_id == target_student.id,
                        ReflexEvidence.semester_id == selected_semester.id,
                        ReflexEvidence.category_key == category_key,
                    )
                    .options(joinedload(ReflexEvidence.creator))
                    .order_by(ReflexEvidence.created_at.desc())
                )
            )
        evidence_rows = []
        for index, evidence in enumerate(evidences, start=1):
            perms = evidence_permissions(current_user, target_student, evidence, selected_semester)
            evidence_rows.append(
                {
                    "id": evidence.id,
                    "index": index,
                    "student_code": target_student.student_code or "",
                    "full_name": vi(target_student.full_name),
                    "class_name": target_student.class_name or "",
                    "reporter_name": vi(evidence.creator.full_name if evidence.creator else target_student.full_name),
                    "status_label": EVIDENCE_STATUS_LABELS.get(evidence.status, evidence.status),
                    "can_view": True,
                    "can_delete": perms["can_delete"],
                    "can_class_review": perms["can_class_review"],
                    "can_advisor_review": perms["can_advisor_review"],
                }
            )

        if target_is_student:
            joined_events, registered_events, open_events = build_event_lists(session, current_user, target_student, selected_semester)
        else:
            joined_events, registered_events, open_events = [], [], []

        student_ids = [student.id for student in students]
        student_submission_map = {
            item.student_id: item
            for item in session.scalars(
                select(ReflexSubmission).where(
                    ReflexSubmission.student_id.in_(student_ids),
                    ReflexSubmission.semester_id == selected_semester.id,
                )
            )
        }
        pending_evidence_counts: dict[int, int] = {}
        for evidence in session.scalars(
            select(ReflexEvidence).where(
                ReflexEvidence.student_id.in_(student_ids),
                ReflexEvidence.semester_id == selected_semester.id,
                ReflexEvidence.status == "pending_class",
            )
        ):
            pending_evidence_counts[evidence.student_id] = pending_evidence_counts.get(evidence.student_id, 0) + 1
        pending_event_counts: dict[int, int] = {}
        for participation in session.scalars(
            select(EventParticipation)
            .join(Event, Event.id == EventParticipation.event_id)
            .where(
                EventParticipation.student_id.in_(student_ids),
                Event.semester_id == selected_semester.id,
                EventParticipation.status == ParticipationStatus.PENDING,
            )
        ):
            pending_event_counts[participation.student_id] = pending_event_counts.get(participation.student_id, 0) + 1

        student_items = [
            serialize_student(
                user,
                student_submission_map.get(user.id),
                pending_evidence_counts.get(user.id, 0),
                pending_event_counts.get(user.id, 0),
                format_points(semester_metrics_for_user(session, user, selected_semester).get("gpa", 0.0)),
            )
            for user in students
        ]
        role_management_rows = build_role_management_rows(session, current_user)
        role_management_classes = build_role_management_classes(role_management_rows)
        profile_card = student_profile_snapshot(session, target_student, selected_semester.name)
        submission_status = submission.status if submission else ""
        submission_status_label = SUBMISSION_LABELS.get(submission_status, submission_status) if submission else ""
        score_total = format_points(submission.self_total if submission else 0.0)
        score_effective_total = format_points(effective_conduct_total(submission))
        score_total_class = format_points(submission.class_total if submission else 0.0)
        score_total_advisor = format_points(submission.advisor_total if submission else 0.0)
        conduct_label = conduct_grade_label(effective_conduct_total(submission)) if submission else "—"
        return {
            "selected_account_id": current_user.id,
            "current_user_name": vi(current_user.full_name),
            "current_user_initial": vi(current_user.full_name)[:1].upper(),
            "current_user_role": current_user.role.value,
            "current_user_role_label": role_label(current_user.role.value),
            "current_user_email": current_user.email or "",
            "current_user_faculty": vi(current_user.faculty or ""),
            "current_user_class_name": current_user.class_name or "",
            "current_user_student_code": current_user.student_code or "",
            "role_management_rows": role_management_rows,
            "role_management_classes": role_management_classes,
            "students": student_items,
            "selected_student_id": target_student.id,
            "selected_student_label": next(
                (item["label"] for item in student_items if item["id"] == target_student.id),
                f"{vi(target_student.full_name)} - {target_student.student_code or ''}".strip(),
            ),
            "selected_student_name": vi(target_student.full_name),
            "selected_student_code": target_student.student_code or "",
            "selected_student_class": target_student.class_name or "",
            "semesters": [{"id": semester.id, "name": vi(semester.name)} for semester in semesters],
            "selected_semester_id": selected_semester.id,
            "selected_semester_name": vi(selected_semester.name),
            "timeline": timeline_from_submission(selected_semester, submission_status or "draft"),
            "outside_window": is_outside_score_window(current_user, target_student, selected_semester) if target_is_student else False,
            "submission_status": submission_status,
            "submission_status_label": submission_status_label,
            "score_rows": score_rows,
            "score_total": score_total,
            "score_effective_total": score_effective_total,
            "score_total_class": score_total_class,
            "score_total_advisor": score_total_advisor,
            "conduct_grade_label": conduct_label,
            "student_note": submission.student_note if submission else "",
            "class_note": submission.class_note if submission else "",
            "advisor_note": submission.advisor_note if submission else "",
            "can_edit_student_note": note_perms["student_note_editable"],
            "can_edit_class_note": note_perms["class_note_editable"],
            "can_edit_advisor_note": note_perms["advisor_note_editable"],
            "can_save_student": permissions["self_editable"],
            "can_save_class": permissions["class_editable"],
            "can_submit_student": permissions["self_editable"],
            "can_review_class": permissions["class_editable"],
            "can_review_advisor": permissions["advisor_editable"],
            "can_reset_submission": False,
            "evidence_categories": EVIDENCE_CATEGORIES,
            "selected_evidence_category": category_key,
            "evidence_rows": evidence_rows,
            "has_evidence_rows": bool(evidence_rows),
            "evidence_count": str(len(evidence_rows)),
            "can_create_evidence": target_is_student
            and semester_evaluation_calendar_open(selected_semester)
            and (
                current_user.role == UserRole.ADMIN
                or (
                    current_user.role in {UserRole.STUDENT, UserRole.CLASS_MONITOR}
                    and current_user.id == target_student.id
                    and current_window_index(selected_semester) == 0
                )
            ),
            "can_download_conduct_pdf": target_is_student
            and (
                current_user.role == UserRole.ADMIN
                or current_user.id == target_student.id
                or can_manage_student(current_user, target_student)
            ),
            "selected_semester_is_active": selected_semester.is_active,
            "criterion_choice_labels": [vi(criterion.title) for criterion in auto_event_criteria(session)],
            "criterion_choice_ids": [int(criterion.id) for criterion in auto_event_criteria(session)],
            "student_profile": profile_card,
            "selected_student_gpa": profile_card.get("gpa", "0"),
            "joined_events": joined_events,
            "registered_events": registered_events,
            "has_registered_events": bool(registered_events),
            "open_events": open_events,
            "has_open_events": bool(open_events),
            "admin_stage_window_rows": serialize_stage_windows_for_admin_editor(selected_semester)
            if current_user.role == UserRole.ADMIN
            else [],
        }


def update_user_role(current_user_id: int, target_user_id: int, new_role: str) -> None:
    ensure_reflex_demo_data()
    try:
        target_role = UserRole(new_role)
    except ValueError as exc:
        raise ValueError("Quyền được chọn không hợp lệ.") from exc

    with get_reflex_session() as session:
        current_user = session.get(User, current_user_id)
        target_user = session.get(User, target_user_id)
        if not current_user or not target_user:
            raise ValueError("Không tìm thấy tài khoản cần cập nhật.")
        if current_user.id == target_user.id:
            raise ValueError("Không tự đổi quyền của chính mình.")

        if current_user.role == UserRole.ADMIN:
            target_user.role = target_role
            return

        if current_user.role != UserRole.ADVISOR:
            raise ValueError("Bạn không có quyền cấp vai trò cho tài khoản khác.")
        if target_role not in {UserRole.STUDENT, UserRole.CLASS_MONITOR}:
            raise ValueError("Cố vấn chỉ được đổi giữa quyền Sinh viên và Ban cán sự.")
        if target_user.role not in {UserRole.STUDENT, UserRole.CLASS_MONITOR}:
            raise ValueError("Cố vấn chỉ được cấp quyền ban cán sự cho sinh viên trong lớp phụ trách.")
        if (target_user.class_name or "") not in managed_classes_for_user(current_user):
            raise ValueError("Tài khoản này không thuộc lớp do bạn phụ trách.")

        target_user.role = target_role


def delete_user_account(current_user_id: int, target_user_id: int) -> None:
    ensure_reflex_demo_data()
    suppressed_seed_usernames = load_suppressed_seed_usernames()
    deleted_seed_username: str | None = None
    with get_reflex_session() as session:
        current_user = session.get(User, current_user_id)
        target_user = session.get(User, target_user_id)
        if not current_user:
            raise ValueError("Không tìm thấy tài khoản đang đăng nhập.")
        if not target_user:
            raise ValueError("Không tìm thấy tài khoản cần xóa.")
        if current_user.id == target_user.id:
            raise ValueError("Không thể xóa chính tài khoản đang đăng nhập.")
        if current_user.role == UserRole.ADMIN:
            pass
        elif current_user.role == UserRole.ADVISOR:
            if target_user.role not in {UserRole.STUDENT, UserRole.CLASS_MONITOR}:
                raise ValueError("Cố vấn chỉ được xóa tài khoản sinh viên hoặc ban cán sự trong lớp phụ trách.")
            if (target_user.class_name or "") not in managed_classes_for_user(current_user):
                raise ValueError("Tài khoản này không thuộc lớp do bạn phụ trách.")
        else:
            raise ValueError("Bạn không có quyền xóa tài khoản.")

        if target_user.username in SEEDED_USERNAMES:
            deleted_seed_username = target_user.username

        for submission in list(
            session.scalars(select(ReflexSubmission).where(ReflexSubmission.student_id == target_user.id))
        ):
            session.delete(submission)
        for submission in list(
            session.scalars(select(LegacySubmission).where(LegacySubmission.student_id == target_user.id))
        ):
            session.delete(submission)
        for participation in list(
            session.scalars(select(EventParticipation).where(EventParticipation.student_id == target_user.id))
        ):
            session.delete(participation)
        for evidence in list(
            session.scalars(select(ReflexEvidence).where(ReflexEvidence.student_id == target_user.id))
        ):
            session.delete(evidence)

        for evidence in list(
            session.scalars(
                select(ReflexEvidence).where(
                    ReflexEvidence.created_by_id == target_user.id,
                    ReflexEvidence.student_id != target_user.id,
                )
            )
        ):
            evidence.created_by_id = evidence.student_id

        session.delete(target_user)
    if deleted_seed_username:
        suppressed_seed_usernames.add(deleted_seed_username)
        save_suppressed_seed_usernames(suppressed_seed_usernames)


def load_evidence_detail(evidence_id: int, current_user_id: int, target_student_id: int) -> dict:
    ensure_reflex_demo_data()
    with get_reflex_session() as session:
        current_user = session.get(User, current_user_id)
        target_student = session.get(User, target_student_id)
        evidence = session.scalar(
            select(ReflexEvidence)
            .where(ReflexEvidence.id == evidence_id)
            .options(joinedload(ReflexEvidence.creator), joinedload(ReflexEvidence.student))
        )
        if not current_user or not target_student or not evidence:
            raise ValueError("Không tìm thấy minh chứng.")
        semester = session.get(Semester, evidence.semester_id)
        if not semester:
            raise ValueError("Không tìm thấy học kỳ của minh chứng.")
        payload = load_payload(evidence)
        resolved_file_path = resolve_evidence_upload(
            str(payload.get("file_path", "") or ""),
            str(payload.get("file_name", "") or ""),
        )
        if resolved_file_path and payload.get("file_path") != resolved_file_path:
            payload["file_path"] = resolved_file_path
            evidence.payload_json = json.dumps(payload, ensure_ascii=False)
        return serialize_evidence_detail(evidence, current_user, target_student, semester)


def create_evidence(
    current_user_id: int,
    target_student_id: int,
    semester_id: int,
    category_key: str,
    payload: dict[str, str],
) -> None:
    ensure_reflex_demo_data()
    with get_reflex_session() as session:
        current_user = session.get(User, current_user_id)
        target_student = session.get(User, target_student_id)
        semester = session.get(Semester, semester_id)
        if not current_user or not target_student:
            raise ValueError("Không tìm thấy người dùng.")
        if not semester:
            raise ValueError("Không tìm thấy học kỳ.")
        if current_user.role not in {UserRole.STUDENT, UserRole.CLASS_MONITOR, UserRole.ADMIN}:
            raise ValueError("Vai trò hiện tại không được thêm minh chứng.")
        if current_user.role in {UserRole.STUDENT, UserRole.CLASS_MONITOR} and current_user.id != target_student.id:
            raise ValueError("Chỉ được khai báo minh chứng cho chính mình.")
        if current_user.role != UserRole.ADMIN and not semester_evaluation_calendar_open(semester):
            raise ValueError("Học kỳ không trong thời gian đánh giá; không thể thêm minh chứng.")
        if current_user.role != UserRole.ADMIN and current_window_index(semester) != 0:
            raise ValueError("Chỉ được khai báo minh chứng trong giai đoạn minh chứng.")
        now = current_app_time()

        session.add(
            ReflexEvidence(
                student_id=target_student.id,
                created_by_id=current_user.id,
                semester_id=semester_id,
                category_key=category_key,
                summary=summary_from_payload(category_key, payload),
                payload_json=json.dumps(payload, ensure_ascii=False),
                status="pending_class",
                created_at=now,
                submitted_at=now,
            )
        )


def delete_evidence(current_user_id: int, evidence_id: int) -> None:
    ensure_reflex_demo_data()
    with get_reflex_session() as session:
        current_user = session.get(User, current_user_id)
        evidence = session.get(ReflexEvidence, evidence_id)
        if not current_user or not evidence:
            raise ValueError("Không tìm thấy minh chứng.")
        allowed = current_user.role == UserRole.ADMIN or (
            current_user.role in {UserRole.STUDENT, UserRole.CLASS_MONITOR}
            and evidence.student_id == current_user.id
            and evidence.status == "pending_class"
        )
        if not allowed:
            raise ValueError("Bạn không có quyền xóa minh chứng này.")
        semester = session.get(Semester, evidence.semester_id)
        if semester and current_user.role != UserRole.ADMIN and not semester_evaluation_calendar_open(semester):
            raise ValueError("Học kỳ đã đóng theo mốc thời gian; không thể xóa minh chứng.")
        if (
            semester
            and current_user.role != UserRole.ADMIN
            and current_window_index(semester) != 0
        ):
            raise ValueError("Chỉ được xóa minh chứng trong giai đoạn minh chứng.")
        payload = load_payload(evidence)
        delete_evidence_upload(
            resolve_evidence_upload(
                str(payload.get("file_path", "") or ""),
                str(payload.get("file_name", "") or ""),
            )
        )
        session.delete(evidence)


def review_evidence(current_user_id: int, evidence_id: int, action: str) -> None:
    ensure_reflex_demo_data()
    with get_reflex_session() as session:
        current_user = session.get(User, current_user_id)
        evidence = session.get(ReflexEvidence, evidence_id)
        if not current_user or not evidence:
            raise ValueError("Không tìm thấy minh chứng.")
        target_student = session.get(User, evidence.student_id)
        if not target_student or not can_manage_student(current_user, target_student):
            raise ValueError("Bạn không có quyền xử lý minh chứng này.")

        semester = session.get(Semester, evidence.semester_id)
        if semester and current_user.role != UserRole.ADMIN and not semester_evaluation_calendar_open(semester):
            raise ValueError("Học kỳ không trong thời gian đánh giá; không thể duyệt minh chứng.")
        if (
            semester
            and current_user.role == UserRole.CLASS_MONITOR
            and current_window_index(semester) != 0
        ):
            raise ValueError("Chưa trong thời gian được duyệt minh chứng.")
        now = current_app_time()

        if action == "class_approve":
            allowed = current_user.role == UserRole.CLASS_MONITOR and evidence.status == "pending_class"
            if not allowed:
                raise ValueError("Không thể duyệt minh chứng ở bước ban cán sự.")
            evidence.status = "class_approved"
            evidence.class_reviewed_at = now
        elif action == "advisor_approve":
            raise ValueError("Minh chứng chỉ cần ban cán sự duyệt.")
        elif action == "reject":
            if current_user.role != UserRole.CLASS_MONITOR or evidence.status != "pending_class":
                raise ValueError("Không có quyền từ chối minh chứng.")
            evidence.status = "rejected"
        else:
            raise ValueError("Hành động không hợp lệ.")


def save_submission_scores(
    current_user_id: int,
    target_student_id: int,
    semester_id: int,
    payload: dict[int, dict[str, str]],
    notes: dict[str, str],
    action: str,
) -> None:
    ensure_reflex_demo_data()
    with get_reflex_session() as session:
        current_user = session.get(User, current_user_id)
        target_student = session.get(User, target_student_id)
        semester = session.get(Semester, semester_id)
        if not current_user or not target_student or not semester:
            raise ValueError("Không tìm thấy dữ liệu phiếu điểm.")
        if current_user.role != UserRole.ADMIN and not semester_evaluation_calendar_open(semester):
            raise ValueError("Học kỳ đã đóng theo mốc thời gian đánh giá; không thể lưu phiếu.")
        if not can_manage_student(current_user, target_student):
            raise ValueError("Bạn không có quyền thao tác với phiếu điểm này.")

        submission = session.scalar(
            select(ReflexSubmission)
            .where(ReflexSubmission.student_id == target_student.id, ReflexSubmission.semester_id == semester.id)
            .options(joinedload(ReflexSubmission.scores).joinedload(ReflexScore.criterion))
        )
        if not submission:
            criteria = list(session.scalars(select(Criterion).order_by(Criterion.group_id, Criterion.display_order)))
            submission = ensure_reflex_submission(session, target_student, semester, criteria, status="draft")

        apply_automatic_scores(session, submission, target_student, semester)
        permissions = score_permissions(current_user, target_student, submission, semester)
        note_perms = note_permissions(current_user, target_student, submission, semester)
        locked_titles = auto_locked_titles(session, semester.id)
        now = current_app_time()

        for score in submission.scores:
            row = payload.get(score.criterion_id, {})
            criterion = score.criterion
            if not criterion:
                continue
            is_locked = criterion.title in locked_titles
            if "self_score" in row and permissions["self_editable"] and not is_locked:
                score.self_score = clamp_score(row["self_score"], criterion)
            if "class_score" in row and permissions["class_editable"] and not is_locked:
                score.class_score = clamp_score(row["class_score"], criterion)
            if "advisor_score" in row and permissions["advisor_editable"] and not is_locked:
                score.advisor_score = clamp_score(row["advisor_score"], criterion)

        apply_automatic_scores(session, submission, target_student, semester)

        if action == "save_draft":
            if not permissions["self_editable"]:
                raise ValueError("Bạn không thể lưu phiếu điểm ở giai đoạn hiện tại.")
            submission.status = "draft"
            if note_perms["student_note_editable"]:
                submission.student_note = notes.get("student_note", "").strip()
        elif action == "save_class":
            if not permissions["class_editable"]:
                raise ValueError("Bạn không thể lưu phiếu ở bước ban cán sự.")
            if note_perms["class_note_editable"]:
                submission.class_note = notes.get("class_note", "").strip()
            for score in submission.scores:
                score.advisor_score = score.class_score
        elif action == "submit_student":
            if not permissions["self_editable"]:
                raise ValueError("Bạn không thể gửi phiếu điểm ở giai đoạn hiện tại.")
            submission.status = "student_submitted"
            if note_perms["student_note_editable"]:
                submission.student_note = notes.get("student_note", "").strip()
            submission.submitted_at = now
            for score in submission.scores:
                score.class_score = score.self_score
                score.advisor_score = score.self_score
        elif action == "review_class":
            if not permissions["class_editable"]:
                raise ValueError("Bạn không thể duyệt phiếu ở bước ban cán sự.")
            submission.status = "class_reviewed"
            if note_perms["class_note_editable"]:
                submission.class_note = notes.get("class_note", "").strip()
            submission.class_reviewed_at = now
            for score in submission.scores:
                score.advisor_score = score.class_score
        elif action == "review_advisor":
            if not permissions["advisor_editable"]:
                raise ValueError("Bạn không thể xác nhận phiếu ở bước cố vấn học tập.")
            submission.status = "advisor_reviewed"
            if note_perms["advisor_note_editable"]:
                submission.advisor_note = notes.get("advisor_note", "").strip()
            submission.advisor_reviewed_at = now
        elif action == "reset":
            if current_user.role != UserRole.ADMIN:
                raise ValueError("Chỉ admin mới được đặt lại phiếu.")
            submission.status = "draft"
            submission.submitted_at = None
            submission.class_reviewed_at = None
            submission.advisor_reviewed_at = None
        else:
            raise ValueError("Hành động không hợp lệ.")

        recompute_totals(submission)


def register_event_for_student(current_user_id: int, target_student_id: int, event_id: int) -> None:
    ensure_reflex_demo_data()
    with get_reflex_session() as session:
        current_user = session.get(User, current_user_id)
        target_student = session.get(User, target_student_id)
        event = session.get(Event, event_id)
        if not current_user:
            raise ValueError("Không tìm thấy người dùng.")
        if not target_student:
            raise ValueError("Không tìm thấy sinh viên.")
        if not event:
            raise ValueError("Không tìm thấy sự kiện.")
        event_semester = session.get(Semester, event.semester_id)
        if not event_semester or not event_semester.is_active:
            raise ValueError("Chỉ được đăng ký sự kiện trong học kỳ hiện tại.")
        if current_user.role not in {UserRole.STUDENT, UserRole.CLASS_MONITOR, UserRole.ADMIN}:
            raise ValueError("Vai trò hiện tại không được đăng ký sự kiện.")
        if current_user.role in {UserRole.STUDENT, UserRole.CLASS_MONITOR} and current_user.id != target_student.id:
            raise ValueError("Chỉ được đăng ký sự kiện cho chính mình.")
        try:
            submit_event_participation(session, target_student_id, event_id)
        except ValueError as exc:
            raise ValueError(str(exc)) from exc


def export_conduct_pdf_bytes(current_user_id: int, target_student_id: int, semester_id: int) -> bytes:
    try:
        from ptit_reflex import pdf_export
    except ModuleNotFoundError as exc:
        if (exc.name or "").split(".")[0] == "fpdf":
            raise ValueError(
                "Thiếu thư viện tạo PDF (fpdf2). Hãy chạy 'pip install -r requirements.txt' rồi mở lại ứng dụng."
            ) from exc
        raise

    ensure_reflex_demo_data()
    with get_reflex_session() as session:
        current_user = session.get(User, current_user_id)
        target = session.get(User, target_student_id)
        semester = session.get(Semester, semester_id)
        if not current_user or not target or not semester:
            raise ValueError("Không tìm thấy dữ liệu.")
        if current_user.role != UserRole.ADMIN and current_user.id != target.id and not can_manage_student(current_user, target):
            raise ValueError("Bạn không có quyền tải phiếu này.")

        submission = session.scalar(
            select(ReflexSubmission)
            .where(ReflexSubmission.student_id == target.id, ReflexSubmission.semester_id == semester.id)
            .options(joinedload(ReflexSubmission.scores).joinedload(ReflexScore.criterion))
        )
        if not submission:
            criteria = list(session.scalars(select(Criterion).order_by(Criterion.group_id, Criterion.display_order)))
            submission = ensure_reflex_submission(session, target, semester, criteria, status="draft")

        if submission.status != "advisor_reviewed":
            apply_automatic_scores(session, submission, target, semester)
        recompute_totals(submission)

        groups = get_criteria_tree(session)
        score_map = {score.criterion_id: score for score in submission.scores}
        rows: list[dict[str, str]] = []
        for group in groups:
            rows.append(
                {
                    "kind": "group",
                    "title": vi(group.title),
                    "range": format_points(group.max_points),
                    "self_score": "",
                    "class_score": "",
                    "advisor_score": "",
                }
            )
            for criterion in group.criteria:
                score = score_map.get(criterion.id)
                rows.append(
                    {
                        "kind": "item",
                        "title": vi(criterion.title),
                        "range": f"[{criterion.min_points:g} - {criterion.max_points:g}]",
                        "self_score": format_points(score.self_score if score else 0.0),
                        "class_score": format_points(score.class_score if score else 0.0),
                        "advisor_score": format_points(score.advisor_score if score else 0.0),
                    }
                )

        eff = effective_conduct_total(submission)
        return pdf_export.build_conduct_pdf_bytes(
            semester_name=vi(semester.name),
            student_name=vi(target.full_name),
            student_code=target.student_code or "",
            class_name=target.class_name or "",
            status_label=SUBMISSION_LABELS.get(submission.status, submission.status),
            self_total=format_points(submission.self_total),
            class_total=format_points(submission.class_total),
            advisor_total=format_points(submission.advisor_total),
            grade_label=conduct_grade_label(eff),
            table_rows=rows,
        )


def create_admin_event(
    current_user_id: int,
    semester_id: int,
    criterion_id: int,
    name: str,
    points: float,
    start_time: str,
    end_time: str,
    location: str,
) -> None:
    ensure_reflex_demo_data()
    name = (name or "").strip()
    normalized_start = normalize_event_datetime_input(start_time)
    normalized_end = normalize_event_datetime_input(end_time)
    resolved_location = (location or "").strip()
    if not name:
        raise ValueError("Tên sự kiện không được để trống.")
    if not normalized_start:
        raise ValueError("Thời gian bắt đầu không được để trống.")
    if not normalized_end:
        raise ValueError("Thời gian kết thúc không được để trống.")
    if not resolved_location:
        raise ValueError("Địa điểm không được để trống.")
    parsed_start = parse_event_datetime(normalized_start)
    parsed_end = parse_event_datetime(normalized_end)
    if not parsed_start or not parsed_end:
        raise ValueError("Thời gian sự kiện không hợp lệ.")
    if parsed_end <= parsed_start:
        raise ValueError("Thời gian kết thúc phải sau thời gian bắt đầu.")
    if float(points) <= 0:
        raise ValueError("Điểm tối đa phải lớn hơn 0.")
    with get_reflex_session() as session:
        current_user = session.get(User, current_user_id)
        if not current_user or current_user.role != UserRole.ADMIN:
            raise ValueError("Chỉ admin được tạo sự kiện.")
        semester = session.get(Semester, semester_id)
        criterion = session.get(Criterion, criterion_id)
        if not semester or not criterion:
            raise ValueError("Học kỳ hoặc tiêu chí không hợp lệ.")
        if criterion.title not in AUTO_EVENT_CRITERIA_TITLES:
            raise ValueError("Chỉ được tạo sự kiện cho 3 tiêu chí tự động tính điểm.")
        session.add(
            Event(
                semester_id=semester_id,
                criterion_id=criterion_id,
                name=name,
                points=float(points),
                start_time=normalized_start,
                end_time=normalized_end,
                location=resolved_location,
                is_active=True,
            )
        )


def approve_registered_event(current_user_id: int, participation_id: int) -> None:
    ensure_reflex_demo_data()
    with get_reflex_session() as session:
        current_user = session.get(User, current_user_id)
        participation = session.get(EventParticipation, participation_id)
        if not current_user or not participation:
            raise ValueError("Không tìm thấy đăng ký sự kiện.")
        target_student = session.get(User, participation.student_id)
        if current_user.role not in {UserRole.CLASS_MONITOR, UserRole.ADMIN}:
            raise ValueError("Chỉ ban cán sự hoặc admin được duyệt tham gia sự kiện.")
        if not target_student or not can_manage_student(current_user, target_student):
            raise ValueError("Bạn không có quyền duyệt đăng ký sự kiện này.")
        event = session.get(Event, participation.event_id)
        semester = session.get(Semester, event.semester_id) if event else None
        if current_user.role == UserRole.CLASS_MONITOR:
            if not semester or not semester_evaluation_calendar_open(semester):
                raise ValueError("Học kỳ không trong thời gian đánh giá; không thể duyệt sự kiện.")
            if current_window_index(semester) != 0:
                raise ValueError("Chỉ được duyệt sự kiện trong giai đoạn cập nhật, duyệt minh chứng.")
        approve_event_participation(session, participation_id)
