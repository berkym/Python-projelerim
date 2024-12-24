print("")
print("Döviz çevirme")
print("|Dolar = 1|Euro = 2|")
print("")

choice = input("Seçiminiz: ")
print("")

if choice == "1":
    dolar = 32.20
    print(f"1 Dolar: {dolar} Türk Lirası")
    amount = float(input("Çevirmek İstenen Miktarı giriniz: "))
    print("Türk Lirası:", amount * 32.20)

elif choice == "2":
    euro = 36.70
    print(f"1 Euro: {euro} Türk Lirası")
    amount = float(input("Çevirmek İstenen Miktarı giriniz: "))
    print("Türk Lirası:", amount * euro)
