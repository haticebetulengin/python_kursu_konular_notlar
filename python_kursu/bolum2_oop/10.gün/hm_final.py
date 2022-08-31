def islem_secenegi():
    islem = input("Hangi işlemi yapmak istiyorsunuz?(Toplama- 1, Çarpma- 2, Çıkarma- 3, Bölme- 4 giriniz)")
    return islem

def cikis_kontrol():
    devam = input("Çıkış için \"ç\" ye basınız.")
    return devam #çıkış yapmak istiyor muyuz istemiyor muyuz kaydetmemiz gerek.

def veri_girisi():
    sayilar_listesi = []
    while True:  
        sayi = input("Veri gir: ")

        kontrol = veri_giris_kontrol(sayi)
        print(kontrol)
        print(type(kontrol))
        
        if (kontrol == 1):
            sayi = int(sayi)
            sayilar_listesi.append(sayi)
        else:
            print("Yanlış veri girdiniz.")
            continue

        devam = cikis_kontrol() # üstteki fonksiyonu çağırıyoruz. kaydettiğimiz değeri devam'a atıyoruz.
        print(devam)
        print(type(devam))
        if (devam == "ç"): # kaydedilip devam'a atılan değer "ç" ye eşitse döngüyü kırıyoruz.
            break
    print(sayilar_listesi)
    return sayilar_listesi

def veri_giris_kontrol(veri): 
    if veri.isdigit(): #girilen input'un sayı mı değil mi kontrolü
        return 1 # veri dönüştürülebilir
    else:
        return 0 # veri dönüştürülemez. 
        
def toplama(sayilar_listesi): #gelen verinin liste biçiminde olduğunu biliyoruz, ona göre kodlamayı yaptık.
    if type(sayilar_listesi) == type(list()):   
        sonuc = 0
        for i in sayilar_listesi:
            sonuc = sonuc + i
    print(f"Toplama işleminin sonucu {sonuc} tur.")

def cikarma(sayilar_listesi):
    sonuc = 0
    for i in sayilar_listesi:
        sonuc = sonuc - i
    print(f"Çıkarma işleminin sonucu {sonuc} tur.")

def carpma(sayilar_listesi):
    sonuc = 1
    for i in sayilar_listesi:
        sonuc = sonuc * i
    print(f"Çarpma işleminin sonucu {sonuc} tur.")

def bolme(sayilar_listesi): #gelen verinin liste biçiminde olduğunu biliyoruz, ona göre kodlamayı yaptık.
    sonuc = sayilar_listesi[0]
    for i in range(1,len(sayilar_listesi)):
        sonuc = sonuc // sayilar_listesi[i] # verinin kendisini bölüyoruz. a
        # // olarak kullan. tam sayı şeklinde olsun .0 olmaz işlem sonucunda. 
    print(f"Bölme işleminin sonucu {sonuc} tur.")

def us_al():
    pass

def main():
    secenek = islem_secenegi()
    veriler = veri_girisi()
    match secenek:
        case "1":
            toplama(veriler)
        case "2":
            cikarma(veriler)
        case "3":
            carpma(veriler)
        case "4":
            bolme(veriler)
        case "5":
            us_al(veriler)
        case _:
            print("Yanlış seçim yaptınız")


if __name__ == "__main__":
    main()