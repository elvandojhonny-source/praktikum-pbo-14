# Praktikum 14 – Debugging dan Unit Testing

## Mata Kuliah

Pemrograman Berorientasi Objek – Praktikum

---

## Identitas Mahasiswa

* **Nama**  : Elvando Agustio Jhonny
* **NIM**   : 2411102441056
* **Kelas** : C

---

## Deskripsi Praktikum

Praktikum 14 berfokus pada proses **debugging program Python menggunakan modul `pdb`** serta **verifikasi kebenaran logika program melalui unit testing**. Studi kasus yang digunakan adalah perhitungan harga setelah diskon pada sebuah layanan sederhana.

---

## Tujuan Praktikum

Tujuan dari praktikum ini adalah:

1. Memahami cara menemukan bug menggunakan debugger Python (`pdb`).
2. Mengidentifikasi kesalahan logika dalam perhitungan program.
3. Memperbaiki bug berdasarkan hasil debugging.
4. Memastikan kebenaran program menggunakan unit testing.
5. Melatih penggunaan test case termasuk boundary dan floating-point testing.

---

## Studi Kasus

Program `DiskonCalculator` digunakan untuk menghitung harga akhir setelah diskon berdasarkan harga awal dan persentase diskon. Pada tahap awal, program sengaja diberikan bug agar dapat dianalisis menggunakan debugger.

---

## Proses Debugging

Debugging dilakukan dengan menambahkan `pdb.set_trace()` pada method `hitung_diskon()`.

Langkah debugging:

1. Menjalankan program dan menghentikan eksekusi di breakpoint.
2. Melakukan inspeksi variabel menggunakan perintah `p`.
3. Menemukan bahwa nilai diskon menjadi terlalu besar.

Hasil debugging menunjukkan bahwa perhitungan diskon salah karena persentase diskon langsung dikalikan dengan harga awal tanpa dibagi 100.

Screenshot proses debugging terlampir pada laporan PDF.

---

## Perbaikan Bug

Bug diperbaiki dengan mengubah rumus perhitungan diskon menjadi:

```
jumlah_diskon = harga_awal * (persentase_diskon / 100)
```

Setelah perbaikan, debugger dinonaktifkan dan program menghasilkan output yang benar.

---

## Unit Testing

Unit testing dilakukan menggunakan modul `unittest` dengan beberapa skenario:

1. Diskon normal (10%)
2. Diskon 0%
3. Diskon 100%
4. Diskon dengan nilai desimal
5. Harga awal bernilai nol

Unit test dasar dan lanjutan dijalankan dan seluruh test berhasil (status OK).

Screenshot hasil unit testing terlampir pada laporan PDF.

---

## Struktur File Proyek

```
Praktikum 14/
├── diskon_service.py
├── test_diskon.py
├── test_diskon_advanced.py
└── README.md
```

---

## Kesimpulan

Melalui praktikum ini, proses debugging menggunakan `pdb` membantu menemukan kesalahan logika program secara sistematis. Unit testing memastikan bahwa program berjalan dengan benar pada berbagai skenario. Kombinasi debugging dan unit testing terbukti efektif dalam meningkatkan kualitas dan keandalan perangkat lunak.

---

## Cara Menjalankan Program

1. Jalankan program utama:

```
python diskon_service.py
```

2. Jalankan unit test:

```
python -m unittest test_diskon.py
python -m unittest test_diskon_advanced.py
```

---

**URL Repository GitHub**: (diisi setelah upload)
