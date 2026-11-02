def diem_trung_binh(ds):
    if not ds:
        raise ValueError("Danh sach diem khong duoc rong")

    if any(d < 0 or d > 10 for d in ds):
        raise ValueError(
            "Diem khong hop le: phai tu 0 den 10"
        )

    return sum(ds) / len(ds)


def xep_loai_hoc_luc(diem):
    if diem >= 8.5:
        return "Giỏi"
    elif diem >= 6.0:
        return "Khá"
    elif diem >= 5.0:
        return "Trung bình"
    else:
        return "Yếu"

diem = diem_trung_binh([7, 8, 8])
print(diem)
print("Xep loai:", xep_loai_hoc_luc(diem))