def diem_trung_binh(ds):
    return round(sum(ds) / len(ds), 2)


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