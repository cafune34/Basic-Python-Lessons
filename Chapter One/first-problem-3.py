# Asagida ki Gibi 3 Tirnak Icerisinde Yorum Satiri Yapabiliriz

# Size Yazmis Oldugum Problemi Kodlara Bakmadan Ogrendikleriniz ve Internetten Arastiracaginiz
# Bilgilerle Birlikte Kendiniz Kodlamaya Calisiniz Sonra Gelip Kodu Inceleyebilirsiniz

"""
- Asagidaki Musterinin Bilgilerini ve Satin Aldigi Urun Bilgilerini Degiskenler Icerisinde Saklayiniz
- Toplam Odenen Ucret Nedir
- Odenen Miktarın KDV Orani Nedir (%18)

Cafune Hakan
5315647820
info@cafune344.com
Istanbul

Satın Alınan Ürünler

Ürün adı: Kablosuz Mouse
Fiyatı: 1.500 TL

Ürün adı: Kablosuz Klavye
Fiyatı: 1.000 TL

Ürün adı: Masaüstü Bilgisayar
Fiyatı: 32.500 TL
"""

musteri_ad = "Cafune"
musteri_soyad = "Hakan"
musteri_telefon_no = "5315647820"
musteri_mail_adresi = "info@cafune344.com"
musteri_sehir = "Istanbul"

kdv_oran = 0.18

urun_1_ad = "Kablosuz Mouse"
urun_1_kdvsiz = 1500
urun_1_fiyat = (urun_1_kdvsiz * kdv_oran) + urun_1_kdvsiz

urun_2_ad = "Kablosuz Klavye"
urun_2_kdvsiz = 1000
urun_2_fiyat = (urun_2_kdvsiz * kdv_oran) + urun_2_kdvsiz

urun_3_ad = "Masaüstü Bilgisayar"
urun_3_kdvsiz = 32500
urun_3_fiyat = (urun_3_kdvsiz * kdv_oran) + urun_3_kdvsiz

toplam_fiyat = urun_1_fiyat + urun_2_fiyat + urun_3_fiyat

kdv_tutari = toplam_fiyat * kdv_oran

print(f"Musteri Bilgileri: {musteri_ad} {musteri_soyad}, {musteri_telefon_no}, {musteri_mail_adresi}, {musteri_sehir}")

print(f"Toplam Odenecek Tutar: {toplam_fiyat}")

print(f"KDV Icin Odenecek Tutar: {kdv_tutari}")