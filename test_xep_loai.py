from tinh_diem import xep_loai_hoc_luc

test_cases = [
    (9.0, "Giỏi"),
    (8.5, "Giỏi"),
    (8.0, "Khá"),
    (7.0, "Khá"),
    (6.0, "Trung bình"),
    (5.0, "Trung bình"),
    (4.9, "Yếu")
]

print("KET QUA KIEM THU CHUC NANG XEP LOAI V1")

passed = 0
failed = 0

for i, (diem, expected) in enumerate(test_cases, 1):
    actual = xep_loai_hoc_luc(diem)

    if actual == expected:
        print(f"TC{i:02d}: PASS | Diem: {diem} | Ket qua: {actual}")
        passed += 1
    else:
        print(f"TC{i:02d}: FAIL | Diem: {diem} | Mong doi: {expected} | Thuc te: {actual}")
        failed += 1

print(f"\nTong so test: {len(test_cases)}")
print(f"PASS: {passed}")
print(f"FAIL: {failed}")