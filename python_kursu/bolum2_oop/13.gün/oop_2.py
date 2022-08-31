# Initialize - İlklendirme - init
# Yapıcı metod - constructor
# Nesne --> Sınıfın örneği - class instance 

class Ornek5:
    pass

class Ornek4():
    pass

class Ornek3(object):
    pass


class Ornek():
    #Sınıf tanımlamasından sonra tanımlanan özellikler SINIF ÖZELLİKELERİdir.
    a = 5 
    b = "Merhaba, merhaba."
    # Çalışan __init__ diye bir metod vardır. Yapıcı metod diyoruz buna
    # Gizlidir, eklemesek de bulunur. 
    def __init__(self,sayi): #initializ, nesne tanımlamasını sağlar. 
        # init içerisinde self ile tanımlanan özellikler NESNE ÖZELLİKLERİdir. 
        self.sayi = sayi
        # yapılan bu işlem şu demektir. bu sınıftan nesne ürettiğimiz zaman buraya parametre göndermemiz gerektiğini belirtir.
        # self - kendi - nesneyi temsil ediyor. (1.parametre nesneyi temsil eder.)

n1 = Ornek(1999) # self = n1
print(n1.a)
print(n1.sayi)

n2 = Ornek(12)
print(n2.a)
print(n2.sayi)