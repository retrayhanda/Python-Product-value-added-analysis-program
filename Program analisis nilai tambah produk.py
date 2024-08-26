data_username = []
data_password = []
a = "1"
is_submenu_2_done = False

def x1():
    print(100* '-')

def x2():
    print(45 * '=')

def x3():
    print(45 * '-')

def x4():
    print(100 * '=')

def print_table(header, rows):
    col_widths = [max(len(str(item)) for item in col) for col in zip(*rows, header)]
    total_width = sum(col_widths) + 3 * len(col_widths) - 1
    
    def format_row(row):
        return " | ".join(f"{str(item).ljust(width)}" for item, width in zip(row, col_widths))

    print(format_row(header))
    print("-" * total_width)
    for row in rows:
        print(format_row(row))

while a == "1":
    x2()
    print("PILIHAN MASUK".center(45))
    x2()
    print("1. REGISTRASI AKUN \n2. LOGIN \n")
    h = str(input("Jawab = "))
    x2()
    print(' ')
    if h == "1":
        username = input("Daftarkan Username : ")
        password = input("Daftarkan Password : ")
        password2 = input("Konfirmasi Password : ")
        if password == password2:
            data_username.append(username)
            data_password.append(password)
            print(' ')
            x3()
            print("AKUN ANDA SUDAH TERDAFTAR".center(45))
            x3()
            koreksi = False
            while not koreksi:
                print(' ')
                print("DAFTAR AKUN LAGI?".center(45))
                x2()
                print("1. Iya")
                print("2. Tidak")
                x2()
                a = input('menu = ')
                koreksi = a == "1" or a == "2"
        else:
            print(' ')
            x3()
            print("PASSWORD KONFIRMASI TIDAK COCOK".center(45))
            x3()
    elif h == "2":
        print(' ')
        a = False

# proses login
x3()
print("LOGIN".center(45))
x3()
print(' ')

n = 0
while n < 3:
    username = input("Masukkan Username : ")
    if username in data_username:
        q = data_username.index(username)
        r = False
        while not r and n < 3:
            password = input("Masukkan Password : ")
            r = password == data_password[q]
            if r:
                x2()
                print("Login Berhasil")
                print()
                x4()
                break
            else:
                print("Password salah")
                n += 1
        if r:
            break
    else:
        print("Username salah")
        n += 1
        if n >= 3:
            break

if n >= 3:
    x3()
    print("Anda telah gagal login 3 kali.".center(45))
    x3()
    exit()

print('''
        ||====================================================================================||
        ||                                                                                    ||
        ||                                                                                    ||
        ||                                                                                    ||
        ||                             Analisis Nilai Tambah Ikan                             || 
        ||                              Produk Perikanan Lemuru                               ||
        ||                             Pelabuhan Muncar Banyuwangi                            ||
        ||                                                                                    ||  
        ||                                                                                    ||
        ||                                                                                    ||
        ||                                       OLEH:                                        ||
        ||                                Rahmad Haret Rathanda                               ||
        ||                                                                                    ||                                               
        ||                                                                                    || 
        ||                                                                                    ||
        ||====================================================================================||
''')

