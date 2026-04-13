# PTIT Conduct Evaluation

Hệ thống đánh giá điểm rèn luyện dành cho sinh viên PTIT.

Ứng dụng hỗ trợ các vai trò:
- `Sinh viên`: khai báo điểm rèn luyện, minh chứng, đăng ký sự kiện
- `Ban cán sự`: phê duyệt minh chứng, sự kiện, phiếu điểm của lớp
- `Cố vấn học tập`: xem và xác nhận phiếu điểm rèn luyện
- `Admin`: quản lý tài khoản, cấu hình mốc thời gian, tạo sự kiện

Hệ thống được viết bằng `Reflex`, lưu dữ liệu bằng `SQLite` và chạy bằng `Docker`.

## Cách chạy

Yêu cầu:
- `Docker Desktop`

Chạy ứng dụng:

```powershell
git clone https://github.com/levanduy181/He_thong_danh_gia_diem_ren_luyen.git
cd He_thong_danh_gia_diem_ren_luyen
docker compose up --build
```

Sau khi chạy xong, mở:

```text
http://localhost:3000
```

Dừng ứng dụng:

```powershell
docker compose down
```

## Tài khoản mẫu

- `admin / admin123`
- `CVHT001 / CVHT001`
- `CVHT002 / CVHT002`
- `B23DCAT001 / B23DCAT001`
- `B23DCAT002 / B23DCAT002`

Tài khoản sinh viên và ban cán sự dùng mật khẩu đúng bằng mã sinh viên.

## Dữ liệu có sẵn

- `4` lớp mẫu
- `12` tài khoản phía sinh viên
- `48` phiếu điểm rèn luyện lịch sử
- `6` sự kiện mẫu

## Lưu ý

- Lần chạy đầu có thể chậm hơn vì Docker cần build image và khởi tạo frontend.
- Nếu Docker chưa mở, hãy mở `Docker Desktop` trước rồi chạy lại.
- Nếu cổng `3000` đang bận, hãy tắt ứng dụng đang dùng cổng đó rồi chạy lại.
