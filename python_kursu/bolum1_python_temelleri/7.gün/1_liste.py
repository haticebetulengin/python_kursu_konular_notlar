
sinif_listesi =["ugur", "buse", "betül","celal"]
print(len(sinif_listesi)) #len bize listedeki eleman sayısı verir.

# in / not in -> bir eleman liste için de mi diye bakmamıza yardımcı olur.
print("ugur" in sinif_listesi)
print("betül" not in sinif_listesi)

index_no = 0
for eleman in sinif_listesi: #sinif_listesi yerine -> range(len(sinif_listesi)-1)
    print(eleman.capitalize()) #capitalize() ile liste elemanlarının baş harfini büyük harfle yapıyoruz. 
    sinif_listesi[index_no] = eleman.capitalize() 
    #Kullandığımız listedeki verileri index_no kullanarak ilk harfi büyük olarak değiştirmiş olduk. 
    index_no += 1

print(sinif_listesi)
