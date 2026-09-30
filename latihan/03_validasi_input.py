# Latihan 3: Validasi Input Nilai
# Input: Nilai ujian (float)
# Proses: Perulangan while untuk memvalidasi rentang 0 - 100
# Output: Pesan nilai diterima setelah input valid

nilai = float(input("Nilai 0-100: "))
while nilai < 0 or nilai > 100:
    print("Nilai tidak valid.")
    nilai = float(input("Nilai 0-100: "))

print(f"Nilai diterima: {nilai}")