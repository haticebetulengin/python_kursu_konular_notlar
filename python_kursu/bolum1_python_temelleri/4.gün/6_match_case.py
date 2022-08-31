# match değişken:
#       case değişken_değeri:
#           kodlar
#       cade değişken_değeri2:
#           kodlar
#       .................. ( değişkenin sahip olabileceği değerler kadar )
#       case_:             (kontrol edilen değerler dışında bir değer ile karşılaşınca çalışır.)
#           kodlar

sayi_1 = int(input("Birinci sayiyi girin:"))
sayi_2 = int(input("İkinci sayiyi girin:"))

islem = input("Hangi işlemi yapmak istiyorsunuz?(Toplama- 1, Çarpma- 2, Çıkarma- 3, Bölme- 4 giriniz)")

match islem:
    case "1":
        islem_yazili="Toplama"
        sonuc = sayi_1 + sayi_2
    case "2":
        islem_yazili="Çarpma"
        sonuc = sayi_1 * sayi_1
    case "3":
        islem_yazili="Çıkarma"
        sonuc = sayi_1 - sayi_2
    case "4":
        islem_yazili="Bölme"
        sonuc = sayi_1 // sayi_2
    case _:
        print("Yanlış seçim yaptınız.")

print(sonuc)
print(f"{islem_yazili} işleminizin sonucu {sonuc} dur.")
