teks = input("Masukkan nilai: ")

try:
    nilai = float(teks)
    print(f"Nilai = {nilai}")
except ValueError:
    print("Input harus berupa angka.")
    