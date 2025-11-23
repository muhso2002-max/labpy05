# Flowchart

                         ┌─────────────────────────┐
                         │          MULAI          │
                         └───────────────┬─────────┘
                                         │
                                         ▼
                             ┌─────────────────────────┐
                             │   Inisialisasi data = {}│
                             └───────────────┬─────────┘
                                             │
                                             ▼
                             ┌────────────────────────────────┐
                             │            MENU:               │
                             │ 1. Tambah Data                 │
                             │ 2. Ubah Data                   │
                             │ 3. Hapus Data                  │
                             │ 4. Lihat Data                  │
                             │ 5. Cari Data                   │
                             │ 6. Keluar                      │
                             └───────────────┬────────────────┘
                                             │
                                             ▼
                             ┌───────────────────────────┐
                             │     Input pilihan menu    │
                             └───────────────┬───────────┘
                                             │
         ┌───────────────────────────────────┼─────────────────────────────────────┐
         │                                   │                                     │
         ▼                                   ▼                                     ▼

    ┌──────────────┐         ┌────────────────┐           ┌──────────────────┐
    │ Pilihan = 1? │─Yes───▶ │  TAMBAH DATA   │           │  Pilihan = 2?    │
    └───────┬──────┘         └──────┬─────────┘           └─────────┬────────┘
            │                        │                               │
            ▼                        ▼                               ▼
    ┌───────────────────┐   ┌──────────────────────┐        ┌───────────────────┐
    │ Input NIM          │   │ UBAH DATA            │        │ Input NIM         │
    │ Input Nama         │   └──────────┬───────────┘        │ Jika ada → ubah  │
    │ Input Tugas        │              │                    │ Jika tidak → err │
    │ Input UTS          │              ▼                    └───────────────────┘
    │ Input UAS          │   ┌────────────────────────┐               │
    │ Hitung Nilai Akhir │   │ Jika ketemu → update   │               ▼
    │ Simpan ke dict     │   │ Jika tidak → error     │       Kembali ke Menu
    └───────────────────┘   └────────────────────────┘

    ▼
    ┌──────────────┐
    │ Pilihan = 3? │──Yes──────────────────────────────▶ HAPUS DATA
    └───────┬──────┘
            │
            ▼
    ┌────────────────────────┐
    │ Input NIM              │
    │ Jika ketemu → hapus    │
    │ Jika tidak → error     │
    └────────────────────────┘
            ▼
       Kembali ke menu

    ▼
    ┌──────────────┐
    │ Pilihan = 4? │──Yes────────────────────────────▶ TAMPILKAN DATA
    └───────┬──────┘
            │
            ▼
    ┌──────────────────────────┐
    │ Cetak seluruh isi data   │
    │ Jika kosong → "No data"  │
    └──────────────────────────┘
            ▼
       Kembali ke menu

    ▼
    ┌──────────────┐
    │ Pilihan = 5? │──Yes────────────────────────────▶ CARI DATA
    └───────┬──────┘
            │
            ▼
    ┌──────────────────────────┐
    │ Input NIM                │
    │ Jika ada → tampilkan     │
    │ Jika tidak → error       │
    └──────────────────────────┘
            ▼
       Kembali ke menu

    ▼
    ┌──────────────┐
    │ Pilihan = 6? │──Yes────────────▶ SELESAI
    └───────┬──────┘
            │
            ▼
    ┌──────────────────────────┐
    │     Input salah!         │
    │     Kembali ke menu      │
    └──────────────────────────┘

## Penjelasan Program

1.  **Mulai Program**\
    Inisialisasi dictionary kosong `data = {}` untuk menyimpan data
    mahasiswa.

2.  **Tampilkan Menu**\
    Menampilkan pilihan: Tambah, Ubah, Hapus, Tampilkan, Cari, Keluar.

3.  **Input Pilihan Menu**\
    User memilih menu dan program mengecek angka tersebut.

4.  **Tambah Data**\
    Input NIM, Nama, Tugas, UTS, UAS → hitung nilai akhir → simpan ke
    dictionary.

5.  **Ubah Data**\
    Input NIM → jika ada datanya, diperbarui → nilai akhir dihitung
    ulang.

6.  **Hapus Data**\
    Input NIM → jika ditemukan, data dihapus.

7.  **Tampilkan Semua Data**\
    Jika data kosong → tampilkan pesan. Jika ada → tampilkan seluruh isi
    dictionary.

8.  **Cari Data**\
    Input NIM → tampilkan data jika ada, jika tidak muncul pesan error.

9.  **Keluar Program**\
    Program berhenti.

10. **Input Tidak Valid**\
    Jika pilihan di luar 0--5 → tampilkan pesan error.

    
