# Birden fazla veri tutan değişkenler 
# list(listeler)
# liste_adı = [değer1, değer2, ..............]
# farklı veri türlerini bir arada tutar. 
# dinamiktir. otomatik olarak büyüyebilir. 
# Array (dizi) - sabit boyutlu, tek tip veri tutarlar. (diğer diziler)

sinif_listesi =["ugur", "buse", "betül","celal"]
# 0 - ugur
# 1 - buse
# 2 - betül
# 3 - celal

gunler = [1,2,3,4,5,6,7]

kisi_bilgileri = ["betül",23,1999,"mühendis"]

bos_liste = []

print(sinif_listesi) #liste elemanlarına erişim.
# index -> çoklu veri yapılarında elemanlara vverilen sıra numarasıdır. index numarası gizlidir.
# index her zaman 0'dan başlar. 
# liste_adi[index_no]
print(sinif_listesi[2])

#eleman değiştirme
sinif_listesi[3] = "hasan"
print(sinif_listesi)

gecici_veri = sinif_listesi[0]
sinif_listesi[0] = sinif_listesi[1]
sinif_listesi[1] = gecici_veri
print(sinif_listesi)

# eleman silme
del sinif_listesi[1]
print(sinif_listesi)

# metod - (fonksiyon) - farklı bir nesne ile kullanıldığı için
# int, str, float, list, fonksiyon --> python'da her şey nesnedir. 

# sinif_listesi.fonksiyon_adı()  fonksiyon'a metod demiş oluyoruz. fonksiyon --> metod

sinif_listesi.append("Eray") # liste sonuna ekleme işlemi için append kullanılır.
sinif_listesi.append("Eray")
print(sinif_listesi)

c_count = sinif_listesi.count("eray") 
print(c_count) #sonuç 0 çıktı, o elemandan yok. 
c_count2 = sinif_listesi.count("Eray") 
print(c_count2) #sonuç 1 çıktı, öyle bir veri var. Eray'dan kaç tane var onu sayar.
# (__value: str, /) -> int
# int metodun veri ürettiğini ifade eder.
# (__value: str, /) kaç tane parametre verilmesi gerektiğini belirtir. 

sinif_listesi.insert(2,"Furkan")
print(sinif_listesi)

sinif_listesi.pop(0)
print(sinif_listesi)

gecici_veri = sinif_listesi[3]
sinif_listesi[3] = sinif_listesi[1]
sinif_listesi[1] = gecici_veri
print(sinif_listesi)

sinif_listesi.remove("Eray")
print(sinif_listesi)

sinif_listesi.sort() #sıralama yapar. 
print(sinif_listesi)

sinif_listesi.reverse() #listeyi tersten yazar.
print(sinif_listesi)

#ters index 
print(sinif_listesi[-1])

#parçalama işlemi - slice
parca1 = sinif_listesi[1:3] # son index numarası olan 3 dahil olmaz. 
print(parca1)

parca2 = sinif_listesi[-3:-1] #betül ve furkanı alır. - olarak sağdan saymaya başla. iki tanesini al.
print(parca2)
