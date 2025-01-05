# Basit Olarak Temel Bazi Veri Tiplerini Isleyecegiz

"""
|---------|---------|---------|
| Numeric | Text    | Boolean |
|---------|---------|---------|
| int     | str     | bool    |
| float   |         |         |
|---------|---------|---------|

"""

isim = "Ahmet"
yas = 21
kilo = 85.5
ogrenci_mi = True

print(type(isim))        # str
print(type(yas))         # int
print(type(kilo))        # float
print(type(ogrenci_mi))  # bool

print("Ad: " + isim + ", Yas: " + str(yas) + ", Kilo: " + str(kilo) + ", Ogrenci mi: " + str(ogrenci_mi))