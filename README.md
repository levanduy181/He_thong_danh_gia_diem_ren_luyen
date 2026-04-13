# PTIT Conduct Evaluation

Ứng dụng web quản lý điểm rèn luyện sinh viên PTIT, viết bằng `Reflex`, lưu dữ liệu bằng `SQLite`.

## Yêu cầu

- `Docker Desktop`

Chỉ cần cài Docker rồi chạy:

```powershell
git clone https://github.com/levanduy181/python.git
cd python
docker compose up --build
```

Sau khi container lên xong, mở `http://localhost:3000`.

## Chạy bằng Docker

```powershell
git clone https://github.com/levanduy181/python.git
cd python
docker compose up --build
```

Khi cần dừng:

```powershell
docker compose down
```

Docker sẽ tự giữ dữ liệu trong:

- `./data`
- `./uploaded_files`

Lần chạy Docker đầu tiên có thể chậm hơn một chút vì container sẽ tự khởi tạo `.web` và cài `tslib`.

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
docker compose down
Remove-Item data\reflex_student_conduct.db -Force
docker compose up --build
```

Nếu muốn xóa luôn file upload runtime:

```powershell
docker compose down
Remove-Item uploaded_files -Recurse -Force
docker compose up --build
```

## Lỗi thường gặp

### Docker build lỗi

Nếu build bị lỗi do cache hoặc package frontend, chạy lại:

```powershell
docker compose build --no-cache
docker compose up
```

### Docker Desktop chưa chạy

Mở `Docker Desktop`, chờ Docker khởi động xong rồi chạy lại:

```powershell
docker compose up --build
```

### Cổng `3000` hoặc `8000` đang bị dùng

```powershell
docker compose down
```

Sau đó tắt ứng dụng khác đang chiếm cổng rồi chạy lại:

```powershell
docker compose up --build
```

## Cấu trúc chính

- `Dockerfile`: image chạy app bằng Docker
- `docker-compose.yml`: chạy app bằng `docker compose`
- `docker-entrypoint.sh`: khởi tạo `.web`, cài `tslib` nếu thiếu rồi chạy app
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
- `uploaded_files/`
