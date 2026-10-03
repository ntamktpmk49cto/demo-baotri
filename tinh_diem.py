def diem_trung_binh(ds):
    return sum(ds) / (len(ds))   # loi co y: chia sai


print("Diem trung binh =", diem_trung_binh([8, 7, 9]))

def diem_trung_binh(ds):
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

diem = diem_trung_binh([8, 7, 9])
print(diem)
print(xep_loai_hoc_luc(diem))