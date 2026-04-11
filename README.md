# PTIT Conduct Evaluation

Ung dung web danh gia diem ren luyen sinh vien PTIT, trong do frontend, backend va database deu duoc xay dung bang Python.

## Cong nghe

- Reflex
- SQLAlchemy + SQLite

## Chuc nang

- Giao dien sinh vien theo phong cach S-Link chi giu phan `Ren luyen`
- 3 muc con: `Khai bao minh chung`, `Su kien da tham gia`, `Phieu diem ren luyen`
- Du lieu diem ren luyen, hoc ky va su kien lay tu SQLite bang Python
- Seed san du lieu demo cho hoc ky dang mo de hien thi dung giao dien mau
- Ho tro 4 role: `admin`, `co van hoc tap`, `ban can su`, `sinh vien`
- Luong xu ly: sinh vien khai bao -> ban can su duyet -> CVHT xac nhan
- Minh chung co 4 form rieng: thanh tich dac biet, tuyen truyen truong/khoa, cong tac xa hoi, noi tru/ngoai tru
- Su kien co popup chi tiet va minh chung co popup xem/duyet

## Chay du an

```bash
pip install -r requirements.txt
python main.py
```

Mo tai `http://127.0.0.1:3000`

Du lieu Reflex se duoc tao trong file `data/reflex_student_conduct.db`.

## Tai khoan / du lieu demo

App Reflex hien dung bo chon tai khoan demo tren topbar de doi role nhanh, khong can form dang nhap.

- `admin`
- `covan`
- `bancansu`
- `b23dccn001`
- `b23dccn002`
