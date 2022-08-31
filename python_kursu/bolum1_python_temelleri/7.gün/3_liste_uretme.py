liste_uretme = ["Betül" for i in range(8)]
print(liste_uretme) # 8 tane Betül içeren row listesi oluştu.

liste_uretme_1 = []
for i in range(8):
    liste_uretme_1.append("Betül")
print(liste_uretme_1)

#4,5,6. satırdaki kodlar yerine 1.satırdaki gibi tek satırda yazabiliriz. Kod yapısı aşağıdaki gibidir.
# liste_adi = [<döngüde çalışacak kod> for <tek_elemanli_değişken> in <cok_elemanlı_degisken>]

kare = [ i*i for i in range(8) ]
print(kare) 

tek_sayilar = []
for i in range(10):
    if (i % 2 == 1):
        tek_sayilar.append(i)

print(tek_sayilar)

ts = [i for i in range(10) if(i%2==1)] # Koşul varsa for'dan sonra yani sona eklenir.
print(ts)