while True:

    sayilar_listesi = []
    
    while True:    
        sayi = input("Sayı gir: ")

        if sayi.isdigit(): #girilen input'un sayı mı değil mi kontrolü
            sayi = int(sayi)
        else:
            continue

        sayilar_listesi.append(sayi)

        devam = input("Çıkış için \"ç\" ye basınız.")

        if devam == "ç":
           break
    
    print(sayilar_listesi)

    islem = input("Hangi işlemi yapmak istiyorsunuz?(Toplama- 1, Çarpma- 2, Çıkarma- 3, Bölme- 4 giriniz)")

    if (islem == "1"):
        islem_yazili="Toplama"
        sonuc = 0
        for i in sayilar_listesi:
            sonuc = sonuc + i
 
    if (islem == "2"):
        islem_yazili="Çarpma"
        sonuc = 1
        for i in sayilar_listesi:
            sonuc = sonuc * i
    
    if (islem == "3"):
        islem_yazili="Çıkarma"
        sonuc = 0
        for i in sayilar_listesi:
            sonuc = sonuc - i
    
    if (islem == "4"):
        islem_yazili="Bölme"
        sonuc = sayilar_listesi[0]
        for i in range(1,len(sayilar_listesi)):
            sonuc = sonuc // sayilar_listesi[i] # verinin kendisini bölüyoruz. a

        # // olarak kullan. tam sayı şeklinde olsun .0 olmaz işlem sonucunda. 

    print(sonuc)
    print(f"{islem_yazili} işleminizin sonucu {sonuc} dur.")

    secim = input("İşlem yapmaya devam etmek istiyor musunuz? H/h: ") # Çıkmak için H/h ye basmamız gerekiyor.
    if(secim == "H" or secim == "h"): #işlem sonlanması için geçerli koşul
        break

