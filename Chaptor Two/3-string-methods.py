# Burada Size Bazi Temel Methodlardan Bahsedecegim

mesaj = "  cafune344, siZLere Python anlatiyor"

# Metindeki Tum Harfleri Buyuk Harfe Cevirir
sonuc = mesaj.upper()
print(sonuc)

# Metindeki Tum Harfleri Kucuk Harfe Cevirir
sonuc = mesaj.lower()
print(sonuc)

# Her Kelimenin Ilk Harfini Buyuk Yapar
sonuc = mesaj.title()
print(sonuc)

# İlk Harfi Buyuk Digerlerini Kucuk Yapar
sonuc = mesaj.capitalize()
print(sonuc)

# Tum Harflerin Kucuk Olup Olmadigini Kontrol Eder
sonuc = "abc".islower()
print(sonuc)

# Metnin Basindaki ve Sonundaki Bosluklari Kaldirir
sonuc = mesaj.strip()
print(sonuc)

# Metni Bosluklardan Bolerek Liste Yapar
sonuc = mesaj.split()
print(sonuc)

# Metni Virgullerden Bolerek Liste Yapar
sonuc = mesaj.split(',')
print(sonuc)

# "Python" Kelimesinin Basladigi Indeksi Doner
sonuc = mesaj.index("Python")
print(sonuc)

# Metnin "a" ile Baslayip Baslamadigini Kontrol Eder
sonuc = mesaj.startswith("a")
print(sonuc)

# Metnin "u" ile Bitip Bitmedigini Kontrol Eder
sonuc = mesaj.endswith("u")
print(sonuc)

# "python" Kelimesini "javascript" ile Degistirir
sonuc = mesaj.replace("python", "javascript")
print(sonuc)