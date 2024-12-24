print("Hoşgeldiniz")
print("")

kartno = 1234
money = 250

number = int(input("Kartınızın numarasını giriniz: "))

if number == kartno:
    print("")
    print("Başarıyla giriş yapıldı")
    print("")
    print("Seçim yapınız")
    print("|Para çekme = 1|Para yatırma = 2|Bakiye sorgulama = 3|")
    print("")

    choice = input("Seçiminiz: ").lower()
    if choice == "1":
        cekim = int(input("Ne kadar çekmek istiyorsunuz: "))
        if cekim > money:
            print("Yetersiz bakiye")
            print("")
        elif cekim < money:
            money -= cekim
            print(f"{cekim}TL çekildi kalan bakiyeniz: {money}TL")
            print("")

    elif choice == "2":
        yatirma = int(input("Ne kadar yatırmak istiyorsunuz: "))
        toplam = (yatirma + money)
        print(f"{yatirma}TL yatırıldı, yeni bakiyeniz: {toplam}TL")
        print("")

    elif choice == "3":
        print(f"Bakiyeniz: {money}TL")
        print("")
