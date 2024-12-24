import time

puan = 0

print("")
print("Ankete Hoşgeldiniz!")
ad = input("Adınızı giriniz: ")
print("Hoş geldin", ad, "Her seviyede 30 soru vardır.")
time.sleep(2)
print("")
print("Zorluk seviyesi seçiniz!")
print("|Başkent bilmece = 1 |Genel kültür = 2 |Savaş tarihleri = 3|")
print("")
seviye = int(input("Seviye numarasını giriniz: "))
print("")

if seviye == 1:
    print("Başkent bilmece seçildi! Test başlıyor...")
    time.sleep(4)
    print("")
    soru1 = input("Türkiye'nin başkenti neresidir?: ").lower()
    if soru1 == "ankara":
        print("Doğru bildiniz, puan eklendi!")
        puan += 1
    else:
        print("Yanlış cevap, puan eklenmedi!")
    print("Puanınız:", puan)
    time.sleep(1)
    print("")
    soru2 = input("Almanya'nın başkenti neresidir?: ").lower()
    if soru2 == "berlin":
        print("Doğru bildiniz, puan eklendi!")
        puan += 1
    else:
        print("Yanlış cevap, puan eklenmedi!")
    print("Puanınız:", puan)
    time.sleep(1)
    print("")
    soru3 = input("Suriye'nin başkenti neresidir?: ").lower()
    if soru3 == "şam" or soru3 == "damascus":
        print("Doğru bildiniz, puan eklendi!")
        puan += 1
    else:
        print("Yanlış cevap, puan eklenmedi!")
    print("Puanınız:", puan)
    time.sleep(1)
    print("")
    soru4 = input("İngiltere'nin başkenti neresidir?: ").lower()
    if soru4 == "londra" or soru4 == "london":
        print("Doğru bildiniz, puan eklendi!")
        puan += 1
    else:
        print("Yanlış cevap, puan eklenmedi!")
    print("Puanınız:", puan)
    time.sleep(1)
    print("")
    soru5 = input("Amerika'nın başkenti neresidir?: ").lower()
    if soru5 == "washington" or soru5 == "washington dc":
        print("Doğru bildiniz, puan eklendi!")
        puan += 1
    else:
        print("Yanlış cevap, puan eklenmedi!")
    print("Puanınız:", puan)
    time.sleep(1)
    print("")
    soru6 = input("Fransa'nın başkenti neresidir?: ").lower()
    if soru6 == "paris":
        print("Doğru bildiniz, puan eklendi!")
        puan += 1
    else:
        print("Yanlış cevap, puan eklenmedi!")
    print("Puanınız:", puan)
    time.sleep(1)
    print("")
    soru7 = input("Japonya'nın başkenti neresidir?: ").lower()
    if soru7 == "tokyo":
        print("Doğru bildiniz, puan eklendi!")
        puan += 1
    else:
        print("Yanlış cevap, puan eklenmedi!")
    print("Puanınız:", puan)
    time.sleep(1)
    print("")
    soru8 = input("İtalya'nın başkenti neresidir?: ").lower()
    if soru8 == "roma" or soru8 == "rome":
        print("Doğru bildiniz, puan eklendi!")
        puan += 1
    else:
        print("Yanlış cevap, puan eklenmedi!")
    print("Puanınız:", puan)
    time.sleep(1)
    print("")
    soru9 = input("Rusya'nın başkenti neresidir?: ").lower()
    if soru9 == "moskova" or soru9 == "moscow":
        print("Doğru bildiniz, puan eklendi!")
        puan += 1
    else:
        print("Yanlış cevap, puan eklenmedi!")
    print("Puanınız:", puan)
    time.sleep(1)
    print("")
    soru10 = input("Azerbaycan'ın başkenti neresidir?: ").lower()
    if soru10 == "bakü" or soru10 == "baku":
        print("Doğru bildiniz, puan eklendi!")
        puan += 1
    else:
        print("Yanlış cevap, puan eklenmedi!")
    print("Puanınız:", puan)
    time.sleep(1)
    print("")
    soru11 = input("Ukrayna'nın başkenti neresidir?: ").lower()
    if soru11 == "kiev" or soru11 == "kyiv":
        print("Doğru bildiniz, puan eklendi!")
        puan += 1
    else:
        print("Yanlış cevap, puan eklenmedi!")
    print("Puanınız:", puan)
    time.sleep(1)
    print("")
    soru12 = input("Çin'in başkenti neresidir?: ").lower()
    if soru12 == "pekin" or soru12 == "beijing":
        print("Doğru bildiniz, puan eklendi!")
        puan += 1
    else:
        print("Yanlış cevap, puan eklenmedi!")
    print("Puanınız:", puan)
    time.sleep(1)
    print("")
    soru13 = input("İsvec'in başkenti neresidir?: ").lower()
    if soru13 == "stockholm":
        print("Doğru bildiniz, puan eklendi!")
        puan += 1
    else:
        print("Yanlış cevap, puan eklenmedi!")
    print("Puanınız:", puan)
    time.sleep(1)
    print("")
    soru14 = input("Irak'ın başkenti neresidir?: ").lower()
    if soru14 == "bağdat" or soru14 == "baghdad":
        print("Doğru bildiniz, puan eklendi!")
        puan += 1
    else:
        print("Yanlış cevap, puan eklenmedi!")
    print("Puanınız:", puan)
    time.sleep(1)
    print("")
    soru15 = input("Tayland'ın başkenti neresidir?: ").lower()
    if soru15 == "bangkok":
        print("Doğru bildiniz, puan eklendi!")
        puan += 1
    else:
        print("Yanlış cevap, puan eklenmedi!")
    print("Puanınız:", puan)
    time.sleep(1)
    print("")
    soru16 = input("Brezilya'nın başkenti neresidir?: ").lower()
    if soru16 == "brasilia":
        print("Doğru bildiniz, puan eklendi!")
        puan += 1
    else:
        print("Yanlış cevap, puan eklenmedi!")
    print("Puanınız:", puan)
    time.sleep(1)
    print("")
    soru17 = input("Yunanistan'ın başkenti neresidir?: ").lower()
    if soru17 == "atina" or soru17 == "athens":
        print("Doğru bildiniz, puan eklendi!")
        puan += 1
    else:
        print("Yanlış cevap, puan eklenmedi!")
    print("Puanınız:", puan)
    time.sleep(1)
    print("")
    soru18 = input("Ermenistan'ın başkenti neresidir?: ").lower()
    if soru18 == "erivan" or soru18 == "yerevan":
        print("Doğru bildiniz, puan eklendi!")
        puan += 1
    else:
        print("Yanlış cevap, puan eklenmedi!")
    print("Puanınız:", puan)
    time.sleep(1)
    print("")
    soru19 = input("Finlandiya'nın başkenti neresidir?: ").lower()
    if soru19 == "helsinki":
        print("Doğru bildiniz, puan eklendi!")
        puan += 1
    else:
        print("Yanlış cevap, puan eklenmedi!")
    print("Puanınız:", puan)
    time.sleep(1)
    print("")
    soru20 = input("Avusturya'nın başkenti neresidir?: ").lower()
    if soru20 == "viyana" or soru20 == "vienna":
        print("Doğru bildiniz, puan eklendi!")
        puan += 1
    else:
        print("Yanlış cevap, puan eklenmedi!")
    print("Puanınız:", puan)
    time.sleep(1)
    print("")
    soru21 = input("İspanya'nın başkenti neresidir?: ").lower()
    if soru21 == "madrid":
        print("Doğru bildiniz, puan eklendi!")
        puan += 1
    else:
        print("Yanlış cevap, puan eklenmedi!")
    print("Puanınız:", puan)
    time.sleep(1)
    print("")
    soru22 = input("Özbekistan'ın başkenti neresidir?: ").lower()
    if soru22 == "taşkent" or soru22 == "tashkent":
        print("Doğru bildiniz, puan eklendi!")
        puan += 1
    else:
        print("Yanlış cevap, puan eklenmedi!")
    print("Puanınız:", puan)
    time.sleep(1)
    print("")
    soru23 = input("Norveç'in başkenti neresidir?: ").lower()
    if soru23 == "oslo":
        print("Doğru bildiniz, puan eklendi!")
        puan += 1
    else:
        print("Yanlış cevap, puan eklenmedi!")
    print("Puanınız:", puan)
    time.sleep(1)
    print("")
    soru24 = input("Pakistan'ın başkenti neresidir?: ").lower()
    if soru24 == "islamabad":
        print("Doğru bildiniz, puan eklendi!")
        puan += 1
    else:
        print("Yanlış cevap, puan eklenmedi!")
    print("Puanınız:", puan)
    time.sleep(1)
    print("")
    soru25 = input("Hollanda'nın başkenti neresidir?: ").lower()
    if soru25 == "amsterdam":
        print("Doğru bildiniz, puan eklendi!")
        puan += 1
    else:
        print("Yanlış cevap, puan eklenmedi!")
    print("Puanınız:", puan)
    time.sleep(1)
    print("")
    soru26 = input("Portekiz'in başkenti neresidir?: ").lower()
    if soru26 == "lizbon" or soru26 == "lisbon":
        print("Doğru bildiniz, puan eklendi!")
        puan += 1
    else:
        print("Yanlış cevap, puan eklenmedi!")
    print("Puanınız:", puan)
    time.sleep(1)
    print("")
    soru27 = input("Polonya'nın başkenti neresidir?: ").lower()
    if soru27 == "varşova" or soru27 == "warsaw":
        print("Doğru bildiniz, puan eklendi!")
        puan += 1
    else:
        print("Yanlış cevap, puan eklenmedi!")
    print("Puanınız:", puan)
    time.sleep(1)
    print("")
    soru28 = input("Vietnam'ın başkenti neresidir?: ").lower()
    if soru28 == "hanoi":
        print("Doğru bildiniz, puan eklendi!")
        puan += 1
    else:
        print("Yanlış cevap, puan eklenmedi!")
    print("Puanınız:", puan)
    time.sleep(1)
    print("")
    soru29 = input("Endonezya'nın başkenti neresidir?: ").lower()
    if soru29 == "cakarta" or soru29 == "jakarta":
        print("Doğru bildiniz, puan eklendi!")
        puan += 1
    else:
        print("Yanlış cevap, puan eklenmedi!")
    print("Puanınız:", puan)
    time.sleep(1)
    print("")
    soru30 = input("Cezayir'in başkenti neresidir?: ").lower()
    if soru30 == "cezayir" or soru30 == "Algiers":
        print("Doğru bildiniz, puan eklendi!")
        puan += 1
    else:
        print("Yanlış cevap, puan eklenmedi!")
    print("Puanınız:", puan)
    time.sleep(1)
    print("")
    print("")
    print("Anketi tamamladınız! Toplam puanınız:", puan)

    if puan < 15:
        print("Başkent bilginizi geliştirmenizi öneririz!")
    elif 15 <= puan <= 25:
        print("Başkent bilginiz ortalama seviyededir. Tebrikler!")
    else:
        print("Siz bir deha olmalısınız! Harika bir Başkent bilgisi!")
    print("")
