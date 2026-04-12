# PTIT Conduct Evaluation

Ứng dụng web quản lý điểm rèn luyện sinh viên PTIT, viết bằng `Reflex`, lưu dữ liệu bằng `SQLite`.

README này viết cho trường hợp người dùng chưa cài gì, chỉ cần clone repo rồi làm lần lượt để chạy được trên Windows.

## 1. Cần cài gì trước

Trước khi chạy dự án, máy cần có:

- `Git`
- `Python 3.12` hoặc `Python 3.13`
- `Node.js LTS` để có `npm`

Khuyến nghị:

- dùng `Python 3.13`
- không dùng `Python 3.14` nếu có thể, vì `Reflex` hiện vẫn cảnh báo tương thích

Không cần cài riêng:

- `SQLite`
- `Reflex` global
- `SQLAlchemy` global

## 2. Clone code

Mở `PowerShell`, chạy:

```powershell
git clone <repo-url>
cd python--btl
```

Thay `<repo-url>` bằng link GitHub của repo của bạn.

## 3. Tạo môi trường Python

Khuyến nghị dùng `py` trên Windows:

```powershell
py -3.13 -m venv .venv
```

Nếu máy bạn cài `Python 3.12` thì dùng:

```powershell
py -3.12 -m venv .venv
```

Nếu lệnh `py` không có, có thể dùng:

```powershell
python -m venv .venv
```

## 4. Cài thư viện Python

Không cần activate môi trường ảo, có thể chạy trực tiếp như sau:

```powershell
.\.venv\Scripts\python.exe -m pip install --upgrade pip
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

File [requirements.txt](D:/PTIT/ki_2_nam_3/python/python--btl/requirements.txt:1) hiện gồm:

- `reflex==0.8.28.post1`
- `SQLAlchemy==2.0.49`
- `fpdf2==2.8.5`

## 5. Tạo thư mục dữ liệu

Project này yêu cầu tự tạo thư mục `data` trước khi chạy:

```powershell
mkdir data
```

Nếu không tạo, [main.py](D:/PTIT/ki_2_nam_3/python/python--btl/main.py:1) sẽ dừng và báo lỗi.

## 6. Chạy ứng dụng

Chạy bằng:

```powershell
.\.venv\Scripts\python.exe main.py
```

Hoặc nếu bạn đã activate `.venv` thì có thể dùng:

```powershell
python main.py
```

Lần chạy đầu:

- `Reflex` sẽ compile giao diện
- thư mục `.web/` sẽ được sinh ra tự động
- database `data/reflex_student_conduct.db` sẽ được tạo tự động

Khi chạy thành công, thường sẽ thấy:

- frontend: `http://localhost:3000`
- backend: `http://0.0.0.0:8000` hoặc `http://0.0.0.0:8001`

Hãy mở trình duyệt tại:

```text
http://localhost:3000
```

## 7. Dữ liệu mẫu hiện tại

Sau khi DB được tạo mới, hệ thống sẽ seed sẵn:

- `1` admin
- `4` cố vấn học tập
- `4` ban cán sự
- `8` sinh viên thường
- `48` phiếu điểm rèn luyện lịch sử
- `6` sự kiện mẫu

### Tài khoản admin

- `admin / admin123`

### Tài khoản cố vấn học tập

- `CVHT001 / CVHT001` cho lớp `D23CQAT001`
- `CVHT002 / CVHT002` cho lớp `D23CQAT002`
- `CVHT003 / CVHT003` cho lớp `D23CQCN001`
- `CVHT004 / CVHT004` cho lớp `D23CQCN002`

### Tài khoản sinh viên và ban cán sự

Mật khẩu của các tài khoản này đều bằng đúng mã sinh viên.

#### Lớp `D23CQAT001`

- `B23DCAT001 / B23DCAT001` `ban cán sự`
- `B23DCAT002 / B23DCAT002`
- `B23DCAT003 / B23DCAT003`

#### Lớp `D23CQAT002`

- `B23DCAT004 / B23DCAT004` `ban cán sự`
- `B23DCAT005 / B23DCAT005`
- `B23DCAT006 / B23DCAT006`

#### Lớp `D23CQCN001`

- `B23DCCN001 / B23DCCN001` `ban cán sự`
- `B23DCCN002 / B23DCCN002`
- `B23DCCN003 / B23DCCN003`

#### Lớp `D23CQCN002`

- `B23DCCN004 / B23DCCN004` `ban cán sự`
- `B23DCCN005 / B23DCCN005`
- `B23DCCN006 / B23DCCN006`

## 8. Sự kiện mẫu có sẵn

DB mới hiện được seed sẵn các sự kiện:

