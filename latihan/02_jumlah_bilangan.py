# Latihan 2: Jumlah Bilangan 1 Sampai n
# Input: Bilangan bulat positif n
# Proses: Akumulasi penjumlahan dari 1 hingga n menggunakan for
# Output: Total hasil penjumlahan

n = int(input("n: "))
total = 0
for i in range(1, n + 1):
    total += i

print(f"Jumlah = {total}")