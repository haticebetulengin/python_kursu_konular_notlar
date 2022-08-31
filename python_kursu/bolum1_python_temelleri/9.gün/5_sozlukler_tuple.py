# Sözlükler - dictionary - dict

#index YOK
#SIRALI OLMAYAN VERİ YAPISI

#KEY(ANAHTAR)-VALUE(DEĞER) ÇİFTİ ŞEKLİNDEDİR
#OKUL-ARHAVİHEM, İLÇE-ARHAVİ, DOGTARH-1999
#Verilere erişmek için KEY kullanılır.

sozluk1 = {"adi":"Betül"} # adi = Betül gibi düşünebiliriz
print(sozluk1)
print(type(sozluk1))

print(sozluk1["adi"]) #sozluk_adi["key"]

sozluk2 = {"adi":"Betül", "tcno":123456, "dt":"31.03.1999", "yas":23, "memleket":"Hopa","dersler":["a","b","c"]}
print(sozluk2["dersler"])
print(sozluk2["dersler"][1]) # dersler içerisindeki "b" yi verir.

#farklı veri türleri içerir. 
#json dosyalarının temeli

print(sozluk2.items()) #hem anahtar değerlerini hem de value değerlerini verir.
print(sozluk2.keys())#liste halinde anahtar değelerini verir.
print(sozluk2.values())#değerleri bize verir.

#döngü ile tek tek yazdırırız.
for eleman in sozluk2.keys(): #keysleri tek tek yazdırabiliriz.
    print(eleman)

for i in sozluk2.values(): #değerleri tek tek yazdırıyoruz.
    print(i)

for anahtar,deger in sozluk2.items():
    #print(f"Key değeri: {anahtar}, value değeri: {deger}")
    print(f"{anahtar} : {deger}") #daha güzel görünüyor.

#Sözlüğe yeni değer eklemek için:
sozluk2["adres"] = "Ortahopa Mahallesi"
print(sozluk2)

#değişim için
sozluk2["memleket"] = "Arhavi"
print(sozluk2)

#silmek için
del sozluk2["tcno"]
print(sozluk2)

print(sozluk2.get("adi")) #adı yazdırır.
