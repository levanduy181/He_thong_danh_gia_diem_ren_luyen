from __future__ import annotations

from datetime import date, datetime

from sqlalchemy import func, select
from sqlalchemy.orm import Session

from ptit_reflex.models import Criterion, CriterionGroup, ScoreEntry, Semester, Submission, SubmissionStatus, User, UserRole, Event
from ptit_reflex.security import hash_password
CRITERION_BLUEPRINT = [
    {
        "title": "Tieu chi 1. Danh gia ve y thuc tham gia hoc tap",
        "max_points": 20,
        "criteria": [
            ("Y thuc va thai do trong hoc tap", "Sinh vien nghiem tuc, tich cuc trong hoc tap", 0.0, 3.0),
            ("Ket qua hoc tap trong ky hoc", "Diem tich luy hoc tap", 0.0, 10.0),
            ("Y thuc chap hanh tot noi quy ve cac ky thi", "Khong vi pham quy che thi", -4.0, 4.0),
            ("Y thuc va thai do tham gia cac hoat dong ngoai khoa, cac su kien lien quan den nghien cuu khoa hoc, hoc thuat, chuyen mon, Cau lac bo", "", 0.0, 2.0),
            ("Tinh than vuot kho, phan dau vuon len trong hoc tap", "Co DTBCTL hoc ky sau lon hon hoc ky truoc; doi voi sinh vien nam 1 thi khong co diem duoi 2.5", 0.0, 1.0),
        ],
    },
    {
        "title": "Tieu chi 2. Danh gia ve y thuc chap hanh noi quy, quy che, quy dinh trong Hoc vien",
        "max_points": 25,
        "criteria": [
            ("Thuc hien nghiem tuc cac noi quy, quy che, cac quy dinh hien hanh trong Hoc vien.", "", 0.0, 15.0),
            ("Thuc hien quy dinh ve cong tac noi tru, ngoai tru", "Diem tru neu vi pham", -5.0, 0.0),
            ("Thuc hien nghiem tuc cac buoi hop lop/ sinh hoat doan the do Hoc vien/Khoa/Vien, CVHT, Lop/Chi doan to chuc", "Tuy thuoc vao so buoi to chuc sinh hoat, hop", 0.0, 5.0),
            ("Tham gia cac buoi hoi thao viec lam, dinh huong nghe nghiep do Hoc vien to chuc", "", 0.0, 5.0),
        ],
    },
    {
        "title": "Tieu chi 3. Danh gia ve y thuc va ket qua tham gia hoat dong chinh tri- xa hoi, van hoa, van nghe, the thao, phong chong toi pham cac te nan xa hoi",
        "max_points": 20,
        "criteria": [
            ("Tham gia day du cac hoat dong chinh tri, xa hoi, the thao, tinh nguyen, cac buoi sinh hoat chuyen de", "", 0.0, 10.0),
            ("Tham gia cong tac xa hoi nhu: hien mau nhan dao, ung ho nguoi ngheo, bao lut", "", 0.0, 4.0),
            ("Tuyen truyen tich cuc hinh anh ve Truong/Khoa tren mang xa hoi", "", 0.0, 3.0),
            ("Tich cuc tham gia hoat dong phong chong toi pham, bao cao hanh vi lien quan toi ma tuy, te nan xa hoi", "", 0.0, 3.0),
            ("Dua tin sai lech, thieu kiem chung, binh luan tieu cuc ve Hoc vien/Khoa", "Diem tru", -10.0, 0.0),
        ],
    },
    {
        "title": "Tieu chi 4. Danh gia y thuc cong dan trong quan he cong dong",
        "max_points": 25,
        "criteria": [
            ("Chap hanh nghiem chinh chu truong cua Dang, phap luat cua Nha nuoc va dia phuong", "", 0.0, 8.0),
            ("Tich cuc tham gia tuyen truyen phap luat, co y thuc giu gin ve sinh chung", "", 0.0, 5.0),
            ("Co moi quan he dung muc voi Thay/Co, can bo, nhan vien Hoc vien", "", 0.0, 5.0),
            ("Co moi quan he tot voi ban be trong lop; tinh than doan ket, chia se, giup do", "", 0.0, 5.0),
            ("Duoc bieu duong khen thuong trong cac hoat dong y thuc cong dan", "", 0.0, 2.0),
            ("Vi pham an ninh, trat tu xa hoi, an toan giao thong", "Diem tru", -5.0, 0.0),
        ],
    },
    {
        "title": "Tieu chi 5. Danh gia ve y thuc va tham gia phu trach lop, cac doan the trong truong, thanh tich dac biet",
        "max_points": 10,
        "criteria": [
            ("Lop truong, lop pho, bi thu, BCH doan, chu nhiem cau lac bo...", "", 0.0, 4.0),
            ("Thanh vien tham gia cac Cau lac bo duoc ghi nhan hoan thanh nhiem vu...", "", 0.0, 3.0),
            ("Sinh vien dat thanh tich dac biet trong hoc tap, ren luyen", "", 0.0, 3.0),
        ],
    },
]