- `Seminar An toàn hệ thống 2026`
- `Tọa đàm nghiên cứu khoa học sinh viên`
- `Sinh hoạt lớp đầu tháng 4`
- `Sinh hoạt lớp giữa học kỳ`
- `Hội thảo kỹ năng CV và phỏng vấn`
- `Ngày hội việc làm PTIT 2026`

## 9. Cách reset dữ liệu

Nếu muốn xóa sạch dữ liệu và tạo lại từ seed:

```powershell
Remove-Item data\reflex_student_conduct.db -Force
.\.venv\Scripts\python.exe main.py
```

Nếu muốn xóa luôn file upload runtime:

```powershell
Remove-Item uploaded_files\evidence -Recurse -Force
```

## 10. Lỗi thường gặp

### Lỗi thiếu `data`

Thông báo thường gặp:

```text
Khong tim thay thu muc data. Hay tu tao thu muc 'data' truoc khi chay ung dung.
```

Cách sửa:

```powershell
mkdir data
.\.venv\Scripts\python.exe main.py
```

### Lỗi thiếu `npm`

Thông báo thường gặp:

```text
Khong tim thay npm. Hay cai Node.js LTS tu https://nodejs.org
```

Cách sửa:

- cài `Node.js LTS`
- đóng PowerShell cũ
- mở PowerShell mới
- chạy lại app

### Lỗi thiếu thư viện PDF `fpdf2`

Thông báo thường gặp:

```text
Khong tim thay thu vien 'fpdf2'
```

Hoặc trong app khi tải PDF sẽ báo thiếu thư viện tạo PDF.

Cách sửa:

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

Sau đó tắt app đang chạy và mở lại:

```powershell
.\.venv\Scripts\python.exe main.py
```

### Cảnh báo Pydantic / Python 3.14

Nếu thấy cảnh báo kiểu:

```text
Core Pydantic V1 functionality isn't compatible with Python 3.14 or greater.
```

thì đó là cảnh báo từ `Reflex`, không phải lỗi logic của dự án.

Nếu muốn chạy ổn định hơn, dùng:

- `Python 3.12`
- hoặc `Python 3.13`

### PowerShell không cho activate `.venv`

Nếu bạn bị chặn `Activate.ps1`, không cần sửa gì cả. Chỉ cần chạy trực tiếp bằng Python trong `.venv`:

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe main.py
```

## 11. Cấu trúc thư mục chính

### Root

- [main.py](D:/PTIT/ki_2_nam_3/python/python--btl/main.py:1): file khởi chạy app
- [rxconfig.py](D:/PTIT/ki_2_nam_3/python/python--btl/rxconfig.py:1): cấu hình `Reflex`
- [requirements.txt](D:/PTIT/ki_2_nam_3/python/python--btl/requirements.txt:1): thư viện Python
- `data/`: nơi lưu DB
- `uploaded_files/`: nơi lưu file upload runtime
- `.web/`: frontend do `Reflex` generate
- `ptit_reflex/`: mã nguồn chính

### Trong `ptit_reflex/`

- [data.py](D:/PTIT/ki_2_nam_3/python/python--btl/ptit_reflex/data.py:1): seed, query, phân quyền, phiếu điểm, minh chứng, sự kiện
- [state.py](D:/PTIT/ki_2_nam_3/python/python--btl/ptit_reflex/state.py:1): state và event handler của app
- [views.py](D:/PTIT/ki_2_nam_3/python/python--btl/ptit_reflex/views.py:1): ghép giao diện theo tab
- [pdf_export.py](D:/PTIT/ki_2_nam_3/python/python--btl/ptit_reflex/pdf_export.py:1): xuất PDF
- [models.py](D:/PTIT/ki_2_nam_3/python/python--btl/ptit_reflex/models.py:1): model ORM gốc
- `ui/`: các thành phần giao diện
- `services/`: helper seed và evaluation

## 12. Nên sửa file nào

Khi làm tính năng mới, thường sẽ sửa:

- [ptit_reflex/data.py](D:/PTIT/ki_2_nam_3/python/python--btl/ptit_reflex/data.py:1)
- [ptit_reflex/state.py](D:/PTIT/ki_2_nam_3/python/python--btl/ptit_reflex/state.py:1)
- các file trong [ptit_reflex/ui](D:/PTIT/ki_2_nam_3/python/python--btl/ptit_reflex/ui)

Không nên sửa tay nếu không thực sự cần:

- `.web/`
- `.venv/`
- `uploaded_files/`

## 13. Quy trình ngắn gọn nhất

Nếu muốn cách chạy ngắn nhất cho máy mới:

```powershell
git clone <repo-url>
cd python--btl
py -3.13 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
mkdir data
.\.venv\Scripts\python.exe main.py
```

Sau đó mở:

```text
http://localhost:3000
```
