# ============================================
# TUGAS PROJECT : SISTEM NILAI MAHASISWA
# Nama          : Dendi Pratama Riawan
# Mata Kuliah   : Python
# Github        : https://github.com/DendiPratamaRiawan
# Linkedin      : www.linkedin.com/in/dendipratamar
# UNIVERSITAS FALETEHAN
# ============================================

# ====== CLASS (OOP) ======
class Mahasiswa:
    def __init__(self, nama, nim):
        self.nama = nama
        self.nim = nim
        self.nilai = []

    # ====== FUNCTION DENGAN OPERATOR ======
    def tambah_nilai(self, nilai):
        # Bagian ini menggunakan operator '+=' (menjawab poin OPERATOR)
        self.nilai.append(nilai)
        print("Nilai " + str(nilai) + " berhasil ditambahkan untuk " + self.nama + ".")

    def rata_rata(self):
        # Menggunakan kondisi dan perulangan (menjawab poin KONDISI & PERULANGAN)
        if len(self.nilai) == 0:
            return 0
        total = 0
        for n in self.nilai:
            total += n  # operator +=
        return total / len(self.nilai)

    def tampilkan_info(self):
        # Bagian ini mengandung String Manipulation dan Type Casting
        print("\n==============================")
        print("Nama: " + self.nama.upper())  # STRING MANIPULATION: upper()
        print("NIM : " + str(self.nim))
        print("Daftar Nilai: " + ", ".join([str(n) for n in self.nilai]))  # STRING MANIPULATION: join()
        print("Rata-rata: " + str(float(self.rata_rata())))  # TYPE CASTING: float()

# ====== FUNCTION BIASA ======
# Bagian ini menjawab poin FUNCTION
def konversi_huruf(nilai):
    # Menggunakan KONDISI (if-elif-else)
    if nilai >= 85:
        return "A"
    elif nilai >= 70:
        return "B"
    elif nilai >= 55:
        return "C"
    elif nilai >= 40:
        return "D"
    else:
        return "E"

# ====== LAMBDA FUNCTION ======
# Menjawab poin LAMBDA FUNCTION
status_kelulusan = lambda rata: "LULUS" if rata >= 55 else "TIDAK LULUS"

# ====== PROGRAM UTAMA ======
def main():
    print("=== SISTEM NILAI MAHASISWA ===")

    # Input data mahasiswa
    nama = input("Masukkan nama mahasiswa: ")
    nim = input("Masukkan NIM: ")

    # Membuat objek dari class Mahasiswa (menjawab poin OOP)
    mhs = Mahasiswa(nama, nim)

    # Perulangan untuk input nilai (menjawab poin PERULANGAN)
    while True:
        try:
            nilai = int(input("Masukkan nilai (0-100): "))
            if 0 <= nilai <= 100:
                mhs.tambah_nilai(nilai)
            else:
                print("Nilai harus antara 0 - 100!")
        except ValueError:
            print("Input tidak valid, masukkan angka!")
            continue

        lanjut = input("Tambah nilai lagi? (y/n): ").lower()
        if lanjut != 'y':
            break

    # Menampilkan hasil akhir
    mhs.tampilkan_info()

    rata2 = mhs.rata_rata()
    print("Nilai Huruf: " + konversi_huruf(rata2))
    print("Status: " + status_kelulusan(rata2))

# Jalankan program
if __name__ == "__main__":
    main()
