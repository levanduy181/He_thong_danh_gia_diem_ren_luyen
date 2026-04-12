# PTIT Conduct Evaluation

Ứng dụng web quản lý và chấm điểm rèn luyện sinh viên bằng `Reflex + SQLAlchemy + SQLite`.

## Công nghệ

- Python 3
- Reflex `0.8.28.post1`
- SQLAlchemy `2.0.49`
- SQLite
- fpdf2 `2.8.5`

## Chức năng chính

- Đăng nhập, đăng ký tài khoản và phân quyền theo 4 role:
  - `admin`
  - `advisor` (`Cố vấn học tập`)
  - `class_monitor` (`Ban cán sự`)
  - `student` (`Sinh viên`)
- Quản lý học kỳ và timeline đánh giá điểm rèn luyện.
- Khai báo minh chứng.
- Đăng ký và duyệt sự kiện.
- Chấm phiếu điểm rèn luyện theo nhiều bước:
  - sinh viên tự đánh giá
  - ban cán sự duyệt/chỉnh
  - cố vấn xác nhận
- Quản lý tài khoản theo lớp.
- Xuất PDF phiếu điểm rèn luyện.

## Cách chạy

```bash
pip install -r requirements.txt
python main.py
```

App chạy mặc định tại `http://127.0.0.1:3000`.

## Dữ liệu

- Database chính: `data/reflex_student_conduct.db`
- Dữ liệu mẫu hiện tại:
  - `admin / admin123`
  - `CVHT001 / CVHT001` cho lớp `D23CQAT01`
  - `CVHT002 / CVHT002` cho lớp `D23CQAT02`
  - `CVHT003 / CVHT003` cho lớp `D23CQCN01`
  - `CVHT004 / CVHT004` cho lớp `D23CQCN02`
  - mỗi lớp có 2 sinh viên mẫu

Lưu ý: đây là dữ liệu demo cho bài tập, mật khẩu đang được lưu theo kiểu đơn giản để tiện seed/test.

## Cấu trúc thư mục

### Mã nguồn chính

- `main.py`
  - entrypoint chạy Reflex trên Windows.
- `rxconfig.py`
  - cấu hình app Reflex.
- `ptit_reflex/`
  - mã nguồn chính của ứng dụng.

### Trong `ptit_reflex/`

- `config.py`
  - khai báo đường dẫn dữ liệu.
- `db.py`
  - `Base` SQLAlchemy và phần tương thích typing.
- `models.py`
  - ORM model gốc/legacy.
- `data.py`
  - tầng dữ liệu chính: session DB, seed, snapshot, phân quyền, điểm, minh chứng, sự kiện.
- `state.py`
  - `Reflex State`, xử lý event từ UI.
- `views.py`
  - ghép layout và điều hướng tab.
- `ptit_reflex.py`
  - khai báo `rx.App`.
- `pdf_export.py`
  - xuất PDF phiếu điểm rèn luyện.

### UI

- `ptit_reflex/ui/primitives.py`
  - nút, badge, form control, modal, flash banner.
- `ptit_reflex/ui/navigation.py`
  - logo, header, sidebar điều hướng.
- `ptit_reflex/ui/auth.py`
  - màn hình đăng nhập/đăng ký.
- `ptit_reflex/ui/profile_views.py`
  - thẻ thông tin admin, cố vấn, sinh viên.
- `ptit_reflex/ui/student_lists.py`
  - danh sách sinh viên, danh sách duyệt, timeline.
- `ptit_reflex/ui/evidence.py`
  - khai báo và duyệt minh chứng.
- `ptit_reflex/ui/events.py`
  - đăng ký và duyệt sự kiện.
- `ptit_reflex/ui/score.py`
  - phiếu điểm rèn luyện.
- `ptit_reflex/ui/role_management.py`
  - quản lý tài khoản và phân quyền.
- `ptit_reflex/ui/admin_conduct_timeline.py`
  - admin cấu hình mốc thời gian.
- `ptit_reflex/ui/admin_events.py`
  - admin tạo sự kiện.
- `ptit_reflex/ui/styles.py`
  - hằng số màu/style.
- `ptit_reflex/ui/__init__.py`
  - re-export các màn UI để `views.py` dùng.

### Services

- `ptit_reflex/services/seed.py`
  - seed tiêu chí, học kỳ, tài khoản mẫu.
- `ptit_reflex/services/evaluation_service.py`
  - helper thao tác với submission, criteria, event participation.

## Thư mục runtime/generate

- `data/`
  - dữ liệu SQLite và file runtime.
- `.web/`
  - frontend/build generate bởi Reflex.
  - không sửa tay nếu không thật sự cần.
- `.venv/`
  - môi trường Python cục bộ.
- `uploaded_files/`
  - thư mục runtime cho upload.

## Dọn repo

Đã dọn các artefact/runtime không cần thiết trong workspace:

- `__pycache__/`
- `.states/`
- `ptit_reflex/**/__pycache__/`
- `err.log`
- `out.log`
- `data/reflex_student_conduct_readable.md`

Các mục runtime này cũng đã được bổ sung vào `.gitignore` nếu phù hợp.