elif seviye == 2:
    print("Genel kültür testi seçildi! Test başlıyor...")
    time.sleep(4)
    print("")
    soru1 = input("Dünyadaki en büyük ülke hangi ülkedir?: ").lower()
    if soru1 == "rusya":
        print("Doğru bildiniz, puan eklendi!")
        puan += 1
    else:
        print("Yanlış cevap, puan eklenmedi!")
    print("Puanınız:", puan)
    time.sleep(1)
    print("")
    soru2 = input("Nobel Ödülü ilk kez hangi alanda verildi?: ").lower()
    if soru2 == "fizik":
        print("Doğru bildiniz, puan eklendi!")
        puan += 1
    else:
        print("Yanlış cevap, puan eklenmedi!")
    print("Puanınız:", puan)
    time.sleep(1)
    print("")
    soru3 = input("Dünya üzerindeki en yüksek dağ zirvesi hangisidir?: ").lower()
    if soru3 == "everest":
        print("Doğru bildiniz, puan eklendi!")
        puan += 1
    else:
        print("Yanlış cevap, puan eklenmedi!")
    print("Puanınız:", puan)
    time.sleep(1)
    print("")
    soru4 = input("Türkiye'nin en kalabalık ili hangisidir?: ").lower()
    if soru4 == "istanbul":
        print("Doğru bildiniz, puan eklendi!")
        puan += 1
    else:
        print("Yanlış cevap, puan eklenmedi!")
    print("Puanınız:", puan)
    time.sleep(1)
    print("")
    soru5 = input("Dünya üzerinde en fazla konuşulan dil hangisidir?: ").lower()
    if soru5 == "çince":
        print("Doğru bildiniz, puan eklendi!")
        puan += 1
    else:
        print("Yanlış cevap, puan eklenmedi!")
    print("Puanınız:", puan)
    time.sleep(1)
    print("")
    soru6 = input("Türkiye'nin en büyük şehri hangisidir?: ").lower()
    if soru6 == "konya":
        print("Doğru bildiniz, puan eklendi!")
        puan += 1
    else:
        print("Yanlış cevap, puan eklenmedi!")
    print("Puanınız:", puan)
    time.sleep(1)
    print("")
    soru7 = input("Atatürk'ün tam adı nedir?: ").lower()
    if soru7 == "mustafa kemal atatürk":
        print("Doğru bildiniz, puan eklendi!")
        puan += 1
    else:
        print("Yanlış cevap, puan eklenmedi!")
    print("Puanınız:", puan)
    time.sleep(1)
    print("")
    soru8 = input("Dünya üzerindeki en büyük çöl hangisidir?: ").lower()
    if soru8 == "sahra çölü":
        print("Doğru bildiniz, puan eklendi!")
        puan += 1
    else:
        print("Yanlış cevap, puan eklenmedi!")
    print("Puanınız:", puan)
    time.sleep(1)
    print("")
    soru9 = input("Dünyanın en yüksek gökdeleni neresidir: ").lower()
    if soru9 == "burj khalifa":
        print("Doğru bildiniz, puan eklendi!")
        puan += 1
    else:
        print("Yanlış cevap, puan eklenmedi!")
    print("Puanınız:", puan)
    time.sleep(1)
    print("")
    soru10 = input("Buzullarla kaplı kıta hangisidir?: ").lower()
    if soru10 == "antartika":
        print("Doğru bildiniz, puan eklendi!")
        puan += 1
    else:
        print("Yanlış cevap, puan eklenmedi!")
    print("Puanınız:", puan)
    time.sleep(1)
    print("")
    soru11 = input("Fransa'nın sembolü olan ve dünya üzerinde en çok bilinen kulesi hangisidir?: ").lower()
    if soru11 == "eyfel" or soru11 == "eiffel":
        print("Doğru bildiniz, puan eklendi!")
        puan += 1
    else:
        print("Yanlış cevap, puan eklenmedi!")
    print("Puanınız:", puan)
    time.sleep(1)
    print("")
    soru12 = input("Dünyanın en büyük petrol rezervine sahip ülkesi hangisidir?: ").lower()
    if soru12 == "suudi arabistan":
        print("Doğru bildiniz, puan eklendi!")
        puan += 1
    else:
        print("Yanlış cevap, puan eklenmedi!")
    print("Puanınız:", puan)
    time.sleep(1)
    print("")
    soru13 = input("Dünyada en çok kullanılan para birimi hangisidir?: ").lower()
    if soru13 == "amerikan doları":
        print("Doğru bildiniz, puan eklendi!")
        puan += 1
    else:
        print("Yanlış cevap, puan eklenmedi!")
    print("Puanınız:", puan)
    time.sleep(1)
    print("")
    soru14 = input("Türkiye'nin en büyük gölü hangisidir?: ").lower()
    if soru14 == "van gölü":
        print("Doğru bildiniz, puan eklendi!")
        puan += 1
    else:
        print("Yanlış cevap, puan eklenmedi!")
    print("Puanınız:", puan)
    time.sleep(1)
    print("")
    soru15 = input("Türkiye'nin en yüksek dağı hangisidir?: ").lower()
    if soru15 == "ağrı dağı":
        print("Doğru bildiniz, puan eklendi!")
        puan += 1
    else:
        print("Yanlış cevap, puan eklenmedi!")
    print("Puanınız:", puan)
    time.sleep(1)
    print("")
    soru16 = input("Dünyanın en derin yeri neresidir?: ").lower()
    if soru16 == "mariana çukuru":
        print("Doğru bildiniz, puan eklendi!")
        puan += 1
    else:
        print("Yanlış cevap, puan eklenmedi!")
    print("Puanınız:", puan)
    time.sleep(1)
    print("")
    soru17 = input("Dünyanın en büyük okyanusu hangisidir?: ").lower()
    if soru17 == "pasifik okyanusu":
        print("Doğru bildiniz, puan eklendi!")
        puan += 1
    else:
        print("Yanlış cevap, puan eklenmedi!")
    print("Puanınız:", puan)
    time.sleep(1)
    print("")
    soru18 = input("İlk Türk kadın pilot kimdir?: ").lower()
    if soru18 == "sabiha gökçen":
        print("Doğru bildiniz, puan eklendi!")
        puan += 1
    else:
        print("Yanlış cevap, puan eklenmedi!")
    print("Puanınız:", puan)
    time.sleep(1)
    print("")
    soru19 = input("İnsan vücudundaki en büyük organ hangisidir?: ").lower()
    if soru19 == "deri":
        print("Doğru bildiniz, puan eklendi!")
        puan += 1
    else:
        print("Yanlış cevap, puan eklenmedi!")
    print("Puanınız:", puan)
    time.sleep(1)
    print("")
    soru20 = input("Bir yılın en kısa günü hangi tarihte yaşanır?: ").lower()
    if soru20 == "21 aralık":
        print("Doğru bildiniz, puan eklendi!")
        puan += 1
    else:
        print("Yanlış cevap, puan eklenmedi!")
    print("Puanınız:", puan)
    time.sleep(1)
    print("")
    soru21 = input("Hangi gezegen halkalarıyla ünlüdür?: ").lower()
    if soru21 == "satürn":
        print("Doğru bildiniz, puan eklendi!")
        puan += 1
    else:
        print("Yanlış cevap, puan eklenmedi!")
    print("Puanınız:", puan)
    time.sleep(1)
    print("")
    soru22 = input("İlk elektrikli ampulü icat eden kimdir?: ").lower()
    if soru22 == "thomas edison":
        print("Doğru bildiniz, puan eklendi!")
        puan += 1
    else:
        print("Yanlış cevap, puan eklenmedi!")
    print("Puanınız:", puan)
    time.sleep(1)
    print("")
    soru23 = input("Hangi spor dalında 'slam dunk' terimi kullanılır?: ").lower()
    if soru23 == "basketbol":
        print("Doğru bildiniz, puan eklendi!")
        puan += 1
    else:
        print("Yanlış cevap, puan eklenmedi!")
    print("Puanınız:", puan)
    time.sleep(1)
    print("")
    soru24 = input("Hangi gezegen Güneş Sistemi'ndeki en küçük gezegendir?: ").lower()
    if soru24 == "merkür":
        print("Doğru bildiniz, puan eklendi!")
        puan += 1
    else:
        print("Yanlış cevap, puan eklenmedi!")
    print("Puanınız:", puan)
    time.sleep(1)
    print("")
    soru25 = input("Türk Lirası'nın alt birimine ne ad verilir?: ").lower()
    if soru25 == "kuruş":
        print("Doğru bildiniz, puan eklendi!")
        puan += 1
    else:
        print("Yanlış cevap, puan eklenmedi!")
    print("Puanınız:", puan)
    time.sleep(1)
    print("")
    soru26 = input("Osmanlı Devleti'nin ilk padişahı kimdir?: ").lower()
    if soru26 == "osman gazi":
        print("Doğru bildiniz, puan eklendi!")
        puan += 1
    else:
        print("Yanlış cevap, puan eklenmedi!")
    print("Puanınız:", puan)
    time.sleep(1)
    print("")
    soru27 = input("Avrupa'nın en kalabalık ülkesi hangisidir?: ").lower()
    if soru27 == "almanya":
        print("Doğru bildiniz, puan eklendi!")
        puan += 1
    else:
        print("Yanlış cevap, puan eklenmedi!")
    print("Puanınız:", puan)
    time.sleep(1)
    print("")
    soru28 = input("Dünyanın en hızlı kara hayvanı hangisidir?: ").lower()
    if soru28 == "çita":
        print("Doğru bildiniz, puan eklendi!")
        puan += 1
    else:
        print("Yanlış cevap, puan eklenmedi!")
    print("Puanınız:", puan)
    time.sleep(1)
    print("")
    soru29 = input("İstanbul'un fethi hangi tarihte gerçekleşmiştir?: ").lower()
    if soru29 == "29 mayıs 1453":
        print("Doğru bildiniz, puan eklendi!")
        puan += 1
    else:
        print("Yanlış cevap, puan eklenmedi!")
    print("Puanınız:", puan)
    time.sleep(1)
    print("")
    soru30 = input("Hangi şehir 'Ebedi Şehir' olarak bilinir?: ").lower()
    if soru30 == "roma":
        print("Doğru bildiniz, puan eklendi!")
        puan += 1
    else:
        print("Yanlış cevap, puan eklenmedi!")
    print("Puanınız:", puan)
    time.sleep(1)
    print("")
    print("")
    print("Anketi tamamladınız! Toplam puanınız:", puan)

    if puan < 15:
        print("Genel kültür seviyenizi geliştirmenizi öneririz!")
    elif 15 <= puan <= 25:
        print("Genel kültür seviyeniz ortalama seviyededir. Tebrikler!")
    else:
        print("Siz bir deha olmalısınız! Harika bir genel kültür seviyesi!")
    print("")
