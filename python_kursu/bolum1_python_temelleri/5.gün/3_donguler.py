# tekrarlı işleri çalıştırmak için döngü (loop) kullanılır.
# for, while

for tek_deger_tutan_degisken in "cok_degerli_degisken":
    pass #kodlar

range(10) #sayı üretir. 0,1,2,3,4,5,6,7,8,9

for rakam in range(10):
    #print(rakam)
    print(rakam**2 )

for karakter in "arhavihem":
    print(karakter)

# Döngü kırma: break
for karakter in "arhavihem":
    print(karakter)
    if (karakter == "i"):
        break