# Diem ren luyen gia cho tung hoc ky (theo thu tu: HK1 2024-2025, HK2 2024-2025, HK1 2025-2026)
# Moi phan tu la dict: criterion_title -> (self_score, advisor_score)
_FAKE_SCORES: list[list[dict[str, float]]] = [
    # HK1 2024-2025 - Student 1 (Tran Minh Anh): Kha, 76 diem
    [
        {"Y thuc va thai do trong hoc tap": 2.5, "Ket qua hoc tap trong ky hoc": 7.0, "Y thuc chap hanh tot noi quy ve cac ky thi": 3.0, "Y thuc va thai do tham gia cac hoat dong ngoai khoa, cac su kien lien quan den nghien cuu khoa hoc, hoc thuat, chuyen mon, Cau lac bo": 1.5, "Tinh than vuot kho, phan dau vuon len trong hoc tap": 1.0},
        {"Thuc hien nghiem tuc cac noi quy, quy che, cac quy dinh hien hanh trong Hoc vien.": 13.0, "Thuc hien quy dinh ve cong tac noi tru, ngoai tru": 0.0, "Thuc hien nghiem tuc cac buoi hop lop/ sinh hoat doan the do Hoc vien/Khoa/Vien, CVHT, Lop/Chi doan to chuc": 4.0, "Tham gia cac buoi hoi thao viec lam, dinh huong nghe nghiep do Hoc vien to chuc": 4.0},
        {"Tham gia day du cac hoat dong chinh tri, xa hoi, the thao, tinh nguyen, cac buoi sinh hoat chuyen de": 8.0, "Tham gia cong tac xa hoi nhu: hien mau nhan dao, ung ho nguoi ngheo, bao lut": 3.0, "Tuyen truyen tich cuc hinh anh ve Truong/Khoa tren mang xa hoi": 2.0, "Tich cuc tham gia hoat dong phong chong toi pham, bao cao hanh vi lien quan toi ma tuy, te nan xa hoi": 2.0, "Dua tin sai lech, thieu kiem chung, binh luan tieu cuc ve Hoc vien/Khoa": 0.0},
        {"Chap hanh nghiem chinh chu truong cua Dang, phap luat cua Nha nuoc va dia phuong": 7.0, "Tich cuc tham gia tuyen truyen phap luat, co y thuc giu gin ve sinh chung": 4.0, "Co moi quan he dung muc voi Thay/Co, can bo, nhan vien Hoc vien": 4.5, "Co moi quan he tot voi ban be trong lop; tinh than doan ket, chia se, giup do": 4.5, "Duoc bieu duong khen thuong trong cac hoat dong y thuc cong dan": 1.5, "Vi pham an ninh, trat tu xa hoi, an toan giao thong": 0.0},
        {"Lop truong, lop pho, bi thu, BCH doan, chu nhiem cau lac bo...": 0.0, "Thanh vien tham gia cac Cau lac bo duoc ghi nhan hoan thanh nhiem vu...": 2.0, "Sinh vien dat thanh tich dac biet trong hoc tap, ren luyen": 1.0},
    ],
    # HK2 2024-2025 - Student 1: Gioi, 83 diem
    [
        {"Y thuc va thai do trong hoc tap": 3.0, "Ket qua hoc tap trong ky hoc": 8.5, "Y thuc chap hanh tot noi quy ve cac ky thi": 4.0, "Y thuc va thai do tham gia cac hoat dong ngoai khoa, cac su kien lien quan den nghien cuu khoa hoc, hoc thuat, chuyen mon, Cau lac bo": 2.0, "Tinh than vuot kho, phan dau vuon len trong hoc tap": 1.0},
        {"Thuc hien nghiem tuc cac noi quy, quy che, cac quy dinh hien hanh trong Hoc vien.": 14.0, "Thuc hien quy dinh ve cong tac noi tru, ngoai tru": 0.0, "Thuc hien nghiem tuc cac buoi hop lop/ sinh hoat doan the do Hoc vien/Khoa/Vien, CVHT, Lop/Chi doan to chuc": 5.0, "Tham gia cac buoi hoi thao viec lam, dinh huong nghe nghiep do Hoc vien to chuc": 5.0},
        {"Tham gia day du cac hoat dong chinh tri, xa hoi, the thao, tinh nguyen, cac buoi sinh hoat chuyen de": 9.0, "Tham gia cong tac xa hoi nhu: hien mau nhan dao, ung ho nguoi ngheo, bao lut": 3.5, "Tuyen truyen tich cuc hinh anh ve Truong/Khoa tren mang xa hoi": 2.5, "Tich cuc tham gia hoat dong phong chong toi pham, bao cao hanh vi lien quan toi ma tuy, te nan xa hoi": 2.5, "Dua tin sai lech, thieu kiem chung, binh luan tieu cuc ve Hoc vien/Khoa": 0.0},
        {"Chap hanh nghiem chinh chu truong cua Dang, phap luat cua Nha nuoc va dia phuong": 7.5, "Tich cuc tham gia tuyen truyen phap luat, co y thuc giu gin ve sinh chung": 4.5, "Co moi quan he dung muc voi Thay/Co, can bo, nhan vien Hoc vien": 5.0, "Co moi quan he tot voi ban be trong lop; tinh than doan ket, chia se, giup do": 5.0, "Duoc bieu duong khen thuong trong cac hoat dong y thuc cong dan": 2.0, "Vi pham an ninh, trat tu xa hoi, an toan giao thong": 0.0},
        {"Lop truong, lop pho, bi thu, BCH doan, chu nhiem cau lac bo...": 0.0, "Thanh vien tham gia cac Cau lac bo duoc ghi nhan hoan thanh nhiem vu...": 3.0, "Sinh vien dat thanh tich dac biet trong hoc tap, ren luyen": 2.0},
    ],
    # HK1 2025-2026 - Student 1: Gioi, 88 diem
    [
        {"Y thuc va thai do trong hoc tap": 3.0, "Ket qua hoc tap trong ky hoc": 9.0, "Y thuc chap hanh tot noi quy ve cac ky thi": 4.0, "Y thuc va thai do tham gia cac hoat dong ngoai khoa, cac su kien lien quan den nghien cuu khoa hoc, hoc thuat, chuyen mon, Cau lac bo": 2.0, "Tinh than vuot kho, phan dau vuon len trong hoc tap": 1.0},
        {"Thuc hien nghiem tuc cac noi quy, quy che, cac quy dinh hien hanh trong Hoc vien.": 15.0, "Thuc hien quy dinh ve cong tac noi tru, ngoai tru": 0.0, "Thuc hien nghiem tuc cac buoi hop lop/ sinh hoat doan the do Hoc vien/Khoa/Vien, CVHT, Lop/Chi doan to chuc": 5.0, "Tham gia cac buoi hoi thao viec lam, dinh huong nghe nghiep do Hoc vien to chuc": 5.0},
        {"Tham gia day du cac hoat dong chinh tri, xa hoi, the thao, tinh nguyen, cac buoi sinh hoat chuyen de": 10.0, "Tham gia cong tac xa hoi nhu: hien mau nhan dao, ung ho nguoi ngheo, bao lut": 4.0, "Tuyen truyen tich cuc hinh anh ve Truong/Khoa tren mang xa hoi": 3.0, "Tich cuc tham gia hoat dong phong chong toi pham, bao cao hanh vi lien quan toi ma tuy, te nan xa hoi": 2.5, "Dua tin sai lech, thieu kiem chung, binh luan tieu cuc ve Hoc vien/Khoa": 0.0},
        {"Chap hanh nghiem chinh chu truong cua Dang, phap luat cua Nha nuoc va dia phuong": 8.0, "Tich cuc tham gia tuyen truyen phap luat, co y thuc giu gin ve sinh chung": 5.0, "Co moi quan he dung muc voi Thay/Co, can bo, nhan vien Hoc vien": 5.0, "Co moi quan he tot voi ban be trong lop; tinh than doan ket, chia se, giup do": 5.0, "Duoc bieu duong khen thuong trong cac hoat dong y thuc cong dan": 2.0, "Vi pham an ninh, trat tu xa hoi, an toan giao thong": 0.0},
        {"Lop truong, lop pho, bi thu, BCH doan, chu nhiem cau lac bo...": 3.0, "Thanh vien tham gia cac Cau lac bo duoc ghi nhan hoan thanh nhiem vu...": 3.0, "Sinh vien dat thanh tich dac biet trong hoc tap, ren luyen": 2.5},
    ],
]

