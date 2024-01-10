# Dictionary Harga Menu Makanan dan Minuman
menu = {
    '1': {'item': 'nasi goreng', 'harga': 13000},
    '2': {'item': 'nasi kuning', 'harga': 10000},
    '3': {'item': 'nasi uduk', 'harga': 10000},
    '4': {'item': 'nasi uduk make telor', 'harga': 14000},
    '5': {'item': 'nasi ayam geprek', 'harga': 17000},
    '6': {'item': 'Air Aqua', 'harga': 4000},
    '7': {'item': 'Teh Hangat', 'harga': 4000},
    '8': {'item': 'Es Teh Manis', 'harga': 5000},
    '9': {'item': 'es kelapa', 'harga': 5000},
    '10': {'item': 'Es Jeruk', 'harga': 6000},
}

def tampilkan_menu(daftar):
    print("{:<10} {:<25} {:<15}".format('No', 'Nama', 'Harga'))
    print("---------------------------------------------")
    for nomor, detail in daftar.items():
        print("{:<10} {:<25} Rp {:<15}".format(nomor, detail['item'], detail['harga']))

def pesan_makanan():
    pesanan = {}
    while True:
        tampilkan_menu(menu)
        pilihan = input("Pilih nomor menu (atau ketik '0' untuk mengakhiri): ")

        if pilihan.lower() == '0':
            break

        if pilihan in menu:
            jumlah = int(input(f"Jumlah {menu[pilihan]['item']}: "))
            pesanan[menu[pilihan]['item']] = {'jumlah': jumlah, 'harga': menu[pilihan]['harga']}
        else:
            print("Pilihan tidak valid. Silakan pilih nomor menu yang benar.")
    return pesanan

def hitung_total(pesanan):
    total = 0
    for item, info in pesanan.items():
        total += info['jumlah'] * info['harga']
    return total

def cetak_struk(pesanan, total_harga):
    print("\n--- Struk Pembelian ---")
    print("\n--- RESTO BANG LOUIS ---")
    print("Menu yang di pesan")
    for item, info in pesanan.items():
        print(f"{info['jumlah']} {item} - Rp {info['jumlah'] * info['harga']}")
    print("----------------------")
    print(f"Total Harga   : Rp {total_harga}")

    # Meminta input jumlah uang pembeli
    uang_pembeli = int(input("Masukkan jumlah uang pembeli: "))

    # Menghitung kembalian
    kembalian = uang_pembeli - total_harga

    # Menampilkan informasi uang pembeli dan kembalian
    print(f"Uang Pembeli  : Rp {uang_pembeli}")
    print(f"Kembalian     : Rp {kembalian}")

    print("Terima kasih atas pesanan Anda di kantin kami! Semoga makanan yang Anda pilih memberikan kepuasan untuk lidah Anda.")

print("=================================")
print("           RESTO BANG LOUIS         ")
print("=================================")
pembeli = input("Masukkan nama Pembeli: ")
print("Nama Pembeli :", pembeli)

while True:
    daftar_pesanan = pesan_makanan()
    total_harga = hitung_total(daftar_pesanan)
    cetak_struk(daftar_pesanan, total_harga)

    ulang = input("Apakah Anda ingin memesan lagi? (Ketik '1' untuk ya, '0' untuk tidak): ")
    if ulang != '1':
        print("Terima kasih atas kunjungan Anda!")
        break
