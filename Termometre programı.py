print("Termometre programına Hoşgeldiniz")

sicaklik = int(input("Hava şu anda kaç derece?: "))
if sicaklik < 15:
    print("Hava soğuk")
elif sicaklik > 15 and sicaklik < 26:
    print("Hava Ilık")
else:
    print("Hava sıcak")
