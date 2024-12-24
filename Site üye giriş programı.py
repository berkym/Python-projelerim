while True:
    print("Hoşgeldiniz")
    print("")
    username = input("Kullanıcı adınızı giriniz: ")
    password = input("Şifrenizi giriniz: ")

    if username == "admin" and password == "1234":
        print("")
        print(f"Hoşgeldin {username} Başarıyla giriş yaptınız.")
        print("")
        break
    else:
        print("")
        print("Kullanıcı adı veya şifre yanlış! Tekrar deneyiniz.")
        print("")
