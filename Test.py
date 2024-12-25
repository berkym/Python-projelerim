print("Teste hoşgeldiniz. Her soru 1 puan değerindedir.")

dogru_sayac = 0
soru_sayac = 0
sorular = ["Gökküşağının kaç rengi var?: ", "Hangi dili öğreniyorsunuz?: ", "Osmanlı Devleti hangi yılda kurulmuştur?: ", "Malazgirt savaşı hangi yılda olmuştur?: ", "Atatürkün doğum tarihi ne zamandır?: "]
dogru_cevaplar = ["7", "python", "1299", "1071", "1881"]

while soru_sayac < len(sorular):
  cevap = input(sorular[soru_sayac])
  if cevap.lower() == dogru_cevaplar[soru_sayac]:
    dogru_sayac += 1
    soru_sayac += 1

  if dogru_sayac >= 5:
    print("Tebrikler, 5 soruda 5 doğru.")
  else:
    print("Puanınız:", dogru_sayac)
