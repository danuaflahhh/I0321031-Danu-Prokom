print("=================JAKARTA PYTHON AIRLINES=================")
harga = 15000000
seat = ['1A', '1B', '1C', '2A', '2B', '2C', '3A', '3B', '3C', '4A', '4B', '4C', '5A', '5B', '5C']
pilihan = []

nama = str(input("Nama Pembeli\t: "))
no = str(input("Nomor HP\t: "))
asal = str(input("Asal Kota\t: "))

print('Seat:', seat)

def hitung():
    def nota():
        print("==========JAKARTA PYTHON AIRLINES==========")
        print("Nama pembeli\t\t: ", nama)
        print("No HP\t\t\t: ", no)
        print("Asal kota\t\t: ", asal)
        print("Total pembayaran\t: Rp", int(bayar))
    beli = len(pilihan)
    if beli % 5 == 0:
        diskon = beli / 5
        potongan = harga * 5 * diskon * 5/100
        total = (harga * beli) - potongan
        print('Total pembelian: Rp', int(total))
        print("Pajak 10%")
        pajak = total * 10/100
        bayar = total + pajak
        print("Jumlah pembayaran Anda: Rp", int(bayar))
        uang = int(input("Jumlah uang: Rp "))
        kembalian = uang - bayar
        print("Uang kembalian sebesar: Rp", int(kembalian))
        nota()
    elif beli % 5 != 0:
        total = harga * beli
        print('Total pembelian: Rp', int(total))
        print("Pajak 10%")
        pajak = total * 10/100
        bayar = total + pajak
        print("Jumlah pembayaran Anda: Rp", int(bayar))
        uang = int(input("Jumlah uang: Rp "))
        kembalian = uang - bayar
        print("Uang kembalian sebesar: Rp", int(kembalian))
        nota()

def P():
    x = str(input("Pilih seat\t: "))
    if x == '':
        print("Terjadi kesalahan input, coba periksa kembali")
        P()
    else:
        if seat.count(x) != 0:
            seat.remove(x)
            pilihan.append(x)
            print("Seat terpilih\t: ", pilihan)
            y = str(input("Apakah ada pilihan seat lagi? (Y/N): "))
            if y == "Y":
                P()
            elif y == "N":
                hitung()
            else:
                print("Terjadi kesalahan input, coba periksa kembali")
        elif seat.count(x) == 0:
            print("Seat tidak tersedia, coba seat lain")
            P()

P()