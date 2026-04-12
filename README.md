# PTIT Conduct Evaluation

Ứng dụng web quản lý và chấm điểm rèn luyện sinh viên PTIT, viết bằng `Reflex`, dùng `SQLite` để lưu dữ liệu.

## 1. Dự án này làm gì

Hệ thống hỗ trợ 4 nhóm tài khoản:

- `admin`
- `advisor` (`Cố vấn học tập`)
- `class_monitor` (`Ban cán sự`)
- `student` (`Sinh viên`)

Các chức năng chính:

- Đăng nhập, đăng ký tài khoản.
- Quản lý và phân quyền tài khoản theo lớp.
- Khai báo minh chứng.
- Tạo sự kiện, đăng ký sự kiện, duyệt sự kiện.
- Tự chấm phiếu điểm rèn luyện.
- Ban cán sự duyệt phiếu và minh chứng.
- Cố vấn xác nhận phiếu điểm rèn luyện.
- Quản lý timeline các giai đoạn đánh giá.
- Xuất PDF phiếu điểm rèn luyện.

## 2. Công nghệ sử dụng

- Python
- Reflex `0.8.28.post1`
- SQLAlchemy `2.0.49`
- SQLite
- fpdf2 `2.8.5`
- Node.js / npm để chạy frontend do Reflex sinh ra

## 3. Yêu cầu trước khi chạy

Người mới cần cài:

- `Python 3.12` hoặc `Python 3.13`
- `Node.js LTS` để có `npm`

Khuyến nghị:

- Không dùng `Python 3.14` nếu có thể, vì Reflex hiện đang phát cảnh báo tương thích.

Không cần cài riêng:

- SQLite
- SQLAlchemy
- Reflex global

## 4. Cách chạy trên Windows

### Bước 1: tạo môi trường ảo

```powershell
python -m venv .venv
.venv\Scripts\activate
```

### Bước 2: cài thư viện Python

```powershell
pip install -r requirements.txt
```

### Bước 3: tự tạo thư mục dữ liệu

```powershell
mkdir data
```

Lưu ý:

- Thư mục `data/` phải được tạo thủ công.
- App hiện không tự tạo thư mục này.

### Bước 4: chạy app

```powershell
python main.py
```

Sau khi chạy:

- frontend thường ở `http://127.0.0.1:3000`
- backend thường ở `http://0.0.0.0:8000`

## 5. Dữ liệu và tài khoản mẫu

Database chính nằm tại:

- `data/reflex_student_conduct.db`

Seed hiện tại có các tài khoản chính:

- `admin / admin123`
- `CVHT001 / CVHT001` cho lớp `D23CQAT01`
- `CVHT002 / CVHT002` cho lớp `D23CQAT02`
- `CVHT003 / CVHT003` cho lớp `D23CQCN01`
- `CVHT004 / CVHT004` cho lớp `D23CQCN02`

Ngoài ra:

- Mỗi lớp có 2 sinh viên mẫu.
- Dữ liệu demo được tạo khi hệ thống khởi tạo database.

Lưu ý bảo mật:

- Đây là dữ liệu demo cho bài tập.
- Mật khẩu đang lưu theo kiểu đơn giản để tiện seed/test, không phải cấu hình production.

## 6. Cấu trúc thư mục

### Thư mục và file chính ở root

- `main.py`
  - file khởi chạy app trên Windows.
  - kiểm tra `data/`, thiết lập biến môi trường, rồi gọi `python -m reflex run`.
- `rxconfig.py`
  - cấu hình app Reflex.
- `requirements.txt`
  - danh sách thư viện Python.
- `README.md`
  - tài liệu dự án.
- `data/`
  - thư mục dữ liệu runtime.
- `ptit_reflex/`
  - mã nguồn chính.
- `.web/`
  - frontend/build do Reflex generate.
- `.venv/`
  - môi trường Python cục bộ.
- `uploaded_files/`
  - thư mục runtime cho upload.

### Trong `ptit_reflex/`

- `config.py`
  - khai báo `BASE_DIR`, `DATA_DIR`.
- `db.py`
  - khai báo `Base` của SQLAlchemy.
- `models.py`
  - ORM model gốc/legacy.
- `data.py`
  - tầng dữ liệu chính: seed, query, snapshot, sự kiện, minh chứng, phiếu điểm, phân quyền.
- `state.py`
  - `Reflex State`, xử lý event và state cho UI.
- `views.py`
  - ghép các màn hình theo tab.
- `ptit_reflex.py`
  - khai báo `rx.App`.
- `pdf_export.py`
  - xuất PDF phiếu điểm.

### Trong `ptit_reflex/ui/`

- `primitives.py`
  - component dùng chung: button, badge, form input, modal, flash banner.
- `navigation.py`
  - header, logo, sidebar.
- `auth.py`
  - màn hình đăng nhập/đăng ký.
- `profile_views.py`
  - giao diện thông tin admin, cố vấn, sinh viên.
- `student_lists.py`
  - danh sách sinh viên, danh sách duyệt, timeline.
- `score.py`
  - phiếu điểm rèn luyện.
- `evidence.py`
  - khai báo và duyệt minh chứng.
- `events.py`
  - đăng ký và duyệt sự kiện.
- `role_management.py`
  - quản lý tài khoản, phân quyền, xóa tài khoản.
- `admin_conduct_timeline.py`
  - cấu hình mốc thời gian đánh giá.
- `admin_events.py`
  - tạo sự kiện.
- `styles.py`
  - hằng số màu và style.
- `__init__.py`
  - gom export cho UI.

### Trong `ptit_reflex/services/`

- `seed.py`
  - seed tiêu chí, học kỳ, tài khoản mẫu.
- `evaluation_service.py`
  - helper thao tác với submission, criteria và event participation.

## 7. File nào nên sửa, file nào không nên sửa

Nên sửa khi làm tính năng:

- `ptit_reflex/data.py`
- `ptit_reflex/state.py`
- `ptit_reflex/views.py`
- `ptit_reflex/ui/*.py`

Không nên sửa tay trừ khi bạn biết rõ mình đang làm gì:

- `.web/`
  - đây là mã generate bởi Reflex.
- `.venv/`
  - đây là môi trường cài thư viện.

## 8. Lỗi thường gặp

### Không tìm thấy thư mục `data`

Nguyên nhân:

- bạn chưa tự tạo `data/`

Cách xử lý:

```powershell
mkdir data
python main.py
```

### Không tìm thấy `npm`

Nguyên nhân:

- chưa cài `Node.js`

Cách xử lý:

- cài `Node.js LTS`
- mở terminal mới
- chạy lại `python main.py`

### Cảnh báo Pydantic V1 / Python 3.14

Đây là warning từ Reflex, không phải lỗi logic của dự án. Nếu muốn ổn định hơn, dùng:

- Python `3.12`
- hoặc Python `3.13`

## 9. Lưu ý khi reset dữ liệu

Nếu muốn reset app:

- xóa file database trong `data/`
- giữ nguyên thư mục `data/`
- chạy lại `python main.py`

Hệ thống sẽ khởi tạo lại dữ liệu demo nếu cần.
