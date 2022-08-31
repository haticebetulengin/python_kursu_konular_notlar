#toplama programı

sayi_1 = input("Birinci sayiyi girin:") #Kullanıcı girişinde tüm veriler string kabul edilir.
#Sayisal veri lazımsa dönüştürme işlemi yapmamız gerekiyor.
#int()
sayi_1 = int(sayi_1)

sayi_2 = input("İkinci sayiyi girin:")
sayi_2 = int(sayi_2)

toplam = sayi_1 + sayi_2

print(toplam)
print("Toplama işleminin sonucu:",toplam)
print(f"Toplama işleminin sonucu {toplam} dır.")
#İkinci yol 
#ilk_sayi = int(input("İlk degeri giriniz:"))
#ikinci_sayi = int(input("İkinci sayiyi giriniz:"))
#toplam_2 = ilk_sayi+ikinci_sayi
#print(toplam_2)
