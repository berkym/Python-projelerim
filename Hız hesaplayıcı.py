print("Bu program girdiğiniz Mil'leri Kilometre'ye dönüştürür.")

mil = float(input("Hızınız kaç mil?: "))
km = mil * 1.6

print(f"Hızınız: {km}")

if km > 100:
  print("Hızınız 100'ü geçmiş durumda, lütfen yavaşlayınız.")
