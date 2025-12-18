# test_diskon.py
import unittest
from diskon_service import DiskonCalculator

class TestDiskonCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = DiskonCalculator()

    def test_diskon_normal(self):
        hasil = self.calc.hitung_diskon(1000, 10)
        self.assertEqual(hasil, 900)

    def test_diskon_100_persen(self):
        hasil = self.calc.hitung_diskon(1000, 100)
        self.assertEqual(hasil, 0)

    def test_diskon_0_persen(self):
        hasil = self.calc.hitung_diskon(1000, 0)
        self.assertEqual(hasil, 1000)


if __name__ == "__main__":
    unittest.main()
