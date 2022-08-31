# Default değerli parametreler (argümanlar)
def carpma (a,b,c=2): # c yerine veri gelmediği zaman c'nin değeri 2 kabul edilir.
    sonuc = a * b * c
    return sonuc

s1 = carpma(10,11) # c'ye değer gönderilmediği için c=2 kullanılacak default olarak
print(s1)

s2 = carpma(2,3,4) # c yerine 2 değil de 4 kullanılacak.
print(s2)

s3 = carpma([1,2,3],4)
print(s3)

#default değerli argümanlar en sona yazılmalıdır. yani sıralı elemanlardan sonra yazılmalıdır. 
# def carpma (a,b=3,c):  -> HATALI TANIMLAMA. b en sona tanımlanmalıydı.
#   sonuc = a*b*c
#   return sonuc

print("########################################")
def fonk_2(a="pyth", b = 2, c = [1,2,3]):
    print(a)
    print(b)
    print(c)

fonk_2(b=4, a="betül") # olarak da yazabiliriz. 

fonk_2(5,"dkdkddk") #program çalışmasına engel olmuyor ama mantıken yanlış bir eşleme olur. 
#biz ilk parametreyi string, ikinci parametreyi sayı istiyorduk burada tam tersi olmuş oldu. 