# Student 2 (Le Thu Ha) - hoc luc thap hon
_FAKE_SCORES_ST2: list[list[dict[str, float]]] = [
    # HK1 2024-2025: Trung binh, 66 diem
    [
        {"Y thuc va thai do trong hoc tap": 2.0, "Ket qua hoc tap trong ky hoc": 5.5, "Y thuc chap hanh tot noi quy ve cac ky thi": 2.0, "Y thuc va thai do tham gia cac hoat dong ngoai khoa, cac su kien lien quan den nghien cuu khoa hoc, hoc thuat, chuyen mon, Cau lac bo": 1.0, "Tinh than vuot kho, phan dau vuon len trong hoc tap": 0.0},
        {"Thuc hien nghiem tuc cac noi quy, quy che, cac quy dinh hien hanh trong Hoc vien.": 11.0, "Thuc hien quy dinh ve cong tac noi tru, ngoai tru": 0.0, "Thuc hien nghiem tuc cac buoi hop lop/ sinh hoat doan the do Hoc vien/Khoa/Vien, CVHT, Lop/Chi doan to chuc": 3.5, "Tham gia cac buoi hoi thao viec lam, dinh huong nghe nghiep do Hoc vien to chuc": 3.0},
        {"Tham gia day du cac hoat dong chinh tri, xa hoi, the thao, tinh nguyen, cac buoi sinh hoat chuyen de": 7.0, "Tham gia cong tac xa hoi nhu: hien mau nhan dao, ung ho nguoi ngheo, bao lut": 2.5, "Tuyen truyen tich cuc hinh anh ve Truong/Khoa tren mang xa hoi": 1.5, "Tich cuc tham gia hoat dong phong chong toi pham, bao cao hanh vi lien quan toi ma tuy, te nan xa hoi": 1.5, "Dua tin sai lech, thieu kiem chung, binh luan tieu cuc ve Hoc vien/Khoa": 0.0},
        {"Chap hanh nghiem chinh chu truong cua Dang, phap luat cua Nha nuoc va dia phuong": 6.5, "Tich cuc tham gia tuyen truyen phap luat, co y thuc giu gin ve sinh chung": 3.5, "Co moi quan he dung muc voi Thay/Co, can bo, nhan vien Hoc vien": 3.5, "Co moi quan he tot voi ban be trong lop; tinh than doan ket, chia se, giup do": 4.0, "Duoc bieu duong khen thuong trong cac hoat dong y thuc cong dan": 1.0, "Vi pham an ninh, trat tu xa hoi, an toan giao thong": 0.0},
        {"Lop truong, lop pho, bi thu, BCH doan, chu nhiem cau lac bo...": 0.0, "Thanh vien tham gia cac Cau lac bo duoc ghi nhan hoan thanh nhiem vu...": 1.0, "Sinh vien dat thanh tich dac biet trong hoc tap, ren luyen": 0.0},
    ],
    # HK2 2024-2025: Kha, 74 diem
    [
        {"Y thuc va thai do trong hoc tap": 2.5, "Ket qua hoc tap trong ky hoc": 7.0, "Y thuc chap hanh tot noi quy ve cac ky thi": 3.0, "Y thuc va thai do tham gia cac hoat dong ngoai khoa, cac su kien lien quan den nghien cuu khoa hoc, hoc thuat, chuyen mon, Cau lac bo": 1.5, "Tinh than vuot kho, phan dau vuon len trong hoc tap": 1.0},
        {"Thuc hien nghiem tuc cac noi quy, quy che, cac quy dinh hien hanh trong Hoc vien.": 12.0, "Thuc hien quy dinh ve cong tac noi tru, ngoai tru": 0.0, "Thuc hien nghiem tuc cac buoi hop lop/ sinh hoat doan the do Hoc vien/Khoa/Vien, CVHT, Lop/Chi doan to chuc": 4.0, "Tham gia cac buoi hoi thao viec lam, dinh huong nghe nghiep do Hoc vien to chuc": 4.0},
        {"Tham gia day du cac hoat dong chinh tri, xa hoi, the thao, tinh nguyen, cac buoi sinh hoat chuyen de": 8.0, "Tham gia cong tac xa hoi nhu: hien mau nhan dao, ung ho nguoi ngheo, bao lut": 3.0, "Tuyen truyen tich cuc hinh anh ve Truong/Khoa tren mang xa hoi": 2.0, "Tich cuc tham gia hoat dong phong chong toi pham, bao cao hanh vi lien quan toi ma tuy, te nan xa hoi": 2.0, "Dua tin sai lech, thieu kiem chung, binh luan tieu cuc ve Hoc vien/Khoa": 0.0},
        {"Chap hanh nghiem chinh chu truong cua Dang, phap luat cua Nha nuoc va dia phuong": 7.0, "Tich cuc tham gia tuyen truyen phap luat, co y thuc giu gin ve sinh chung": 4.0, "Co moi quan he dung muc voi Thay/Co, can bo, nhan vien Hoc vien": 4.0, "Co moi quan he tot voi ban be trong lop; tinh than doan ket, chia se, giup do": 4.5, "Duoc bieu duong khen thuong trong cac hoat dong y thuc cong dan": 1.5, "Vi pham an ninh, trat tu xa hoi, an toan giao thong": 0.0},
        {"Lop truong, lop pho, bi thu, BCH doan, chu nhiem cau lac bo...": 0.0, "Thanh vien tham gia cac Cau lac bo duoc ghi nhan hoan thanh nhiem vu...": 2.0, "Sinh vien dat thanh tich dac biet trong hoc tap, ren luyen": 1.0},
    ],
    # HK1 2025-2026: Kha, 79 diem
    [
        {"Y thuc va thai do trong hoc tap": 2.5, "Ket qua hoc tap trong ky hoc": 8.0, "Y thuc chap hanh tot noi quy ve cac ky thi": 3.5, "Y thuc va thai do tham gia cac hoat dong ngoai khoa, cac su kien lien quan den nghien cuu khoa hoc, hoc thuat, chuyen mon, Cau lac bo": 2.0, "Tinh than vuot kho, phan dau vuon len trong hoc tap": 1.0},
        {"Thuc hien nghiem tuc cac noi quy, quy che, cac quy dinh hien hanh trong Hoc vien.": 13.0, "Thuc hien quy dinh ve cong tac noi tru, ngoai tru": 0.0, "Thuc hien nghiem tuc cac buoi hop lop/ sinh hoat doan the do Hoc vien/Khoa/Vien, CVHT, Lop/Chi doan to chuc": 4.5, "Tham gia cac buoi hoi thao viec lam, dinh huong nghe nghiep do Hoc vien to chuc": 4.5},
        {"Tham gia day du cac hoat dong chinh tri, xa hoi, the thao, tinh nguyen, cac buoi sinh hoat chuyen de": 8.5, "Tham gia cong tac xa hoi nhu: hien mau nhan dao, ung ho nguoi ngheo, bao lut": 3.5, "Tuyen truyen tich cuc hinh anh ve Truong/Khoa tren mang xa hoi": 2.5, "Tich cuc tham gia hoat dong phong chong toi pham, bao cao hanh vi lien quan toi ma tuy, te nan xa hoi": 2.0, "Dua tin sai lech, thieu kiem chung, binh luan tieu cuc ve Hoc vien/Khoa": 0.0},
        {"Chap hanh nghiem chinh chu truong cua Dang, phap luat cua Nha nuoc va dia phuong": 7.5, "Tich cuc tham gia tuyen truyen phap luat, co y thuc giu gin ve sinh chung": 4.5, "Co moi quan he dung muc voi Thay/Co, can bo, nhan vien Hoc vien": 4.5, "Co moi quan he tot voi ban be trong lop; tinh than doan ket, chia se, giup do": 5.0, "Duoc bieu duong khen thuong trong cac hoat dong y thuc cong dan": 1.5, "Vi pham an ninh, trat tu xa hoi, an toan giao thong": 0.0},
        {"Lop truong, lop pho, bi thu, BCH doan, chu nhiem cau lac bo...": 0.0, "Thanh vien tham gia cac Cau lac bo duoc ghi nhan hoan thanh nhiem vu...": 2.5, "Sinh vien dat thanh tich dac biet trong hoc tap, ren luyen": 1.5},
    ],
]


