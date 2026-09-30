# Pertemuan 05 Perulangan Python

Nama: [Jihan Fithriyyah]
NIM: [2225250155]
Kelas: [3A]

## Tujuan
Menggunakan for dan while untuk menyelesaikan masalah iteratif.

## Cara Menjalankan
python3 kuis/kuis2_deret_aritmetika.py

## Algoritma Kuis 2
1. Membaca input nilai suku pertama (a) dan beda (d) sebagai bilangan desimal (float).
2. Membaca input banyak suku (n) sebagai bilangan bulat (integer).
3. Memvalidasi nilai n menggunakan perulangan while. Jika n <= 0, tampilkan pesan error dan minta input ulang sampai n bernilai positif.
4. Menginisialisasi variabel total = 0 untuk menampung jumlah deret.
5. Menggunakan perulangan for dari i = 0 sampai n - 1 untuk menghitung nilai tiap suku dengan rumus `suku = a + i * d`.
6. Menambahkan nilai suku ke variabel total dan mencetak nilai suku tersebut.
7. Menampilkan hasil akhir akumulasi total dengan format 2 angka di belakang koma.

## Hasil Pengujian
| Test Case | Input (a, d, n) | Keluaran yang Diharapkan | Hasil Aktual | Status |
| :--- | :--- | :--- | :--- | :--- |
| Test 1 | a=2, d=3, n=5 | Suku: 2, 5, 8, 11, 14; Jumlah = 40.00 | Sesuai | Lulus |
| Test 2 | a=10, d=-2, n=4 | Suku: 10, 8, 6, 4; Jumlah = 28.00 | Sesuai | Lulus |
| Test 3 | a=1.5, d=0.5, n=3 | Suku: 1.5, 2.0, 2.5; Jumlah = 6.00 | Sesuai | Lulus |

## Refleksi
Saat membuat perulangan validasi input menggunakan while, variabel kontrol harus dibaca ulang di dalam badan perulangan agar tidak terjadi infinite loop. Selain itu, inisialisasi variabel total = 0 harus diletakkan di luar loop agar nilainya tidak terus ter-reset pada setiap iterasi.
