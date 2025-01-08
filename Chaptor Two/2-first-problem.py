# Size Yazmis Oldugum Problemi Kodlara Bakmadan, Ogrendikleriniz ve Internetten Arastiracaginiz
# Bilgilerle Birlikte Kendiniz Kodlamaya Calisiniz Sonra Gelip Kodu Inceleyebilirsiniz

title = "Python ile Programlama Dersleri"

# 1 - 'title' Degiskeni Icerisindeki Karakter Sayisi Nedir
# 2 - 'title' Icerisindeki 'Python' Kelimesini Alin
# 3 - 'title' Degiskeninin Ilk 5 ve Son 5 Karakterini Alin
# 4 - 'title' Degiskenini Tersten Yazdiriniz
# 5 - Klavyeden Girilen Ogrenci Bilgisine Gore Ornek Verilen Cumleyi Yazdiriniz
# Ornek: Harun Yilmaz Isimli Ogrencinin Vize Notu 80, Final Notu 60 ve Not Ortalamasi 70 Olarak Hesaplanmistir

# ---------------------------------------------------------------------------------------------------------

# 1 - 'title' Degiskeni Icerisindeki Karakter Sayisi Nedir:

print(len(title))

# 2 - 'title' Icerisindeki 'Python' Kelimesini Alin

print(title[0:6])

# 3 - 'title' Degiskeninin Ilk 5 ve Son 5 Karakterini Alin

print(title[:5] + title[-5:])

# 4 - 'title' Degiskenini Tersten Yazdiriniz

print(title[::-1])

# 5 - Klavyeden Girilen Ogrenci Bilgisine Gore Ornek Verilen Cumleyi Yazdiriniz

k_adi = input("Ogrencinin Adi Nedir: ")
k_soyadi = input("Ogrencinin Soyadi Nedir: ")
k_vize_not = float(input("Ogrencinin Vize Notu Nedir: "))
k_final_not = float(input("Ogrencinin Final Notu Nedir: "))

k_ort = round((k_vize_not + k_final_not) / 2, 2)

print(f"{k_adi} {k_soyadi} Isimli Ogrencinin Vize Notu {k_vize_not}, Final Notu {k_final_not} ve Not Ortalamasi {k_ort} Olarak Hesaplanmistir")

print("{ad} {soyad} Isimli Ogrencinin Vize Notu {vize}, Final Notu {final} ve Not Ortalamasi {ort} Olarak Hesaplanmistir".format(ad = k_adi, soyad = k_soyadi, vize = k_vize_not, final = k_final_not, ort = k_ort))