print("Askerliğe uygun musunuz? Lütfen cevaplayınız: (Hayır için: H, Evet için: E)")

yas = int(input("Kaç yaşındasınız?: "))
if yas < 18 or yas > 41:
    print("Askerlik için uygun değilsiniz.")
else:
    boy = int(input("Boyunuz kaç cm?: "))
    if boy < 160:
        print("Askerlik için uygun değilsiniz.")
    else:
        kilo = int(input("Kaç kilosunuz?: "))
        if kilo < 50 or kilo > 100:
            print("Askerlik için uygun değilsiniz.")
        else:
            yaptinmi = input("Daha önce askerlik yaptınız mı?: ")
            if yaptinmi != "E" and yaptinmi != "H":
                print("Geçersiz giriş! Lütfen 'E' veya 'H' girin.")
            else:
                if yaptinmi == "E":
                    print("ASKER KAÇAĞI!!!")
                else:
                    vatandaslik = input("T.C Vatandaşlığınız var mı?: ")
                    if vatandaslik != "E" and vatandaslik != "H":
                        print("Geçersiz giriş! Lütfen 'E' veya 'H' girin.")
                    else:
                        if vatandaslik == "H":
                            print("Askerlik için uygun değilsiniz.")
                        elif vatandaslik == "E":
                            print("Askerlik için uygunsunuz!")