def _create_reviewed_submission(
    session: Session,
    student: User,
    semester: Semester,
    criteria: list[Criterion],
    score_data: list[dict],
    student_note: str,
    advisor_note: str,
) -> None:
    """Tao mot submission da duoc duyet co day du diem."""
    sub = Submission(
        student_id=student.id,
        semester_id=semester.id,
        status=SubmissionStatus.REVIEWED,
        student_note=student_note,
        advisor_note=advisor_note,
        submitted_at=datetime(semester.end_date.year, semester.end_date.month, max(1, semester.end_date.day - 20)),
        reviewed_at=datetime(semester.end_date.year, semester.end_date.month, semester.end_date.day),
        updated_at=datetime(semester.end_date.year, semester.end_date.month, semester.end_date.day),
    )
    session.add(sub)
    session.flush()

    # Ghep cac dict score lai thanh 1 dict phang
    flat_scores: dict[str, float] = {}
    for group_dict in score_data:
        flat_scores.update(group_dict)

    self_total = 0.0
    advisor_total = 0.0
    for criterion in criteria:
        self_score = flat_scores.get(criterion.title, 0.0)
        # Clamp trong khoang [min_points, max_points]
        self_score = max(criterion.min_points, min(self_score, criterion.max_points))
        advisor_score = self_score  # CVHT dng y voi SV
        self_total += self_score
        advisor_total += advisor_score
        entry = ScoreEntry(
            submission_id=sub.id,
            criterion_id=criterion.id,
            self_score=self_score,
            advisor_score=advisor_score,
            evidence="Sinh vien da nop minh chung day du.",
            evidence_type="Tham gia cong tac xa hoi",
            advisor_feedback="Da xem xet va chap thuan.",
        )
        session.add(entry)

    sub.self_total = round(self_total, 2)
    sub.advisor_total = round(advisor_total, 2)
    session.flush()


