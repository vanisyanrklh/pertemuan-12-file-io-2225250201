# Latihan 3: Append File
with open("data/catatan.txt", "a", encoding="utf-8") as file:
    file.write("Latihan append berhasil.\n")

    print("Data berhasil ditambahkan ke file")
    