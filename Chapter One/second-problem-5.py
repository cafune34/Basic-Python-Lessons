# Size Yazmis Oldugum Problemleri Kodlara Bakmadan, Ogrendikleriniz ve Internetten Arastiracaginiz
# Bilgilerle Birlikte Kendiniz Kodlamaya Calisiniz Sonra Gelip Kodu Inceleyebilirsiniz

"""  
Uygulama 1: Yarıçapı klavyeden girilen bir dairenin alan ve çevresini hesaplayınız.  
Alan: πr²
Çevre: 2πr  

Uygulama 2: Klavyeden girilen km bilgisini mil cinsinden hesaplayınız.  
mil = km / 1.609344
"""

# Uygulama-1

pi_sayisi = 3.14

# Input Degeri String Olarak Aldigi Icin Tum Degerleri Kapsiyacak Float ile Degistirmemiz Gerekiyor

daire_yaricap = float(input("Dairenin Yaricapini Giriniz: "))

# pow Methodu ile Bir Sayinin Ussunu Alabilirsiniz

daire_alan = pi_sayisi * pow(daire_yaricap, 2)
daire_cevre = 2 * pi_sayisi * daire_yaricap

print(f"Dairenin Yaricapi: {daire_yaricap}, Cevresi: {daire_cevre}, Alani: {daire_alan}")

# Uygulama-2

yol_km = float(input("Hesaplanacak Kilometre Degerini Giriniz: "))

# round Methodu ile Sayilari Yuvarlamak Icın Kullaniriz

mil_to_km = round((yol_km / 1.609344), 2)

print(f"{yol_km} Kilometre = {mil_to_km} Mil")