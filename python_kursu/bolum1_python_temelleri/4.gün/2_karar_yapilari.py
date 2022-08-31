# if- eğer
# if (hava == soguk): --> True, False  
#    giyin(mont)
# else:
#    giyin(tişört)

hava = "sıcak"
if(hava == "sıcak"):
    print("tişört giyin")

#ya alınan inputu int'e çevirip öyle kontrol yapacağız.
puan = int(input("Lütfen puanı giriniz:"))
if(puan >= 50):
    print("Tebrikler BAŞARDINIZ.")

#ya da aldığımız input ile if içinde "50" olarak string kullanacağız.
puan = input("puanı giriniz:")
if(puan < "50"):
    print("Üzgünüm KALDINIZ.")