# Latihan 1: Tabel Perkalian
# Input: Bilangan bulat n
# Proses: Perulangan for dari 1 sampai 10
# Output: Tabel perkalian n x 1 hingga n x 10

n = int(input("Bilangan: "))
for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")