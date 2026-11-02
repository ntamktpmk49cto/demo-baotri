import unittest
from tinh_diem import diem_trung_binh

class TestEmptyScore(unittest.TestCase):

    def test_empty_list(self):
        with self.assertRaisesRegex(
            ValueError,
            "Danh sach diem"
        ):
            diem_trung_binh([])

if __name__ == "__main__":
    unittest.main()