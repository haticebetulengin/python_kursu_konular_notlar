
sayilar_listesi = []
while True:    
    sayi = int(input("Sayı gir: "))
    sayilar_listesi.append(sayi)
    devam = input("Çıkış için \"ç\" ye basınız.")
    if devam == "ç":
        break

print(sayilar_listesi)

