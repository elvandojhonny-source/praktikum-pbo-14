# test_diskon_advanced.py
import unittest
from diskon_service import DiskonCalculator

class TestDiskonLanjut(unittest.TestCase):

    def setUp(self):
        self.calc = DiskonCalculator()

    def test_diskon_float(self):
        hasil = self.calc.hitung_diskon(999, 33)
        self.assertAlmostEqual(hasil, 669.33, places=2)

    def test_harga_nol(self):
        hasil = self.calc.hitung_diskon(0, 50)
        self.assertEqual(hasil, 0)


if __name__ == "__main__":
    unittest.main()
