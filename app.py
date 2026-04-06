#Hitung Luas Bangun Datar
def luas_segitiga():
    a = int(input("Masukkan Alas Segitiga: "))
    t = int(input("Masukkan Tinggi Segitiga: "))
    luas = a * t / 2
    print("Luas Segitiga adalah ", luas)

luas_segitiga()

def luas_persegi_panjang():
    p = int(input("Masukkan Panjang Persegi Panjang: "))
    l = int(input("Masukkan Lebar Persegi Panjang: "))
    luas = p * l
    print("Luas Persegi Panjang adalah ", luas)

luas_persegi_panjang()

def luas_lingkaran():
    r = int(input("Masukkan Jari-jari Lingkaran: "))
    luas = 3.14 * r * r
    print("Luas Lingkaran adalah ", luas)

luas_lingkaran()

