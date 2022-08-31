# modül : başkası tarafından geliştirilmiş
# kodları tekrar tekrar kullanmamızı sağlar
# kendimizde modül oluşturabiliriz.
# her .py dosyası bir modüldür.
# içerisinde tek bir konu için oluşturulmuş komutlar (fonksiyon metot değerleri)
# math - matematik ile iligili işlemler

# kullanmak için önce
# modülü indirmemiz gerekir (paket)
# çalışma alanında aktif hale getirmemiz gerekir.

# python ile gelen modüller var
# harici olarak yüklenen modüller var

# şimdiye kadar kullandığımız komutları içeren modüller vardı
# varsayılan olarak aktif idi 

import math #komutları aktif

# Komuta erişmek için MODULADI.KOMUT

print(math.factorial(5))
print(math.sqrt(100)) # math modülünün sqrt'sini kullanıyoruz. 

def sqrt(a): # Kendi sqrt fonksiyonumuzu çağırıyoruz. 
    return a ** 0.5 

print(sqrt(25))