def seed_historical_submissions(session: Session) -> None:
    """Tao du lieu diem ren luyen gia cho cac hoc ky truoc neu chua co."""
    past_semesters = list(session.scalars(
        select(Semester).where(Semester.is_active.is_(False)).order_by(Semester.start_date)
    ))
    if not past_semesters:
        return

    students = list(session.scalars(
        select(User).where(User.role == UserRole.STUDENT).order_by(User.student_code)
    ))
    if not students:
        return

    criteria = list(session.scalars(select(Criterion).order_by(Criterion.group_id, Criterion.display_order)))
    if not criteria:
        return

    # Kiem tra da co du lieu lich su chua
    existing_count = session.scalar(
        select(func.count()).select_from(Submission).where(
            Submission.semester_id.in_([s.id for s in past_semesters])
        )
    ) or 0
    if existing_count > 0:
        return

    all_fake = [_FAKE_SCORES, _FAKE_SCORES_ST2]
    notes_st1 = [
        "Sinh vien nho can co gang hon o hoc ky tiep theo.",
        "Trang bi them ky nang mem de phat trien ban than.",
        "Xuat sac trong cac hoat dong ngoai khoa, tiep tuc phat huy.",
    ]
    notes_st2 = [
        "Can chu y hon den viec tham gia cac hoat dong tap the.",
        "Da co tien bo so voi hoc ky truoc, tiep tuc co gang.",
        "Phan dau dat muc Gioi trong hoc ky toi.",
    ]
    notes_advisor = [
        "CVHT da xem xet va xac nhan ket qua danh gia.",
        "Sinh vien chap hanh tot quy che, xac nhan cac hoat dong theo minh chung.",
        "Ket qua danh gia phu hop voi qua trinh theo doi cua CVHT.",
    ]

    for si, student in enumerate(students[:2]):  # chi seed 2 sinh vien demo
        fake_data = all_fake[si] if si < len(all_fake) else _FAKE_SCORES
        notes = notes_st1 if si == 0 else notes_st2
        for ki, semester in enumerate(past_semesters[:3]):  # 3 ky truoc
            score_data = fake_data[ki] if ki < len(fake_data) else fake_data[-1]
            _create_reviewed_submission(
                session,
                student,
                semester,
                criteria,
                score_data,
                notes[ki],
                notes_advisor[ki],
            )


