import os

# 1. Pastikan folder 'data' ada (mencegah error jika folder belum dibuat)
os.makedirs("data", exist_ok=True)

# 2. Latihan 1: Menulis File
with open("data/catatan.txt", "w", encoding="utf-8") as file:
    file.write("Algoritma dan Pemrograman\n")
    file.write("Pertemuan 12\n")

print("File 'data/catatan.txt' berhasil ditulis!")
