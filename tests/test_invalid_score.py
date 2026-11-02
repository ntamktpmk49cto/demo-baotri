import unittest
from tinh_diem import diem_trung_binh


class TestInvalidScore(unittest.TestCase):

    def test_score_above_10(self):
        with self.assertRaisesRegex(ValueError, "Diem"):
            diem_trung_binh([8, 11])

    def test_score_below_0(self):
        with self.assertRaisesRegex(ValueError, "Diem"):
            diem_trung_binh([-1, 7])


if __name__ == "__main__":
    unittest.main()