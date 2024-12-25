import random

print("Şifre oluşturucu")

uzunluk = int(input("şifreniz ne kadar uzun olacak? (Max: 9): "))

if uzunluk == 1:
  sifre = random.randint(0,9)
  print(sifre)

elif uzunluk == 2:
  sifre = random.randint(0,99)
  print(sifre)

elif uzunluk == 3:
  sifre = random.randint(0,999)
  print(sifre)

elif uzunluk == 4:
  sifre = random.randint(0,9999)
  print(sifre)

elif uzunluk == 5:
  sifre = random.randint(0,99999)
  print(sifre)

elif uzunluk == 6:
  sifre = random.randint(0,999999)
  print(sifre)

elif uzunluk == 7:
  sifre = random.randint(0,9999999)
  print(sifre)

elif uzunluk == 8:
  sifre = random.randint(0,99999999)
  print(sifre)

elif uzunluk == 9:
  sifre = random.randint(0,99999999)
  print(sifre)

else:
  print("Geçersiz giriş.")
