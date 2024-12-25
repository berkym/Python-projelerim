while True:
    import random

    print("Zar atma programı")
    print("")
    print("|Tek: 1|Çift: 2|")

    doublesingle = input("Çift zar mı atmak istiyorsunuz Tek mi?: ")
    print("")

    if doublesingle == "1":
        zar = random.randint(1, 6)
        print("Zar:", zar)

    elif doublesingle == "2":
        zar1 = random.randint(1, 6)
        zar2 = random.randint(1, 6)
        print("Zar 1:", zar1)
        print("Zar 2:", zar2)
        print("Toplam:", zar1 + zar2)
        print("")
