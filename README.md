# PTIT Conduct Evaluation

Ứng dụng web quản lý điểm rèn luyện sinh viên PTIT, viết bằng `Reflex`, lưu dữ liệu bằng `SQLite`.

## Yêu cầu

- `Git`
- `Python 3.12` hoặc `Python 3.13`
- `Node.js LTS`

Không nên dùng `Python 3.14` vì `Reflex` vẫn còn cảnh báo tương thích.

## Clone và chạy nhanh

```powershell
git clone <repo-url>
cd python--btl
powershell -ExecutionPolicy Bypass -File .\setup_and_run.ps1
```

Script `setup_and_run.ps1` sẽ tự:

- tạo `.venv`
- cài `requirements.txt`
- tạo thư mục `data`
- compile app để sinh `.web`
- cài `tslib` trong `.web` nếu thiếu
- chạy ứng dụng

Sau khi chạy, mở `http://localhost:3000`.

## Chạy thủ công

```powershell
py -3.13 -m venv .venv
.\.venv\Scripts\python.exe -m pip install --upgrade pip
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
mkdir data
.\.venv\Scripts\python.exe main.py
```

Nếu máy không có `py`, có thể thay bằng `python`.

## Tài khoản mẫu

- `admin / admin123`
- `CVHT001 / CVHT001` lớp `D23CQAT001`
- `CVHT002 / CVHT002` lớp `D23CQAT002`
- `CVHT003 / CVHT003` lớp `D23CQCN001`
- `CVHT004 / CVHT004` lớp `D23CQCN002`

Mỗi lớp có `3` tài khoản phía sinh viên, trong đó `1` tài khoản là ban cán sự:

- `D23CQAT001`: `B23DCAT001`, `B23DCAT002`, `B23DCAT003`
- `D23CQAT002`: `B23DCAT004`, `B23DCAT005`, `B23DCAT006`
- `D23CQCN001`: `B23DCCN001`, `B23DCCN002`, `B23DCCN003`
- `D23CQCN002`: `B23DCCN004`, `B23DCCN005`, `B23DCCN006`

Mật khẩu của các tài khoản sinh viên và ban cán sự đều bằng đúng mã sinh viên.

## Dữ liệu seed sẵn

- `48` phiếu điểm rèn luyện lịch sử
- `6` sự kiện mẫu

Các sự kiện mặc định:

- `Seminar An toàn hệ thống 2026`
- `Tọa đàm nghiên cứu khoa học sinh viên`
- `Sinh hoạt lớp đầu tháng 4`
- `Sinh hoạt lớp giữa học kỳ`
- `Hội thảo kỹ năng CV và phỏng vấn`
- `Ngày hội việc làm PTIT 2026`

## Reset dữ liệu

```powershell
Remove-Item data\reflex_student_conduct.db -Force
.\.venv\Scripts\python.exe main.py
```

Nếu muốn xóa luôn file upload runtime:

```powershell
Remove-Item uploaded_files -Recurse -Force
```

## Lỗi thường gặp

### Thiếu thư mục `data`

```powershell
mkdir data
.\.venv\Scripts\python.exe main.py
```

### Thiếu `npm`

Cài `Node.js LTS`, mở terminal mới rồi chạy lại app.

### Thiếu `fpdf2`

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

### Lỗi `Cannot find module 'tslib'`

```powershell
Remove-Item .web -Recurse -Force
.\.venv\Scripts\python.exe main.py
```

Nếu lỗi vẫn còn, dừng app rồi chạy:

```powershell
cd .web
npm install tslib --no-save --legacy-peer-deps
cd ..
.\.venv\Scripts\python.exe main.py
```

### PowerShell chặn `Activate.ps1`

Không cần activate `.venv`. Chạy trực tiếp:

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe main.py
```

## Cấu trúc chính

- `main.py`: launcher chạy `Reflex`
- `setup_and_run.ps1`: script cài và chạy một lệnh cho Windows
- `requirements.txt`: thư viện Python
- `rxconfig.py`: cấu hình `Reflex`
- `ptit_reflex/data.py`: seed, query, phân quyền, phiếu điểm, minh chứng, sự kiện
- `ptit_reflex/state.py`: state và event handler
- `ptit_reflex/views.py`: ghép giao diện theo tab
- `ptit_reflex/pdf_export.py`: xuất PDF
- `ptit_reflex/ui/`: các thành phần giao diện
- `ptit_reflex/services/`: helper nghiệp vụ

Không nên sửa tay:

- `.web/`
- `.venv/`
- `uploaded_files/`
