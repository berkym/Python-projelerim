import random

print("Burç yorumlamaya hoşgeldiniz. Burcunuzu yazarak başlayabilirsiniz.")

zaman_listesi = ["Bugün", "Yarın", "Çok yakında"]
etkinlik_listesi = ["Karşılaşacaksınız", "Sizinle olacak", "Bulacaksınız"]
obje_listesi = ["Sihirli bir şey", "Bir olay", "Bu bir sürpriz"]

while True:
  burc = input("Burcunuzu giriniz: ")
  zaman = zaman_listesi[random.randint(0, len(zaman_listesi) - 1)]
  etkinlik = etkinlik_listesi[random.randint(0, len(etkinlik_listesi) - 1)]
  obje = obje_listesi[random.randint(0, len(obje_listesi) - 1)]

  print(zaman + " " + etkinlik + " " + obje)
  sonra = input("Tekrar denemek ister misiniz?: ")
  if sonra.lower() != "evet" or sonra.lower() != "olur":
    break

print("Yeni tahmin için daha sonra tekrar gelebilirsiniz.")
