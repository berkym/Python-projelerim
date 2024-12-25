import time

ayarlama = ["Taş", "Kağıt", "Makas"]

print("")
nick = input("Adınız nedir: ")
print(f"Taş, Kağıt, Makas oyununa hoşgeldin {nick}")
print("")
time.sleep(2)
print("Bota karşı oynacaksınız!")
time.sleep(2)

while True:

    choice = input("Sen: ").capitalize()

    if choice not in ayarlama:
            print("Geçersiz seçim! Lütfen 'Taş', 'Kağıt' veya 'Makas' yazın.")
            exit()

    answer = random.choice(ayarlama)
    print(f"Bot: {answer}")

    if choice == answer:
        print("Berabere!")

    elif (choice == "Taş" and answer == "Kağıt") or\
        (choice == "Kağıt" and answer == "Makas") or\
        (choice == "Makas" and answer == "Taş"):
        print("Kazandınız!")

    else:
        print("Kaybettiniz!")
