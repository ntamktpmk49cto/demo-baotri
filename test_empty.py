
from tinh_diem import diem_trung_binh

try:
    diem_trung_binh([])
except ValueError:
    print("PASS: Da xu ly danh sach diem rong")
except Exception as e:
    print(f"FAIL: Loi khong mong doi: {type(e).__name__}")
else:
    print("FAIL: Ham chap nhan danh sach rong ma khong bao loi")
