kurs_adi = "Python ile Programlama"
kurs_aciklama = "Kendinize Deger Katin"
kurs_suresi = "10 Saat"

# Mesaj Degiskeni Kurs Bilgilerini Bir Araya Getiriyor
mesaj = "Kurs Adi: " + kurs_adi + ", " + "Kurs Aciklamasi: " + kurs_aciklama + ", " + "Kurs Suresi: " + kurs_suresi

# Ilk Karakter ve Son Karakter
print(mesaj[0])                 # K
print(kurs_adi[0])              # P
print(kurs_adi[-1])             # a
  
# String Uzunlugu  
adet = len(kurs_adi)            # Toplam Karakter Sayisi
  
print(adet)                     # 22
print(kurs_adi[adet - 1])       # Son Karakter (a)
  
# Dilimleme işlemleri  
print(kurs_adi[0:6])            # Ilk 6 Karakter: "Python"
print(kurs_adi[:6])             # Ayni Sekilde: "Python"
print(kurs_adi[11:adet])        # 11. Indeksten Sona Kadar: "Programlama"
print(kurs_adi[11:])            # Ayni Sekilde: "Programlama"
print(kurs_adi[-11:])           # Negatif Indeksleme ile: "Programlama"
  
# Ikili Atlama ile Dilimleme  
print(kurs_adi[0:20:2])         # 0'dan 20'ye Kadar 2 Karakter Atlayarak: "Pto l rgaml"
  
# Tersine Cevirme  
print(kurs_adi[::-1])           # "amalmargoP eli nohtyP"

k_ad = "Hakan"
k_soyad = "Cafune"
k_yas = 20

# String Birlestirme (concatenation)
msj = "Benim Adim is " + k_ad + " " + k_soyad + ". " + "Ben " + str(k_yas) + " Yasindayim."
print(msj)

# String Format Kullanimi
msj = "Benim Adim {} {}. Ben {} Yasindayim.".format(k_ad, k_soyad, k_yas)
print(msj)

msj = "Benim Adim {0} {1}. Ben {2} Yasindayim.".format(k_ad, k_soyad, k_yas)
print(msj)

msj = "Ben {y} Yasindayim. Benim Adim {a} {s}.".format(a=k_ad, s=k_soyad, y=k_yas)
print(msj)

# f-string Kullanimi
msj = f"Benim Adim {k_ad} {k_soyad}. Ben {k_yas} Yasindayim."
print(msj)