elif seviye == 3:
    print("Savaş tarihleri testi seçildi! Test başlıyor...")
    time.sleep(4)
    print("")

    soru1 = input("I. Dünya Savaşı hangi tarihte başlamıştır?: ").lower()
    if soru1 == "1914":
        print("Doğru bildiniz, puan eklendi!")
        puan += 1
    else:
        print("Yanlış cevap, puan eklenmedi!")
    print("Puanınız:", puan)
    time.sleep(1)
    print("")
    soru2 = input("II. Dünya Savaşı hangi tarihte sona ermiştir?: ").lower()
    if soru2 == "1945":
        print("Doğru bildiniz, puan eklendi!")
        puan += 1
    else:
        print("Yanlış cevap, puan eklenmedi!")
    print("Puanınız:", puan)
    time.sleep(1)
    print("")
    soru3 = input("Malazgirt Meydan Muharebesi hangi tarihte yapılmıştır?: ").lower()
    if soru3 == "1071":
        print("Doğru bildiniz, puan eklendi!")
        puan += 1
    else:
        print("Yanlış cevap, puan eklenmedi!")
    print("Puanınız:", puan)
    time.sleep(1)
    print("")
    soru4 = input("Waterloo Savaşı hangi tarihte yapılmıştır?: ").lower()
    if soru4 == "1815":
        print("Doğru bildiniz, puan eklendi!")
        puan += 1
    else:
        print("Yanlış cevap, puan eklenmedi!")
    print("Puanınız:", puan)
    time.sleep(1)
    print("")
    soru5 = input("Kurtuluş Savaşı hangi yıl başlamıştır?: ").lower()
    if soru5 == "1919":
        print("Doğru bildiniz, puan eklendi!")
        puan += 1
    else:
        print("Yanlış cevap, puan eklenmedi!")
    print("Puanınız:", puan)
    time.sleep(1)
    print("")
    soru6 = input("Vietnam Savaşı hangi tarihte sona ermiştir?: ").lower()
    if soru6 == "1975":
        print("Doğru bildiniz, puan eklendi!")
        puan += 1
    else:
        print("Yanlış cevap, puan eklenmedi!")
    print("Puanınız:", puan)
    time.sleep(1)
    print("")
    soru7 = input("Truva Savaşı'nın tahmini başlangıç yılı nedir?: ").lower()
    if soru7 == "m.ö. 1200" or soru7 == "m.ö.1200":
        print("Doğru bildiniz, puan eklendi!")
        puan += 1
    else:
        print("Yanlış cevap, puan eklenmedi!")
    print("Puanınız:", puan)
    time.sleep(1)
    print("")
    soru8 = input("Mohaç Meydan Muharebesi hangi tarihte yapılmıştır?: ").lower()
    if soru8 == "1526":
        print("Doğru bildiniz, puan eklendi!")
        puan += 1
    else:
        print("Yanlış cevap, puan eklenmedi!")
    print("Puanınız:", puan)
    time.sleep(1)
    print("")
    soru9 = input("Çanakkale Savaşı hangi tarihte başlamıştır?: ").lower()
    if soru9 == "1915":
        print("Doğru bildiniz, puan eklendi!")
        puan += 1
    else:
        print("Yanlış cevap, puan eklenmedi!")
    print("Puanınız:", puan)
    time.sleep(1)
    print("")
    soru10 = input("Napolyon'un Rusya Seferi hangi yıl gerçekleşmiştir?: ").lower()
    if soru10 == "1812":
        print("Doğru bildiniz, puan eklendi!")
        puan += 1
    else:
        print("Yanlış cevap, puan eklenmedi!")
    print("Puanınız:", puan)
    time.sleep(1)
    print("")
    soru11 = input("Persler ile Yunanlılar arasında yapılan Maraton Savaşı hangi tarihte gerçekleşmiştir?: ").lower()
    if soru11 == "m.ö. 490":
        print("Doğru bildiniz, puan eklendi!")
        puan += 1
    else:
        print("Yanlış cevap, puan eklenmedi!")
    print("Puanınız:", puan)
    time.sleep(1)
    print("")
    soru12 = input("II. Balkan Savaşı hangi yıl başlamıştır?: ").lower()
    if soru12 == "1913":
        print("Doğru bildiniz, puan eklendi!")
        puan += 1
    else:
        print("Yanlış cevap, puan eklenmedi!")
    print("Puanınız:", puan)
    time.sleep(1)
    print("")
    soru13 = input("Peleponnes Savaşları hangi tarihler arasında yapılmıştır?: ").lower()
    if soru13 == "m.ö. 431-404":
        print("Doğru bildiniz, puan eklendi!")
        puan += 1
    else:
        print("Yanlış cevap, puan eklenmedi!")
    print("Puanınız:", puan)
    time.sleep(1)
    print("")
    soru14 = input("Hastings Savaşı hangi tarihte gerçekleşmiştir?: ").lower()
    if soru14 == "1066":
        print("Doğru bildiniz, puan eklendi!")
        puan += 1
    else:
        print("Yanlış cevap, puan eklenmedi!")
    print("Puanınız:", puan)
    time.sleep(1)
    print("")
    soru15 = input("Haçlı Seferleri hangi tarihte başlamıştır?: ").lower()
    if soru15 == "1096":
        print("Doğru bildiniz, puan eklendi!")
        puan += 1
    else:
        print("Yanlış cevap, puan eklenmedi!")
    print("Puanınız:", puan)
    time.sleep(1)
    print("")
    soru16 = input("Yüz Yıl Savaşları hangi tarihler arasında yapılmıştır?: ").lower()
    if soru16 == "1337-1453":
        print("Doğru bildiniz, puan eklendi!")
        puan += 1
    else:
        print("Yanlış cevap, puan eklenmedi!")
    print("Puanınız:", puan)
    time.sleep(1)
    print("")
    soru17 = input("Austerlitz Savaşı hangi yıl gerçekleşmiştir?: ").lower()
    if soru17 == "1805":
        print("Doğru bildiniz, puan eklendi!")
        puan += 1
    else:
        print("Yanlış cevap, puan eklenmedi!")
    print("Puanınız:", puan)
    time.sleep(1)
    print("")
    soru18 = input("Ankara Savaşı hangi tarihte yapılmıştır?: ").lower()
    if soru18 == "1402":
        print("Doğru bildiniz, puan eklendi!")
        puan += 1
    else:
        print("Yanlış cevap, puan eklenmedi!")
    print("Puanınız:", puan)
    time.sleep(1)
    print("")
    soru19 = input("Kırım Savaşı hangi tarihler arasında yapılmıştır?: ").lower()
    if soru19 == "1853-1856":
        print("Doğru bildiniz, puan eklendi!")
        puan += 1
    else:
        print("Yanlış cevap, puan eklenmedi!")
    print("Puanınız:", puan)
    time.sleep(1)
    print("")
    soru20 = input("Kore Savaşı hangi tarihler arasında yapılmıştır?: ").lower()
    if soru20 == "1950-1953":
        print("Doğru bildiniz, puan eklendi!")
        puan += 1
    else:
        print("Yanlış cevap, puan eklenmedi!")
    print("Puanınız:", puan)
    time.sleep(1)
    print("")
    soru21 = input("Fetret Devri hangi tarihte başlamıştır?: ").lower()
    if soru21 == "1402":
        print("Doğru bildiniz, puan eklendi!")
        puan += 1
    else:
        print("Yanlış cevap, puan eklenmedi!")
    print("Puanınız:", puan)
    time.sleep(1)
    print("")
    soru22 = input("Roma'nın Kartaca'ya karşı kazandığı Zama Savaşı hangi tarihte yapılmıştır?: ").lower()
    if soru22 == "m.ö. 202":
        print("Doğru bildiniz, puan eklendi!")
        puan += 1
    else:
        print("Yanlış cevap, puan eklenmedi!")
    print("Puanınız:", puan)
    time.sleep(1)
    print("")
    soru23 = input("Bizans İmparatorluğu'nun yıkıldığı tarih nedir?: ").lower()
    if soru23 == "1453":
        print("Doğru bildiniz, puan eklendi!")
        puan += 1
    else:
        print("Yanlış cevap, puan eklenmedi!")
    print("Puanınız:", puan)
    time.sleep(1)
    print("")
    soru24 = input("III. Haçlı Seferi hangi tarihte sona ermiştir?: ").lower()
    if soru24 == "1192":
        print("Doğru bildiniz, puan eklendi!")
        puan += 1
    else:
        print("Yanlış cevap, puan eklenmedi!")
    print("Puanınız:", puan)
    time.sleep(1)
    print("")
    soru25 = input("Büyük Selçuklu Devleti'nin kazandığı Dandanakan Savaşı hangi tarihte yapılmıştır?: ").lower()
    if soru25 == "1040":
        print("Doğru bildiniz, puan eklendi!")
        puan += 1
    else:
        print("Yanlış cevap, puan eklenmedi!")
    print("Puanınız:", puan)
    time.sleep(1)
    print("")
    soru26 = input("Osmanlı'nın Viyana Kuşatması hangi tarihte başarısız olmuştur?: ").lower()
    if soru26 == "1683":
        print("Doğru bildiniz, puan eklendi!")
        puan += 1
    else:
        print("Yanlış cevap, puan eklenmedi!")
    print("Puanınız:", puan)
    time.sleep(1)
    print("")
    soru27 = input("Alparslan'ın kazandığı Pasinler Savaşı hangi tarihte yapılmıştır?: ").lower()
    if soru27 == "1048":
        print("Doğru bildiniz, puan eklendi!")
        puan += 1
    else:
        print("Yanlış cevap, puan eklenmedi!")
    print("Puanınız:", puan)
    time.sleep(1)
    print("")
    soru28 = input("Fransız İhtilali'nin başlangıç tarihi nedir?: ").lower()
    if soru28 == "1789":
        print("Doğru bildiniz, puan eklendi!")
        puan += 1
    else:
        print("Yanlış cevap, puan eklenmedi!")
    print("Puanınız:", puan)
    time.sleep(1)
    print("")
    soru29 = input("Berlin Duvarı hangi tarihte yıkılmıştır?: ").lower()
    if soru29 == "1989":
        print("Doğru bildiniz, puan eklendi!")
        puan += 1
    else:
        print("Yanlış cevap, puan eklenmedi!")
    print("Puanınız:", puan)
    time.sleep(1)
    print("")
    soru30 = input("Osmanlı Devleti'nin katıldığı ilk savaşı olan Koyunhisar Savaşı hangi tarihte yapılmıştır?: ").lower()
    if soru30 == "1302":
        print("Doğru bildiniz, puan eklendi!")
        puan += 1
    else:
        print("Yanlış cevap, puan eklenmedi!")
    print("Puanınız:", puan)
    time.sleep(1)
    print("")

    print("")
    print("Anketi tamamladınız! Toplam puanınız:", puan)

    if puan < 15:
        print("Genel kültür seviyenizi geliştirmenizi öneririz!")
    elif 15 <= puan <= 25:
        print("Genel kültür seviyeniz ortalama seviyededir. Tebrikler!")
    else:
        print("Siz bir deha olmalısınız! Harika bir genel kültür seviyesi!")
    print("")
else:
    print("Hatalı giriş. Tekrar deneyiniz!")
