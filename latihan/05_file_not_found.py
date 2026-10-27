try:
    with open("data/tidak_ada.txt", "r", encoding="utf-8") as file:
        print(file.read())
except FileNotFoundError:
    print("File tidak ditemukan.")
    