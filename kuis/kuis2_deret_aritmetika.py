# Kuis 2: Deret Aritmetika
# Spesifikasi:
# - Input a (suku pertama) dan d (beda) bertipe float
# - Input n (banyak suku) bertipe int dengan validasi while (harus > 0)
# - Perulangan for untuk menghitung tiap suku dan total deret

print("Deret Aritmetika")
a = float(input("Suku pertama a: "))
d = float(input("Beda d: "))
n = int(input("Banyak suku n: "))

# Validasi input n
while n <= 0:
    print("n harus bilangan bulat positif.")
    n = int(input("Banyak suku n: "))

total = 0
for i in range(n):
    suku = a + i * d
    total += suku
    print(f"Suku ke-{i + 1}: {suku:.2f}")

print(f"Jumlah = {total:.2f}")