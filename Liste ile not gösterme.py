ders = "İngilizce"

ogrenciler = ["Berkay", "Muhammet", "Ali", "Enes", "Ahmet"]
notlar = [98, 59, 74, 81, 100]

for i in range(len(ogrenciler)):
  ogrenci = ogrenciler[i]
  notu = notlar[i]
  print(f"{ogrenci}`nin {ders} ders notu: {notu}")
