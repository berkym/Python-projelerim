import random

print("Asistana hoş geldiniz!")
print("Sorunuzu sorabiilirsiniz")
print("")

cevaplar = ["Evet", "Hayir", "Olabilir", "Emin değilim", "Maalesef", "Kesinlikle", "Neden?", "Tamam", "Bilmiyorum", "Bunu söyleyemem", "Öyle düşünüyorum", "Kesinlikle!",
            "Neden olmasin", "Hayir bu imkansiz", "Olamaz", "O da ayni şeyi düşünüyor", "Bu mümkün değil", "Bu imkansiz", "Şanslisin", "Bunu denemelisin", "EVETT", "Aynen",
            "Bu gerçekleşecek", "Ne dediğinin farkinda misin", "Düşünme bile", "Bu gerçekleşecek", "Böyle bir şey mümkün değil", "Bu olacak", "Bu olmayacak", "Üzgünüm"]

while True:
    input("Sorunuz: ")
    secim = random.choice(cevaplar)
    print("Cevap:", secim)
