# Latihan 2: Membaca File
with open("data/catatan.txt", "r", encoding="utf-8") as file:
    for baris in file:
        print(baris.strip())
        