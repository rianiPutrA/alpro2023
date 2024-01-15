class BidangDatar:
    luas = None
    jenis = None


def luas_segitiga():
    print()
    print("Luas segitiga")
    alas = int(input("masukkan alas: "))
    tinggi = int(input("masukkan tinggi: "))
    luas = 0.5 * alas * tinggi

    bidang_datar = BidangDatar()
    bidang_datar.luas = luas
    bidang_datar.jenis = "segitiga"

    return bidang_datar


def luas_persegi_panjang():
    bidang_datar = "persegi panjang"
    print()
    print("Luas persegi panjang")
    panjang = int(input("masukkan panjang: "))
    lebar = int(input("masukkan lebar: "))
    luas = panjang * lebar

    bidang_datar = BidangDatar()
    bidang_datar.luas = luas
    bidang_datar.jenis = "persegi panjang"

    return bidang_datar


def luas_lingkaran():
    bidang_datar = "lingkaran"
    print()
    print("luas lingkaran")
    jarijari = int(input("masukkan jari-jari: "))
    luas = 3.14 * jarijari * jarijari

    bidang_datar = BidangDatar()
    bidang_datar.luas = luas
    bidang_datar.jenis = "lingkaran"

    return bidang_datar


def luas_jajar_genjar():
    bidang_datar = "jajargenjar"
    print()
    print("luas jajar genjar")
    alas = int(input("masukkan alas: "))
    tinggi = int(input("masukkan tinggi: "))
    luas = alas * tinggi

    bidang_datar = BidangDatar()
    bidang_datar.luas = luas
    bidang_datar.jenis = "jajargenjar"

    return bidang_datar


if __name__ == "__main__":
    while True:
        print("Menu")
        print("===================")
        print("1. Luas Segitiga")
        print("2. Luas Persegi Panjang")
        print("3. Luas Lingkaran")
        print("4. Luas Jajar Genjar")
        print("5. kembali")
        menu = int(input("Pilih Menu: "))

        if menu == 5:
            break

        if menu == 1:
            bidang_datar = luas_segitiga()
        elif menu == 2:
            bidang_datar = luas_persegi_panjang()
        elif menu == 3:
            bidang_datar = luas_lingkaran()
        elif menu == 4:
            bidang_datar = luas_jajar_genjar()

        print("luas {} adalah {}".format(bidang_datar.jenis, bidang_datar.luas))
        print()
