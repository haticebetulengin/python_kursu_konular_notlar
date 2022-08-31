sinif_listesi =["ugur", "buse", "betül","celal"]
print(len(sinif_listesi)) #len bize listedeki eleman sayısı verir.

for index in range(len(sinif_listesi)): # döngü başlayınca 0'dan başlayıp 4'e kadar gidecek. liste boyutu kadar
    print(sinif_listesi[index].capitalize()) #listedeki elemanlarının ilk harfini büyütür ama öyle kaydetmez.
    
    sinif_listesi[index]=sinif_listesi[index].capitalize()
    # Listedeki elemanların ilk harflerini büyütüp öyle kaydeder, listedeki elemanlar artık büyük harfle başlıyor.

print(sinif_listesi)
