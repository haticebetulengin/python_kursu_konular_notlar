# BaseException -> En temel hata
# birden fazla hata kontrolü yapabiliriz. 
# kendimiz de özel hata ekleyebiliriz. 
# İLK ÖNCE EN ÖZEL - EN SPESİFİK HATA KONTROL EDİLİR.
# sonrasında genel hatalar kontrol edilir. 

#özel hatalardan (en dip kısımdan) genel hatalara doğru gidilir.
#try:
#    pass
#except en_ozel_hata:
#    pass
#except:
#    pass

#ÖRNEK 1
try:
    x = int(input("Enter a number: "))
    y = 1 / x
    print(y)
except ZeroDivisionError:
    print("You cannot divide by zero, sorry.")
except ValueError:
    print("You must enter an integer value.")
except:
    print("Oh dear, something went wrong...")

print("THE END.")

#ÖRNEK 2
try:
    y = 1 / 0
except ZeroDivisionError:
    print("Oooppsss...")

print("THE END.")

#ÖRNEK 3
try:
    y = 1 / 0
except ZeroDivisionError:
    print("Zero Division!")
except ArithmeticError:
    print("Arithmetic problem!")

print("THE END.")

#ÖRNEK 4
def bad_fun(n):
    try:
        return 1 / n
    except ArithmeticError:
        print("Arithmetic Problem!")
    return None

bad_fun(0)

print("THE END.")

