from math import sin,pi

print(sin(pi/2)) # modülden gelen sin ve pi kullanılıyor.

pi = 3.14

def sin(x):
    if 2 * x == pi:
        return 0.999999999
    else:
        return None

print(sin(pi/2)) # kendi yazdığımız sin ve pi kullanılıyor. 

# math gelen pi değerini kullanmak istiyorum diyorum. 
from math import sin,pi

print(pi)

from math import * # bütün komutları içe aktarır.

# takma ad verme
import math as m # başka bir isimle kullanmak için. 
# math yerine m harfi kullanılacak. 

from math import sin as sinus, pi as pi_sayisi

