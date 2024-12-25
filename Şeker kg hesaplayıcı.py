print("1 KG şeker: 250TL.")
print("2 KG ve fazlası: 200TL.")
print("")
gram = float(input("Şeker kaç gram?: "))
kg = gram / 1000

print(f"[{gram} gram, {kg} kilograma eşittir.")

indirimli = kg * 200
indirimsiz = kg * 250

if kg > 2.0:
  print("Bu şeker 2 Kilodan büyük, Bu yüzden kilo başına 200TL alınacak.")
  print(f"Fiyat: {indirimli}")
if kg < 1.9:
  print("Bu şeker 2 Kilodan küçük, Bu yüzden kilo başına 250TL alınacak.")
  print(f"Fiyat: {indirimsiz}")

