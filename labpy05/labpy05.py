# Program Daftar Nilai Mahasiswa Menggunakan Dictionary

data_mahasiswa = {}

def hitung_nilai_akhir(tugas, uts, uas):
    return (tugas * 0.30) + (uts * 0.35) + (uas * 0.35)

while True:
    print("\n=== MENU PILIHAN ===")
    print("1. Tambah Data")
    print("2. Ubah Data")
    print("3. Hapus Data")
    print("4. Tampilkan Data")
    print("5. Cari Data")
    print("6. Keluar")

    pilih = input("Pilih menu (1-6): ")

    # ===================== TAMBAH DATA ===================== #
    if pilih == "1":
        nim = input("NIM Mahasiswa  : ")
        nama = input("Nama Mahasiswa : ")
        tugas = float(input("Nilai Tugas    : "))
        uts = float(input("Nilai UTS      : "))
        uas = float(input("Nilai UAS      : "))

        nilai_akhir = hitung_nilai_akhir(tugas, uts, uas)

        data_mahasiswa[nim] = {
            'nama': nama,
            'tugas': tugas,
            'uts': uts,
            'uas': uas,
            'akhir': nilai_akhir
        }

        print("Data berhasil ditambahkan.")

    # ===================== UBAH DATA ===================== #
    elif pilih == "2":
        nim = input("Masukkan NIM mahasiswa yang akan diubah: ")
        if nim in data_mahasiswa:
            nama  = input("Nama baru       : ")
            tugas = float(input("Nilai Tugas baru: "))
            uts   = float(input("Nilai UTS baru  : "))
            uas   = float(input("Nilai UAS baru  : "))

            nilai_akhir = hitung_nilai_akhir(tugas, uts, uas)

            data_mahasiswa[nim] = {
                'nama': nama,
                'tugas': tugas,
                'uts': uts,
                'uas': uas,
                'akhir': nilai_akhir
            }

            print("Data berhasil diubah.")
        else:
            print("Data tidak ditemukan!")

    # ===================== HAPUS DATA ===================== #
    elif pilih == "3":
        nim = input("Masukkan NIM mahasiswa yang akan dihapus: ")
        if nim in data_mahasiswa:
            del data_mahasiswa[nim]
            print("Data berhasil dihapus.")
        else:
            print("Data tidak ditemukan!")

    # ===================== TAMPILKAN DATA (TABEL) ===================== #
    elif pilih == "4":
        if data_mahasiswa:
            print("\n=== DAFTAR NILAI MAHASISWA ===")
            print("="*85)
            print(f"{'No':<4}{'NIM':<12}{'Nama':<20}{'Tugas':<10}{'UTS':<10}{'UAS':<10}{'Akhir':<10}")
            print("="*85)

            no = 1
            for nim, nilai in data_mahasiswa.items():
                print(f"{no:<4}{nim:<12}{nilai['nama']:<20}{nilai['tugas']:<10}{nilai['uts']:<10}{nilai['uas']:<10}{nilai['akhir']:<10.2f}")
                no += 1

            print("="*85)
        else:
            print("Belum ada data.")

    # ===================== CARI DATA ===================== #
    elif pilih == "5":
        nim = input("Masukkan NIM mahasiswa yang dicari: ")
        if nim in data_mahasiswa:
            nilai = data_mahasiswa[nim]
            print(f"\nData ditemukan untuk NIM {nim}:")
            print(f"Nama         : {nilai['nama']}")
            print(f"Tugas        : {nilai['tugas']}")
            print(f"UTS          : {nilai['uts']}")
            print(f"UAS          : {nilai['uas']}")
            print(f"Nilai Akhir  : {nilai['akhir']:.2f}")
        else:
            print("Data tidak ditemukan!")

    # ===================== KELUAR PROGRAM ===================== #
    elif pilih == "6":
        print("Program selesai.")
        break

    else:
        print("Pilihan salah, coba lagi.")