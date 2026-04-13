# PTIT Conduct Evaluation

Hệ thống đánh giá điểm rèn luyện dành cho sinh viên PTIT.

Ứng dụng có 4 vai trò chính:
- `Sinh viên`: khai báo điểm rèn luyện, minh chứng, đăng ký sự kiện
- `Ban cán sự`: phê duyệt minh chứng, sự kiện, phiếu điểm của lớp
- `Cố vấn học tập`: xem và xác nhận phiếu điểm rèn luyện
- `Admin`: quản lý tài khoản, mốc thời gian và sự kiện

Hệ thống được viết bằng `Reflex`, lưu dữ liệu bằng `SQLite`.

## Deploy lên Reflex Cloud

Yêu cầu:
- `Python 3.12` hoặc `Python 3.13`

Chạy các lệnh sau:

```powershell
git clone https://github.com/levanduy181/He_thong_danh_gia_diem_ren_luyen.git
cd He_thong_danh_gia_diem_ren_luyen
py -3.12 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m reflex login
.\.venv\Scripts\python.exe -m reflex deploy --config cloud.yml
```

Sau khi deploy xong, Reflex Cloud sẽ trả về đường dẫn public để mở trên internet.

## Cấu hình deploy

Repo đã có sẵn file `cloud.yml`:
- app name: `he-thong-danh-gia-diem-ren-luyen`
- region: `sin` (Singapore)
- vm type: `c1m1`

Nếu bạn muốn đổi tên app hoặc đổi region, sửa trực tiếp file `cloud.yml`.

## Tài khoản mẫu

- `admin / admin123`
- `CVHT001 / CVHT001`
- `CVHT002 / CVHT002`
- `B23DCAT001 / B23DCAT001`
- `B23DCAT002 / B23DCAT002`

Tài khoản sinh viên và ban cán sự dùng mật khẩu đúng bằng mã sinh viên.

## Lưu ý quan trọng

- Deploy kiểu này phù hợp để demo nhanh trên internet.
- Theo tài liệu chính thức của Reflex, nếu dùng `include_db` với SQLite local thì dữ liệu đó không persistent và có thể mất khi app restart. Hiện file `cloud.yml` không mang DB local lên cloud.
- Theo tài liệu upload của Reflex, thư mục upload trên Reflex hosting không persistent và sẽ bị xóa khi redeploy. Nếu muốn giữ file minh chứng lâu dài, nên chuyển sang dịch vụ lưu file ngoài như S3.

## Tài liệu chính thức

- [Reflex Cloud Quick Start](https://reflex.dev/docs/hosting/deploy-quick-start/)
- [reflex deploy](https://reflex.dev/docs/hosting/cli/deploy/)
- [cloud.yml config](https://reflex.dev/docs/hosting/config-file/)
- [upload persistence trên Reflex hosting](https://reflex.dev/docs/library/forms/upload/)
