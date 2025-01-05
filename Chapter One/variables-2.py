# Kaydedecegimiz Farklı Degiskenlerle Matematiksel Islemler

urunAFiyat = 10000
urunBFiyat = 5000
kdvOrani = 0.40

print(urunAFiyat + (urunAFiyat * kdvOrani))
print(urunBFiyat + (urunBFiyat * kdvOrani))

urunToplami = urunAFiyat + urunBFiyat

print(urunToplami + (urunToplami * kdvOrani)) 

sayi1 = 20
sayi2 = 30

# 3sayi = 40  -> Degisken Isimleri Hicbir Zaman Sayi ile Baslayamaz

sayi3 = 50

# sayi3@ = 60 => Degiskenler Içerisinde Sadece '_' Kullanılabilir

urunFiyati = 2000
urun_fiyati = 5000

yas = 20
YAS = 30  # Case Sensitive

# Komut Isimlerinden Kullanmamaliyiz
# True = "ahmet"

x = "10"
y = "20"

# Eger Toplanan Deger String ise Iki Stringi Birlestirerek Yazar

print(x + y)  # 1020

# Bu Islem String Tipini Integer Tipine Donusturerek Toplama Yapar

print(int(x) + int(y))  # 30

# Sirasiyla Deger Atama veya Bir Deger Atama

x, y, z = 10, 20, 30
x, y, z = 50