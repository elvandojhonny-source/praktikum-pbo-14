# diskon_service.py
import pdb

class DiskonCalculator:
    def hitung_diskon(self, harga_awal, persentase_diskon):
        """
        Menghitung harga akhir setelah diskon
        BUG: Perhitungan diskon salah
        """
        # pdb.set_trace()  # breakpoint untuk debugging

        jumlah_diskon = harga_awal * (persentase_diskon / 100) # ❌ BUG (harusnya / 100)
        harga_akhir = harga_awal - jumlah_diskon

        return harga_akhir


if __name__ == "__main__":
    calc = DiskonCalculator()
    hasil = calc.hitung_diskon(1000, 10)
    print("Harga akhir:", hasil)
