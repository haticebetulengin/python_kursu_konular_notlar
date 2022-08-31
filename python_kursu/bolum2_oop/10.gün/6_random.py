# random - rastgele sayı üretmek için kullanılır. 
from random import random ,seed, randrange, randint# random hem modül adı hem de method adıdır. 

print(random()) # 0.0 ile 1.0 arasında değer üretir. 

seed(0) # aynı sayıyı/verileri üretmemizi sağlıyor. 


print(random()) # seed kullanıldığı için hep aynı değeri üretir diğer çalışmalarında. 

print(randrange(10,100)) # verilen aralıkta sayı üretir.

print(randint(0,100))

from platform import platform
print(platform())

