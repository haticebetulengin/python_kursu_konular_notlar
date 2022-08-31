puan = int(input("Lütfen puanınızı giriniz:"))

if (0<puan<50):
    print("Başarısız not.")
elif (50<= puan <70):
    print("Orta not.")
elif (70<= puan <85):
    print("İyi not.")
else:
    print("Çok iyi not.")
