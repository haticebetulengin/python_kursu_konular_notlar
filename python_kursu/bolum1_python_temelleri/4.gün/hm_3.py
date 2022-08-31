sayi_1 = int(input("Birinci sayiyi girin:"))
sayi_2 = int(input("İkinci sayiyi girin:"))

islem = input("Hangi işlemi yapmak istiyorsunuz?(Toplama- 1, Çarpma- 2, Çıkarma- 3, Bölme- 4 giriniz)")

if (islem == "1"):
    islem_yazili="Toplama"
    sonuc = sayi_1 + sayi_2
if (islem == "2"):
    islem_yazili="Çarpma"
    sonuc = sayi_1 * sayi_1
if (islem == "3"):
    islem_yazili="Çıkarma"
    sonuc = sayi_1 - sayi_2
if (islem == "4"):
    islem_yazili="Bölme"
    sonuc = sayi_1 / sayi_2
    # // olarak kullan. tam sayı şeklinde olsun .0 olmaz işlem sonucunda. 

print(f"{islem_yazili} işleminizin sonucu {sonuc} dur.")