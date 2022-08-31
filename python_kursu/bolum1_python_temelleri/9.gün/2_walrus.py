# walrus : 3.10 ile birlikte geldi. hem atama yapar, hem veri döndürür. 
# = --> atama operatör

c = 5 #RAM e veri kayıt eder

# := --> walrus operatörü
#print(b = 34) hatalı bir gösterimdir. önce b tanımlanmalı ve değeri verilmeli sonra print edilmeli
print(a := 55)

print(a := 1903) # çıktısı 1903 olur. veriyi kaydeder hem de geri döndürür.
print(a) #kaydedilen veri olarak 1903 gösterir. 

sayı = int(input("Sayi girin"))
while sayı<10:
    print(sayı)
    sayı += 1
