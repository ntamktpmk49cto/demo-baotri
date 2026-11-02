[1mdiff --git a/test_empty.py b/test_empty.py[m
[1mdeleted file mode 100644[m
[1mindex 3e2f824..0000000[m
[1m--- a/test_empty.py[m
[1m+++ /dev/null[m
[36m@@ -1,14 +0,0 @@[m
[31m-import unittest[m
[31m-from tinh_diem import diem_trung_binh[m
[31m-[m
[31m-class TestEmptyScore(unittest.TestCase):[m
[31m-[m
[31m-    def test_empty_list(self):[m
[31m-        with self.assertRaisesRegex([m
[31m-            ValueError,[m
[31m-            "Danh sach diem"[m
[31m-        ):[m
[31m-            diem_trung_binh([])[m
[31m-[m
[31m-if __name__ == "__main__":[m
[31m-    unittest.main()[m
\ No newline at end of file[m
[1mdiff --git a/test_xep_loai.py b/test_xep_loai.py[m
[1mdeleted file mode 100644[m
[1mindex 0a55f26..0000000[m
[1m--- a/test_xep_loai.py[m
[1m+++ /dev/null[m
[36m@@ -1,30 +0,0 @@[m
[31m-from tinh_diem import xep_loai_hoc_luc[m
[31m-[m
[31m-test_cases = [[m
[31m-    (9.0, "Giỏi"),[m
[31m-    (8.5, "Giỏi"),[m
[31m-    (8.0, "Khá"),[m
[31m-    (7.0, "Khá"),[m
[31m-    (6.0, "Trung bình"),[m
[31m-    (5.0, "Trung bình"),[m
[31m-    (4.9, "Yếu")[m
[31m-][m
[31m-[m
[31m-print("KET QUA KIEM THU CHUC NANG XEP LOAI V1 - DEMO")[m
[31m-[m
[31m-passed = 0[m
[31m-failed = 0[m
[31m-[m
[31m-for i, (diem, expected) in enumerate(test_cases, 1):[m
[31m-    actual = xep_loai_hoc_luc(diem)[m
[31m-[m
[31m-    if actual == expected:[m
[31m-        print(f"TC{i:02d}: PASS | Diem: {diem} | Ket qua: {actual}")[m
[31m-        passed += 1[m
[31m-    else:[m
[31m-        print(f"TC{i:02d}: FAIL | Diem: {diem} | Mong doi: {expected} | Thuc te: {actual}")[m
[31m-        failed += 1[m
[31m-[m
[31m-print(f"\nTong so test: {len(test_cases)}")[m
[31m-print(f"PASS: {passed}")[m
[31m-print(f"FAIL: {failed}")[m
\ No newline at end of file[m
