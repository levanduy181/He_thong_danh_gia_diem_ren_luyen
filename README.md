# PTIT Conduct Evaluation

Ứng dụng web đánh giá điểm rèn luyện sinh viên PTIT, trong đó frontend, backend và dữ liệu đều chạy bằng Python với Reflex.

## Công nghệ

- Reflex
- SQLAlchemy + SQLite
- fpdf2

## Chức năng chính

- Đăng nhập theo vai trò `admin`, `cố vấn học tập`, `ban cán sự`, `sinh viên`
- Sinh viên khai báo minh chứng, theo dõi sự kiện đã tham gia và tự điền phiếu điểm rèn luyện
- Ban cán sự duyệt minh chứng của lớp và duyệt phiếu điểm rèn luyện của sinh viên
- Cố vấn học tập xác nhận phiếu điểm rèn luyện
- Có mốc thời gian đánh giá theo từng học kỳ
- Có API demo: `/api/health`, `/api/semesters`, `/api/dashboard`, `/api/submissions/{id}`

## Chạy dự án

```bash
pip install -r requirements.txt
python main.py
```

Mở tại `http://127.0.0.1:3000`

## Dữ liệu

- CSDL demo được tạo tại `data/reflex_student_conduct.db`
- Tệp upload được phục vụ qua route `/_upload/...`

## Tài khoản demo

- `admin / admin123`
- `covan / covan123`
- `bancansu / bcs123`
- `b23dccn001 / student123`
- `b23dccn002 / student123`
