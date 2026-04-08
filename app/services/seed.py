from __future__ import annotations

from datetime import date

from sqlalchemy import func, select
from sqlalchemy.orm import Session

from app.models import Criterion, CriterionGroup, Semester, User, UserRole
from app.security import hash_password


CRITERION_BLUEPRINT = [
    {
        "title": "I. Y thuc hoc tap va chap hanh noi quy",
        "max_points": 25,
        "criteria": [
            ("Di hoc day du, dung gio", "Sinh vien tham gia hoc tap nghiem tuc, han che vang hoc khong ly do.", 10),
            ("Chap hanh quy che thi cu", "Khong vi pham quy che thi, kiem tra va cac quy dinh cua hoc vien.", 8),
            ("Chu dong tu hoc, nghien cuu", "Tham gia seminar, nghien cuu khoa hoc, boi duong kien thuc ngoai lop hoc.", 7),
        ],
    },
    {
        "title": "II. Y thuc chap hanh phap luat va quy dinh",
        "max_points": 20,
        "criteria": [
            ("Chap hanh phap luat", "Khong vi pham phap luat, an ninh trat tu, an toan giao thong.", 10),
            ("Thuc hien quy dinh noi tru, ngoai tru", "Bao cao, dang ky tam tru tam vang va chap hanh quy dinh dia phuong.", 5),
            ("Van hoa hoc duong", "Ung xu van minh, ton trong giang vien va ban hoc.", 5),
        ],
    },
    {
        "title": "III. Y thuc tham gia hoat dong chinh tri xa hoi",
        "max_points": 20,
        "criteria": [
            ("Tham gia hoat dong doan hoi", "Tham gia tinh nguyen, cong tac doan hoi, cau lac bo.", 10),
            ("Cong dong va xa hoi", "Dong gop cho cac hoat dong vi cong dong va ho tro ban hoc.", 5),
            ("Tuyen truyen hinh anh hoc vien", "Tham gia truyen thong, ket noi cuu sinh vien, huong nghiep.", 5),
        ],
    },
    {
        "title": "IV. Y thuc cong dan va quan he cong dong",
        "max_points": 15,
        "criteria": [
            ("Tinh than hop tac", "Doan ket, giup do ban be, tham gia xay dung tap the lop hoc.", 8),
            ("Trach nhiem cong dan", "Tham gia sinh hoat cong dan, bao ve moi truong va tai san cong.", 7),
        ],
    },
    {
        "title": "V. Y thuc va ket qua tham gia cong tac lop",
        "max_points": 20,
        "criteria": [
            ("Tham gia xay dung lop", "Dong gop y kien, tham gia sinh hoat lop, ho tro co van hoc tap.", 10),
            ("Nhan su lop/doan hoi", "Dam nhan vai tro lop truong, bi thu, can bo doan hoi hoac tro ly hoc tap.", 10),
        ],
    },
]


def seed_default_data(session: Session) -> None:
    if not session.scalar(select(func.count()).select_from(User)):
        session.add_all(
            [
                User(username="admin", password_hash=hash_password("admin123"), full_name="Quan tri he thong", role=UserRole.ADMIN, email="admin@ptit.edu.vn", faculty="PTIT"),
                User(username="covan", password_hash=hash_password("covan123"), full_name="Nguyen Thi Co Van", role=UserRole.ADVISOR, email="covan@ptit.edu.vn", faculty="Cong nghe thong tin"),
                User(username="b23dccn001", password_hash=hash_password("student123"), full_name="Tran Minh Anh", role=UserRole.STUDENT, student_code="B23DCCN001", email="anh.tm@ptit.edu.vn", class_name="D23CQCN01-N", faculty="Cong nghe thong tin", major="Ky thuat phan mem"),
                User(username="b23dccn002", password_hash=hash_password("student123"), full_name="Le Thu Ha", role=UserRole.STUDENT, student_code="B23DCCN002", email="ha.lt@ptit.edu.vn", class_name="D23CQCN01-N", faculty="Cong nghe thong tin", major="He thong thong tin"),
            ]
        )

    if not session.scalar(select(func.count()).select_from(Semester)):
        session.add_all(
            [
                Semester(name="Hoc ky 1 nam hoc 2025-2026", academic_year="2025-2026", start_date=date(2025, 9, 1), end_date=date(2026, 1, 15), is_active=False),
                Semester(name="Hoc ky 2 nam hoc 2025-2026", academic_year="2025-2026", start_date=date(2026, 2, 1), end_date=date(2026, 6, 15), is_active=True),
            ]
        )

    if not session.scalar(select(func.count()).select_from(CriterionGroup)):
        for group_order, group_blueprint in enumerate(CRITERION_BLUEPRINT, start=1):
            group = CriterionGroup(title=group_blueprint["title"], display_order=group_order, max_points=group_blueprint["max_points"])
            session.add(group)
            session.flush()
            for criterion_order, (title, description, max_points) in enumerate(group_blueprint["criteria"], start=1):
                session.add(
                    Criterion(
                        group_id=group.id,
                        title=title,
                        description=description,
                        max_points=max_points,
                        display_order=criterion_order,
                    )
                )
