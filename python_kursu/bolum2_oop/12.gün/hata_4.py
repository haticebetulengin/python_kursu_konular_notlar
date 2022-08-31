# Hata üretme
# raise -> herhangi bir yerde manuel hata oluşturmak için kullanırız. 
#raise ZeroDivisionError

#Örnek 1
def bad_fun(n):
    raise ZeroDivisionError

try:
    bad_fun(0)
except ArithmeticError:
    print("What happened? An error?")

print("THE END.")

# assert koşul -> bir koşul gerçekleşmediğinde hata üretiyor. 
    #import math
    #x = float(input("Enter a number: "))
    #assert x >= 0.0
    #x = math.sqrt(x)
    #print(x)

# üsttekinin revize hali

import math
x = float(input("Enter a number: "))
try:
    assert x >= 0.0
except:
    print("Hata oluştu.")

x = math.sqrt(x)
print(x)