r = False
while not r:
    print()
    print("Pilihan Menu = \n1. Latar Belakang \n2. Teori \n3. Perhitungan \n4. Logout")
    x3()
    menu = str(input("Jawab = "))
    
    print()
    if menu == "1":
        while True:
            print("============================================================================")
            print("                                LATAR BELAKANG                              ")
            print("============================================================================")
            print()
            print('Program analisis nilai tambah produk perikanan lemuru \n'
                  'pelabuhan muncar Banyuwangi memberikan gambaran umum terkait \n'
                  'kebutuhan ikan untuk bahan baku industri pengolahan ikan muncar \n'
                  'dan persentase serapan ikan segar untuk industri yang dengan memper- \n'
                  'tingkan kapasitas produksi, jenis dan jumlah mesin yang digunakan \n'
                  'untuk proses pengolahan, estimasi harga mesin, bahan baku pendukung \n'
                  'dan harga per ton dari bahan tersebut, biaya tenaga kerja dan biaya overhead')
            print()
            print("============================================================================")
            tanya = str(input("Ingin Melanjutkan Program? (y/n): "))
            if tanya.lower() == "y":
                break
            elif tanya.lower() == "n":
                print("Selesai")
                r = True
                break
    elif menu == "2":
        while True:
            print("======================================================================================")
            print("                                          TEORI                                       ")
            print("======================================================================================")
            print()
            print('1. Deskripsi Pola Distribusi : Rantai pasok menggambarkan \n'
                  'pergerakan produk dari pemasok bahan baku hingga pelanggan \n'
                  'akhir. Proses pendistribusian dari tempat pendaratan (landing site) \n'
                  'ke industri pengolahan ikan di sekitarnya.')
            print()
            print('2. Biaya Pengolahan Industri : Teori rantai pasokan memperhitungkan biaya \n'
                  'yang terkait dengan setiap tahapan dalam rantai, termasuk biaya pengolahan \n'
                  'di industri. Pengefisienan proses pengolahan ikan di industri dan faktor apa \n'
                  'yang mempengaruhi biaya tersebut.')
            print()
            print('3. Nilai Tambah Ekonomi : Konsep nilai tambah dalam rantai pasokan mengacu \n'
                  'pada peningkatan nilai produk selama setiap tahapan proses produksi. \n'
                  'Pengidentifikasian berbagai produk yang dihasilkan dari lemuru dan mengukur \n'
                  'nilai tambah ekonominya di setiap tahapan, mulai dari pengolahan hingga produk akhir.')
            print()
            print("======================================================================================")
            tanya = str(input("Ingin Melanjutkan Program? (y/n): "))
            if tanya.lower() == "y":
                break
            elif tanya.lower() == "n":
                print("Selesai")
                r = True
                break

    elif menu == "3":
        while True:
            print("Pilihan Perhitungan = \n1. Estimasi Biaya Investasi \n2. Rekapitulasi Biaya Pengolahan Ikan \n3. Nilai Tambah per Ton Produk (hanya bisa dijalankan setelah menggunakan perhitungan 2) \n4. Kembali")
            x3()
            sub_menu = str(input("Jawab = "))
            
            print()
            if sub_menu == "1":
                print("=========================================================================================================")
                print("                                           ESTIMASI BIAYA INVESTASI                                      ")
                print("=========================================================================================================")
                print()
                
                items = ["Kapal", "Mesin", "Jaring", "Genset", "Sekoci", "Lampu"]
                total_cost = 0

                header = ["Item", "Jumlah", "Harga per Unit (Rp)", "Umur Teknis (tahun)", "Biaya Investasi per Tahun (Rp)"]
                rows = []

                for item in items:
                    jumlah = float(input(f"Masukkan jumlah unit per item {item} : "))
                    harga_per_unit = float(input(f"Masukkan harga per unit {item} (Rp): "))
                    umur_teknis = int(input(f"Masukkan umur teknis {item} (tahun): "))
                    
                    biaya_investasi_tahun = (jumlah * harga_per_unit) / umur_teknis
                    total_cost += biaya_investasi_tahun

                    rows.append([item, jumlah, harga_per_unit, umur_teknis, round(biaya_investasi_tahun, 2)])
                
                rows.append(["Total", "", "", "", round(total_cost, 2)])

                print()
                print_table(header, rows)
                print()
                print("---------------------------------------------------------------------------------------------------------")
                print('Estimasi Biaya Investasi yang dimana terdiri dari (Kapal, Mesin, Jaring, Genset, Sekoci, dan Lampu) \n'
                      'untuk keperluan industri pengolahan ikan Pelabuhan Muncar Banyuwangi adalah Rp.', (total_cost))
                print()
                
            elif sub_menu == "2":
                print("=========================================================================================================")
                print("                                       REKAPITULASI BIAYA PENGOLAHAN IKAN                                ")
                print("=========================================================================================================")
                print()

                # Input data dari pengguna
                print()
                print("---------------------------------------------------------------------------------------------------------")
                print("                                              Pengalengan Ikan                                           ")
                print("---------------------------------------------------------------------------------------------------------")
                print()
                produksi_tahunan_pengalengan = int(input("Masukkan Produksi Per Tahun Pengalengan Ikan (Kg / Tahun): "))
                biaya_bahan_baku_pengalengan = float(input("Masukkan Biaya Bahan Baku Utama Pengalengan Ikan (Rp / Tahun): "))
                biaya_tenaga_kerja_pengalengan = float(input("Masukkan Biaya Tenaga Kerja Pengalengan Ikan (Rp / Tahun): "))
                biaya_bb_pendukung_pengalengan = float(input("Masukkan Biaya Bahan Baku Pendukung Pengalengan Ikan (Rp / Tahun): "))
                biaya_overhead_pengalengan = float(input("Masukkan Biaya Overhead Pengalengan Ikan (Rp / Tahun): "))
                harga_jual_estimasi_pengalengan = float(input("Masukkan Estimasi Harga Jual Pengalengan Ikan (Rp / Ton): "))
                print()
                print("---------------------------------------------------------------------------------------------------------")
                print("                                                Cold Storage                                             ")
                print("---------------------------------------------------------------------------------------------------------")
                print()
                produksi_tahunan_cold_storage = int(input("Masukkan Produksi Per Tahun Cold Storage (Kg / Tahun): "))
                biaya_bahan_baku_cold_storage = float(input("Masukkan Biaya Bahan Baku Utama Cold Storage (Rp / Tahun): "))
                biaya_tenaga_kerja_cold_storage = float(input("Masukkan Biaya Tenaga Kerja Cold Storage (Rp / Tahun): "))
                biaya_bb_pendukung_cold_storage = float(input("Masukkan Biaya Bahan Baku Pendukung Cold Storage (Rp / Tahun): "))
                biaya_overhead_cold_storage = float(input("Masukkan Biaya Overhead Cold Storage (Rp / Tahun): "))
                harga_jual_estimasi_cold_storage = float(input("Masukkan Estimasi Harga Jual Cold Storage (Rp / Ton): "))
                print()
                print("---------------------------------------------------------------------------------------------------------")
                print("                                             Tepung dan Minyak                                           ")
                print("---------------------------------------------------------------------------------------------------------")
                print()
                produksi_tahunan_tepung_minyak = float(input("Masukkan Produksi Per Tahun Tepung dan Minyak (Kg / Tahun): "))
                biaya_bahan_baku_tepung_minyak = float(input("Masukkan Biaya Bahan Baku Utama Tepung dan Minyak (Rp / Tahun): "))
                biaya_tenaga_kerja_tepung_minyak = float(input("Masukkan Biaya Tenaga Kerja Tepung dan Minyak (Rp / Tahun): "))
                biaya_bb_pendukung_tepung_minyak = float(input("Masukkan Biaya Bahan Baku Pendukung Tepung dan Minyak (Rp / Tahun): "))
                biaya_overhead_tepung_minyak = float(input("Masukkan Biaya Overhead Tepung dan Minyak (Rp / Tahun): "))
                harga_jual_estimasi_tepung_minyak = float(input("Masukkan Estimasi Harga Jual Tepung dan Minyak (Rp / Ton): "))

                # Perhitungan
                print()
                total_cost_pengalengan = biaya_bahan_baku_pengalengan + biaya_tenaga_kerja_pengalengan
                + biaya_bb_pendukung_pengalengan + biaya_overhead_pengalengan
                biaya_produksi_per_ton_pengalengan = total_cost_pengalengan / produksi_tahunan_pengalengan
                estimasi_laba_per_ton_pengalengan = harga_jual_estimasi_pengalengan - biaya_produksi_per_ton_pengalengan
                estimasi_laba_per_tahun_pengalengan = estimasi_laba_per_ton_pengalengan * produksi_tahunan_pengalengan
                pajak_pengalengan = 0.10 * estimasi_laba_per_tahun_pengalengan
                laba_bersih_pengalengan = estimasi_laba_per_tahun_pengalengan - pajak_pengalengan
                profitabilitas_pengalengan = laba_bersih_pengalengan / total_cost_pengalengan
                print()
                total_cost_cold_storage = biaya_bahan_baku_cold_storage + biaya_tenaga_kerja_cold_storage
                + biaya_bb_pendukung_cold_storage + biaya_overhead_cold_storage
                biaya_produksi_per_ton_cold_storage = total_cost_cold_storage / produksi_tahunan_cold_storage
                estimasi_laba_per_ton_cold_storage = harga_jual_estimasi_cold_storage - biaya_produksi_per_ton_cold_storage
                estimasi_laba_per_tahun_cold_storage = estimasi_laba_per_ton_cold_storage * produksi_tahunan_cold_storage
                pajak_cold_storage = 0.10 * estimasi_laba_per_tahun_cold_storage
                laba_bersih_cold_storage = estimasi_laba_per_tahun_cold_storage - pajak_cold_storage
                profitabilitas_cold_storage = laba_bersih_cold_storage / total_cost_cold_storage
                print()
                total_cost_tepung_minyak = biaya_bahan_baku_tepung_minyak + biaya_tenaga_kerja_tepung_minyak
                + biaya_bb_pendukung_tepung_minyak + biaya_overhead_tepung_minyak
                biaya_produksi_per_ton_tepung_minyak = total_cost_tepung_minyak / produksi_tahunan_tepung_minyak
                estimasi_laba_per_ton_tepung_minyak = harga_jual_estimasi_tepung_minyak - biaya_produksi_per_ton_tepung_minyak
                estimasi_laba_per_tahun_tepung_minyak = estimasi_laba_per_ton_tepung_minyak * produksi_tahunan_tepung_minyak
                pajak_tepung_minyak = 0.10 * estimasi_laba_per_tahun_tepung_minyak
                laba_bersih_tepung_minyak = estimasi_laba_per_tahun_tepung_minyak - pajak_tepung_minyak
                profitabilitas_tepung_minyak = laba_bersih_tepung_minyak / total_cost_tepung_minyak
                print()
                header = ["Jenis Industri", "Satuan", "Pengalengan Ikan", "Cold Storage", "Tepung dan Minyak"]
                rows = [
                ["Produksi Tahunan","Rp / Tahun", round(produksi_tahunan_pengalengan, 5), 
                 round(produksi_tahunan_cold_storage, 5), round(produksi_tahunan_tepung_minyak, 5)],
                ["Biaya Bahan Baku Utama","Rp / Tahun", round(biaya_bahan_baku_pengalengan, 5),
                  round(biaya_bahan_baku_cold_storage, 5), round(biaya_bahan_baku_tepung_minyak, 5)],
                ["Biaya Tenaga Kerja","Rp / Tahun", round(biaya_tenaga_kerja_pengalengan, 5), 
                 round(biaya_tenaga_kerja_cold_storage, 5), round(biaya_tenaga_kerja_tepung_minyak, 5)],
                ["BB Pendukung","Rp / Tahun", round(biaya_bb_pendukung_pengalengan, 5),
                  round(biaya_bb_pendukung_cold_storage, 5), round(biaya_bb_pendukung_tepung_minyak, 5)],
                ["Biaya Overhead","Rp / Tahun", round(biaya_overhead_pengalengan, 5),
                  round(biaya_overhead_cold_storage, 5), round(biaya_overhead_tepung_minyak, 5)],
                ["Total Cost","Rp / Tahun", round(total_cost_pengalengan, 5),
                  round(total_cost_cold_storage, 5), round(total_cost_tepung_minyak, 5)],
                ["Biaya Produksi per Ton","Rp / Ton", round(biaya_produksi_per_ton_pengalengan, 5),
                 round(biaya_produksi_per_ton_cold_storage, 5), round(biaya_produksi_per_ton_tepung_minyak, 5)],
                ["Estimasi Harga Jual","Rp / Ton", round(harga_jual_estimasi_pengalengan, 5),
                  round(harga_jual_estimasi_cold_storage, 5), round(harga_jual_estimasi_tepung_minyak, 5)],
                ["Estimasi Laba per Ton","Rp / Ton", round(estimasi_laba_per_ton_pengalengan, 5),
                  round(estimasi_laba_per_ton_cold_storage, 5), round(estimasi_laba_per_ton_tepung_minyak, 5)],
                ["Estimasi Laba per Tahun","Rp / Tahun", round(estimasi_laba_per_tahun_pengalengan, 5),
                  round(estimasi_laba_per_tahun_cold_storage, 5), round(estimasi_laba_per_tahun_tepung_minyak, 5)],
                ["Pajak (10%)"," ", round(pajak_pengalengan, 5), round(pajak_cold_storage, 5), round(pajak_tepung_minyak, 5)],
                ["Laba Bersih per Tahun"," ", round(laba_bersih_pengalengan, 5),
                  round(laba_bersih_cold_storage, 5), round(laba_bersih_tepung_minyak, 5)],
                ["Profitabilitas"," ", round(profitabilitas_pengalengan, 5), 
                 round(profitabilitas_cold_storage, 5), round(profitabilitas_tepung_minyak, 5)]
        ]   

                
                print_table(header, rows)
                is_submenu_2_done = True
                print()
                print("---------------------------------------------------------------------------------------------------------")
                print('Dan rekapitulasi biaya pengolahan ikan industri pengolahan ikan Pelabuhan Muncar Banyuwangi ini \n'
                      'memiliki rekap data seperti tabel diatas')
                print()

            elif sub_menu == "3":
                if not is_submenu_2_done:
                    print("Laba bersih belum ada\n Silahkan menjalankan submenu 2 terlebih dahulu")
                else:
                    print("============================================================================")
                    print("                        NILAI TAMBAH PER TON PRODUK                         ")
                    print("============================================================================")
                    print(" ")
                    print("----------------------------------------------------------------------------")
                    print("                                  Data Awal                                 ")
                    print("----------------------------------------------------------------------------")
                    dawal_pengalengan = float(input("Masukkan Data Awal Pengalengan Ikan : "))
                    dawal_cold_storage = float(input("Masukkan Data Awal Cold Storage : ")) 
                    dawal_tepung_minyak = float(input("Masukkan Data Awal Tepung dan Minyak : "))
                    print(" ")
                    print("----------------------------------------------------------------------------")
                    print("                                 Input Total                                ")
                    print("----------------------------------------------------------------------------")
                    input_total = float(input("Masukkan Total Olahan ( ton ) : "))
                    print(" ")
                
                    # Perhitungan
                    nilai_tambah_pengalengan = dawal_pengalengan * input_total * laba_bersih_pengalengan
                    nilai_tambah_cold_storage = dawal_cold_storage * input_total * laba_bersih_cold_storage
                    nilai_tambah_tepung_minyak = dawal_tepung_minyak * input_total * laba_bersih_tepung_minyak

                    jumlah_nilai_tambah = nilai_tambah_pengalengan + nilai_tambah_cold_storage + nilai_tambah_tepung_minyak
                    print(" ")
                    print("----------------------------------------------------------------------------")
                    print("                              Pengalengan Ikan                              ")
                    print("----------------------------------------------------------------------------")
                    print("Nilai Tambah Pengalengan Ikan : ", (nilai_tambah_pengalengan))
                    print(" ")
                    print("----------------------------------------------------------------------------")
                    print("                                 Cold Storage                               ")
                    print("----------------------------------------------------------------------------")
                    print("Nilai Tambah Cold Storage : ", (nilai_tambah_cold_storage))
                    print(" ")
                    print("----------------------------------------------------------------------------")
                    print("                               Tepung dan Minyak                            ")
                    print("----------------------------------------------------------------------------")
                    print("Nilai Tambah Tepung dan Minyak : ", (nilai_tambah_tepung_minyak))
                    print(" ")
                    print("----------------------------------------------------------------------------")
                    print("                               Jumlah Nilai Tambah                          ")
                    print("----------------------------------------------------------------------------")
                    print("Jumlah Nilai Tambah : Rp", (jumlah_nilai_tambah))
            
                    print()
                    print("============================================================================")
                    print('Nilai tambah perton produk pengolahan ikan Pelabuhan Muncar Banyuwangi ini \n' 
                        'adalah Rp', (jumlah_nilai_tambah))
                    print("----------------------------------------------------------------------------")

            elif sub_menu == "4":
                break
            else:
                print("Pilihan Tidak Valid, Coba Lagi.")
                x3()
    elif menu == "4":
        print("Logout Berhasil. Terima kasih!")
        break
    else:
        print("Pilihan Tidak Valid, Coba Lagi.")
        x3()