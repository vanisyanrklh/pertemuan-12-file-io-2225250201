def baca_data(nama_file):
    data = []

    with open(nama_file, "r") as file:
        for baris in file:
            baris = baris.strip()

            try:
                nim, teks_nilai = baris.split(",")
                nilai = float(teks_nilai)
                data.append((nim, nilai))
            except ValueError:
                print(f"Data tidak valid: {baris}")

    return data


def tulis_rekap(nama_file, data):
    if len(data) == 0:
        return

    nilai = [n for _, n in data]

    jumlah = len(nilai)
    rata_rata = sum(nilai) / jumlah
    tertinggi = max(nilai)
    terendah = min(nilai)

    with open(nama_file, "w") as file:
        file.write("HASIL REKAP NILAI\n")
        file.write(f"Jumlah data valid: {jumlah}\n")
        file.write(f"Rata-rata: {rata_rata:.2f}\n")
        file.write(f"Nilai tertinggi: {tertinggi}\n")
        file.write(f"Nilai terendah: {terendah}\n")


input_file = "data/nilai.txt"
output_file = "data/hasil_rekap.txt"

data = baca_data(input_file)
tulis_rekap(output_file, data)

print("Rekap selesai dibuat.")

    