def seed_default_data(session: Session) -> None:
    if not session.scalar(select(func.count()).select_from(User)):
        session.add_all(
            [
                User(username="admin", password_hash=hash_password("admin123"), full_name="Quan tri he thong", role=UserRole.ADMIN, email="admin@ptit.edu.vn", faculty="PTIT"),
                User(username="covan", password_hash=hash_password("covan123"), full_name="Nguyen Thi Co Van", role=UserRole.ADVISOR, email="covan@ptit.edu.vn", faculty="Cong nghe thong tin"),
                User(username="bancansu", password_hash=hash_password("bcs123"), full_name="Nguyen Van Lop Truong", role=UserRole.CLASS_MONITOR, email="bancansu@ptit.edu.vn", class_name="D23CQCN01-N", faculty="Cong nghe thong tin", major="Ky thuat phan mem"),
                User(username="b23dccn001", password_hash=hash_password("student123"), full_name="Tran Minh Anh", role=UserRole.STUDENT, student_code="B23DCCN001", email="anh.tm@ptit.edu.vn", class_name="D23CQCN01-N", faculty="Cong nghe thong tin", major="Ky thuat phan mem"),
                User(username="b23dccn002", password_hash=hash_password("student123"), full_name="Le Thu Ha", role=UserRole.STUDENT, student_code="B23DCCN002", email="ha.lt@ptit.edu.vn", class_name="D23CQCN01-N", faculty="Cong nghe thong tin", major="He thong thong tin"),
            ]
        )

    if not session.scalar(select(func.count()).select_from(Semester)):
        session.add_all(
            [
                Semester(name="Hoc ky 1 nam hoc 2024-2025", academic_year="2024-2025", start_date=date(2024, 9, 1), end_date=date(2025, 1, 15), is_active=False),
                Semester(name="Hoc ky 2 nam hoc 2024-2025", academic_year="2024-2025", start_date=date(2025, 2, 1), end_date=date(2025, 6, 15), is_active=False),
                Semester(name="Hoc ky 1 nam hoc 2025-2026", academic_year="2025-2026", start_date=date(2025, 9, 1), end_date=date(2026, 1, 15), is_active=False),
                Semester(name="Hoc ky 2 nam hoc 2025-2026", academic_year="2025-2026", start_date=date(2026, 2, 1), end_date=date(2026, 6, 15), is_active=True),
            ]
        )

    if not session.scalar(select(func.count()).select_from(CriterionGroup)):
        for group_order, group_blueprint in enumerate(CRITERION_BLUEPRINT, start=1):
            group = CriterionGroup(title=group_blueprint["title"], display_order=group_order, max_points=group_blueprint["max_points"])
            session.add(group)
            session.flush()
            for criterion_order, (title, description, min_points, max_points) in enumerate(group_blueprint["criteria"], start=1):
                session.add(
                    Criterion(
                        group_id=group.id,
                        title=title,
                        description=description,
                        min_points=min_points,
                        max_points=max_points,
                        display_order=criterion_order,
                    )
                )

    if not session.scalar(select(func.count()).select_from(Event)):
        active_semester = session.scalar(select(Semester).where(Semester.is_active.is_(True)))
        c1 = session.scalar(select(Criterion).where(Criterion.title == "Tham gia day du cac hoat dong chinh tri, xa hoi, the thao, tinh nguyen, cac buoi sinh hoat chuyen de"))
        c2 = session.scalar(select(Criterion).where(Criterion.title == "Tuyen truyen tich cuc hinh anh ve Truong/Khoa tren mang xa hoi"))
        if active_semester and c1 and c2:
            session.add_all([
                Event(
                    semester_id=active_semester.id,
                    criterion_id=c1.id,
                    name="Chien dich Mua he Xanh 2026",
                    points=5.0,
                    qr_code="QR-MHX2026",
                ),
                Event(
                    semester_id=active_semester.id,
                    criterion_id=c2.id,
                    name="Truyen thong tuyen sinh PTIT 2026",
                    points=3.0,
                    qr_code="QR-TS2026",
                )
            ])

    # Seed du lieu lich su cho cac ky truoc
    seed_historical_submissions(session)
