# Size Yazmis Oldugum Problemleri Kodlara Bakmadan, Ogrendikleriniz ve Internetten Arastiracaginiz
# Bilgilerle Birlikte Kendiniz Kodlamaya Calisiniz Sonra Gelip Kodu Inceleyebilirsiniz

kurs_adi = "Cafune344 ile Birlikte Python Kodlama Dersi"
website = "https://www.github.com/"

# 1 - 'Cafune344' Karakter Dizisinin Bas ve Sondaki Bosluk Karakterlerini Siliniz
# 2 - kurs_adi Degiskenindeki Tum Karakterleri Kucuk Harfe Ceviriniz
# 3 - website Degiskeninde Kac Tane '.' Karakteri Vardir
# 4 - website Degiskeni 'https' ile mi Basliyor
# 5 - website 'com' ile mi Bitiyor
# 6 - kurs_adi Icerisindeki Tum Karakterler Harflerden mi Olusuyor
# 7 - kurs_adi Degiskenindeki Tum Bosluklari '-' ile Degistiriniz
# 8 - kurs_adi Degiskenindeki Python Kelimesini ReactJS ile Degistiriniz
# 9 - website Degiskeni 'www' iceriyor mu
# 10 - kurs_adi Degiskenini Listeye Ceviriniz

# ---------------------------------------------------------------------------------------------------------

# 1 - 'Cafune344' Karakter Dizisinin Bas ve Sondaki Bosluk Karakterlerini Siliniz:

cevap = kurs_adi.strip()
print(cevap)

# 2 - kurs_adi Degiskenindeki Tum Karakterleri Kucuk Harfe Ceviriniz:

cevap = kurs_adi.lower()
print(cevap)

# 3 - website Degiskeninde Kac Tane '.' Karakteri Vardir:

cevap = website.count(".")
print(cevap)

# 4 - website Degiskeni 'https' ile mi Basliyor:

cevap = website.startswith("https")
print(cevap)

# 5 - website 'com' ile mi Bitiyor:

cevap = website.endswith("com")
print(cevap)

# 6 - kurs_adi Icerisindeki Tum Karakterler Harflerden mi Olusuyor:

cevap = kurs_adi.isalpha()
print(cevap)

# 7 - kurs_adi Degiskenindeki Tum Bosluklari '-' ile Degistiriniz:

cevap = kurs_adi.replace(" ", "-")
print(cevap)

# 8 - kurs_adi Degiskenindeki Python Kelimesini ReactJS ile Degistiriniz:

cevap = kurs_adi.replace("Python", "ReactJS")
print(cevap)

# 9 - website Degiskeni 'www' iceriyor mu:

cevap = website.find("www")
print(cevap)

# 10 - kurs_adi Degiskenini Listeye Ceviriniz:

cevap = kurs_adi.split()
print(cevap)