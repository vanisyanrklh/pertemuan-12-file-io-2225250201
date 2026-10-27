"""
# Pertemuan 12 - File I/O dan Error Handling
Nama: [Nama Anda]
NIM: [NIM Anda]
Kelas: [Kelas Anda]

## Tujuan
Membaca, memvalidasi, mengolah, dan menulis data file dengan Python secara aman 
menggunakan penanganan error (try-except).

## Format File Input
NIM,nilai

## Cara Menjalankan
python3 tugas/rekap_nilai_file.py

## Error yang Ditangani
- FileNotFoundError: Menangani kasus ketika file input tidak ditemukan atau salah path.
- ValueError: Menangani format baris yang salah atau nilai bukan angka / di luar rentang 0-100.

## Refleksi
Salah satu error krusial yang ditangani dalam program ini adalah `ValueError`. 
Error ini muncul ketika data di dalam file tidak sesuai dengan ekspektasi program—misalnya 
kolom nilai diisi dengan huruf alih-alih angka, atau berada di luar rentang yang valid (0 hingga 100). 
Cara program menangkap dan menanganinya adalah dengan membungkus proses pembacaan dan konversi 
tipe data di dalam blok `try...except ValueError`. Jika baris data gagal divalidasi, Python 
akan menghentikan eksekusi lebih lanjut agar tidak merusak data output, lalu mencetak pesan 
kesalahan yang informatif beserta nomor barisnya agar debugging lebih mudah.
"""

import os

def proses_rekap_nilai(input_file="tugas/data_nilai.txt", output_file="tugas/hasil_rekap.txt"):
    """Fungsi utama untuk membaca, memvalidasi, dan merekap nilai dari file teks."""
    try:
        # Membuka dan membaca file input
        with open(input_file, "r") as f:
            lines = f.readlines()
        
        if not lines:
            print("Peringatan: File input kosong.")
            return False

        total_nilai = 0
        jumlah_data = 0
        hasil_list = []

        # Memeriksa apakah baris pertama adalah header
        start_idx = 0
        if "NIM" in lines[0] or "nilai" in lines[0]:
            start_idx = 1

        # Proses iterasi dan validasi baris per baris
        for i in range(start_idx, len(lines)):
            line = lines[i].strip()
            if not line:
                continue  # Lewati baris kosong
            
            parts = line.split(",")
            if len(parts) != 2:
                raise ValueError(f"Format baris tidak valid pada baris {i+1}: '{line}' (Harus format NIM,nilai)")
            
            nim = parts[0].strip()
            nilai_str = parts[1].strip()
            
            # Validasi apakah nilai dapat dikonversi menjadi angka
            try:
                nilai = float(nilai_str)
            except ValueError:
                raise ValueError(f"Nilai bukan angka pada baris {i+1}: '{nilai_str}'")
            
            # Validasi rentang nilai (0 - 100)
            if not (0 <= nilai <= 100):
                raise ValueError(f"Nilai di luar rentang 0-100 pada baris {i+1}: {nilai}")
            
            total_nilai += nilai
            jumlah_data += 1
            
            # Menentukan status kelulusan (KKM = 60)
            status = "Lulus" if nilai >= 60 else "Remedial"
            hasil_list.append(f"{nim},{nilai},{status}")

        # Menghitung rata-rata kelas
        rata_rata = total_nilai / jumlah_data if jumlah_data > 0 else 0

        # Menulis hasil ke file output
        with open(output_file, "w") as f_out:
            f_out.write("NIM,Nilai,Status\n")
            for item in hasil_list:
                f_out.write(f"{item}\n")
            f_out.write(f"\nRata-rata Kelas: {rata_rata:.2f}\n")
        
        print(f"[SUKSES] Rekapitulasi berhasil disimpan ke '{output_file}'")
        return True

    except FileNotFoundError:
        print(f"[ERROR FileNotFoundError] File '{input_file}' tidak ditemukan. Pastikan path benar.")
        return False
    except ValueError as e:
        print(f"[ERROR ValueError] Validasi Data Gagal: {e}")
        return False


def jalankan_test_case():
    """Fungsi untuk mensimulasikan Test Case secara otomatis."""
    os.makedirs("tugas", exist_ok=True)
    
    print("=" * 60)
    print(" MENJALANKAN PENGUJIAN TEST CASE")
    print("=" * 60)
    
    # Test Case 1: Normal
    print("\n--- Test Case 1: Kondisi Normal ---")
    normal_file = "tugas/data_nilai.txt"
    with open(normal_file, "w") as f:
        f.write("NIM,nilai\n101,85\n102,90\n103,45\n104,75\n")
    proses_rekap_nilai(normal_file, "tugas/hasil_rekap.txt")
    
    # Test Case 2: FileNotFoundError
    print("\n--- Test Case 2: FileNotFoundError (File Tidak Ada) ---")
    proses_rekap_nilai("tugas/file_tidak_ada.txt", "tugas/hasil_rekap.txt")
    
    # Test Case 3: ValueError (Nilai Huruf / Invalid)
    print("\n--- Test Case 3: ValueError (Format/Nilai Salah) ---")
    error_file = "tugas/data_error.txt"
    with open(error_file, "w") as f:
        f.write("NIM,nilai\n101,85\n102,abc\n") # 'abc' memicu ValueError
    proses_rekap_nilai(error_file, "tugas/hasil_rekap.txt")
    
    print("\n" + "=" * 60)
    print(" PENGUJIAN SELESAI")
    print("=" * 60)


if __name__ == "__main__":
    jalankan_test_case()
    