# Latihan 4: Menghitung Bilangan Genap
# Input: Bilangan bulat positif n
# Proses: Perulangan for dari 1 ke n dan seleksi if untuk cek bilangan genap
# Output: Banyaknya bilangan genap

n = int(input("n: "))
jumlah_genap = 0
for i in range(1, n + 1):
    if i % 2 == 0:
        jumlah_genap += 1

print(f"Banyak bilangan genap = {jumlah_genap}")