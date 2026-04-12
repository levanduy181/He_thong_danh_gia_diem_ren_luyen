from __future__ import annotations

from datetime import date

from sqlalchemy import func, select
from sqlalchemy.orm import Session

from ptit_reflex.models import Criterion, CriterionGroup, Semester, User, UserRole


CRITERION_BLUEPRINT = [
    {
        "title": "Tieu chi 1. Danh gia ve y thuc tham gia hoc tap",
        "max_points": 23,
        "criteria": [
            ("Y thuc va thai do trong hoc tap", "Sinh vien nghiem tuc, tich cuc trong hoc tap", 0.0, 3.0),
            ("Ket qua hoc tap trong ky hoc", "Diem tich luy hoc tap", 0.0, 10.0),
            ("Y thuc chap hanh tot noi quy ve cac ky thi", "Khong vi pham quy che thi", -4.0, 4.0),
            (
                "Y thuc va thai do tham gia cac hoat dong ngoai khoa, cac su kien lien quan den nghien cuu khoa hoc, hoc thuat, chuyen mon, Cau lac bo",
                "",
                0.0,
                5.0,
            ),
            (
                "Tinh than vuot kho, phan dau vuon len trong hoc tap",
                "Co DTBCTL hoc ky sau lon hon hoc ky truoc; doi voi sinh vien nam 1 thi khong co diem duoi 2.5",
                0.0,
                1.0,
            ),
        ],
    },
    {
        "title": "Tieu chi 2. Danh gia ve y thuc chap hanh noi quy, quy che, quy dinh trong Hoc vien",
        "max_points": 25,
        "criteria": [
            ("Thuc hien nghiem tuc cac noi quy, quy che, cac quy dinh hien hanh trong Hoc vien.", "", 0.0, 15.0),
            ("Thuc hien quy dinh ve cong tac noi tru, ngoai tru", "Diem tru neu vi pham", -5.0, 0.0),
            (
                "Thuc hien nghiem tuc cac buoi hop lop/ sinh hoat doan the do Hoc vien/Khoa/Vien, CVHT, Lop/Chi doan to chuc",
                "Tuy thuoc vao so buoi to chuc sinh hoat, hop",
                0.0,
                5.0,
            ),
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
        "max_points": 7,
        "criteria": [
            ("Lop truong, lop pho, bi thu, BCH doan, chu nhiem cau lac bo...", "", 0.0, 4.0),
            ("Sinh vien dat thanh tich dac biet trong hoc tap, ren luyen", "", 0.0, 3.0),
        ],
    },
]


DEFAULT_USERS = [
    {
        "username": "admin",
        "password_hash": "admin123",
        "full_name": "Quan tri he thong",
        "role": UserRole.ADMIN,
        "email": "admin@ptit.edu.vn",
        "faculty": "PTIT",
    },
    {
        "username": "CVHT001",
        "password_hash": "CVHT001",
        "full_name": "Co van hoc tap 001",
        "role": UserRole.ADVISOR,
        "student_code": "CVHT001",
        "email": "CVHT001@ptit.edu.vn",
        "class_name": "D23CQAT01",
        "faculty": "An toan thong tin",
        "major": "An toan thong tin",
    },
    {
        "username": "CVHT002",
        "password_hash": "CVHT002",
        "full_name": "Co van hoc tap 002",
        "role": UserRole.ADVISOR,
        "student_code": "CVHT002",
        "email": "CVHT002@ptit.edu.vn",
        "class_name": "D23CQAT02",
        "faculty": "An toan thong tin",
        "major": "An toan thong tin",
    },
    {
        "username": "CVHT003",
        "password_hash": "CVHT003",
        "full_name": "Co van hoc tap 003",
        "role": UserRole.ADVISOR,
        "student_code": "CVHT003",
        "email": "CVHT003@ptit.edu.vn",
        "class_name": "D23CQCN01",
        "faculty": "Cong nghe thong tin",
        "major": "Cong nghe thong tin",
    },
    {
        "username": "CVHT004",
        "password_hash": "CVHT004",
        "full_name": "Co van hoc tap 004",
        "role": UserRole.ADVISOR,
        "student_code": "CVHT004",
        "email": "CVHT004@ptit.edu.vn",
        "class_name": "D23CQCN02",
        "faculty": "Cong nghe thong tin",
        "major": "Cong nghe thong tin",
    },
    {
        "username": "B23DCAT001",
        "password_hash": "B23DCAT001",
        "full_name": "Nguyen An Khang",
        "role": UserRole.STUDENT,
        "student_code": "B23DCAT001",
        "email": "b23dcat001@stu.ptit.edu.vn",
        "class_name": "D23CQAT01",
        "faculty": "An toan thong tin",
        "major": "An toan thong tin",
    },
    {
        "username": "B23DCAT002",
        "password_hash": "B23DCAT002",
        "full_name": "Tran Minh Anh",
        "role": UserRole.STUDENT,
        "student_code": "B23DCAT002",
        "email": "b23dcat002@stu.ptit.edu.vn",
        "class_name": "D23CQAT01",
        "faculty": "An toan thong tin",
        "major": "An toan thong tin",
    },
    {
        "username": "B23DCAT003",
        "password_hash": "B23DCAT003",
        "full_name": "Le Thu Ha",
        "role": UserRole.STUDENT,
        "student_code": "B23DCAT003",
        "email": "b23dcat003@stu.ptit.edu.vn",
        "class_name": "D23CQAT02",
        "faculty": "An toan thong tin",
        "major": "An toan thong tin",
    },
    {
        "username": "B23DCAT004",
        "password_hash": "B23DCAT004",
        "full_name": "Pham Gia Han",
        "role": UserRole.STUDENT,
        "student_code": "B23DCAT004",
        "email": "b23dcat004@stu.ptit.edu.vn",
        "class_name": "D23CQAT02",
        "faculty": "An toan thong tin",
        "major": "An toan thong tin",
    },
    {
        "username": "B23DCCN001",
        "password_hash": "B23DCCN001",
        "full_name": "Nguyen Hoang Nam",
        "role": UserRole.STUDENT,
        "student_code": "B23DCCN001",
        "email": "b23dccn001@stu.ptit.edu.vn",
        "class_name": "D23CQCN01",
        "faculty": "Cong nghe thong tin",
        "major": "Cong nghe thong tin",
    },
    {
        "username": "B23DCCN002",
        "password_hash": "B23DCCN002",
        "full_name": "Vo Ngoc Linh",
        "role": UserRole.STUDENT,
        "student_code": "B23DCCN002",
        "email": "b23dccn002@stu.ptit.edu.vn",
        "class_name": "D23CQCN01",
        "faculty": "Cong nghe thong tin",
        "major": "Cong nghe thong tin",
    },
    {
        "username": "B23DCCN003",
        "password_hash": "B23DCCN003",
        "full_name": "Dang Quoc Huy",
        "role": UserRole.STUDENT,
        "student_code": "B23DCCN003",
        "email": "b23dccn003@stu.ptit.edu.vn",
        "class_name": "D23CQCN02",
        "faculty": "Cong nghe thong tin",
        "major": "Cong nghe thong tin",
    },
    {
        "username": "B23DCCN004",
        "password_hash": "B23DCCN004",
        "full_name": "Bui Khanh Vy",
        "role": UserRole.STUDENT,
        "student_code": "B23DCCN004",
        "email": "b23dccn004@stu.ptit.edu.vn",
        "class_name": "D23CQCN02",
        "faculty": "Cong nghe thong tin",
        "major": "Cong nghe thong tin",
    },
]


DEFAULT_SEMESTERS = [
    {"name": "Hoc ky 1 nam hoc 2024-2025", "academic_year": "2024-2025", "start_date": date(2024, 9, 1), "end_date": date(2025, 1, 15), "is_active": False},
    {"name": "Hoc ky 2 nam hoc 2024-2025", "academic_year": "2024-2025", "start_date": date(2025, 2, 1), "end_date": date(2025, 6, 15), "is_active": False},
    {"name": "Hoc ky 1 nam hoc 2025-2026", "academic_year": "2025-2026", "start_date": date(2025, 9, 1), "end_date": date(2026, 1, 15), "is_active": False},
    {"name": "Hoc ky 2 nam hoc 2025-2026", "academic_year": "2025-2026", "start_date": date(2026, 2, 1), "end_date": date(2026, 6, 15), "is_active": True},
]


def seed_default_data(session: Session) -> None:
    if not session.scalar(select(func.count()).select_from(User)):
        session.add_all(User(**user_data) for user_data in DEFAULT_USERS)

    if not session.scalar(select(func.count()).select_from(Semester)):
        session.add_all(Semester(**semester_data) for semester_data in DEFAULT_SEMESTERS)

    if not session.scalar(select(func.count()).select_from(CriterionGroup)):
        for group_order, group_blueprint in enumerate(CRITERION_BLUEPRINT, start=1):
            group = CriterionGroup(
                title=group_blueprint["title"],
                display_order=group_order,
                max_points=group_blueprint["max_points"],
            )
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
