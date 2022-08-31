class Ornek():
    okul = "Arhavi Halk Eğitim"
    def __init__(self):
        self.sayi = 0
        self.okul = "arhavihem"
        self.adi = "ben"
    def metod_s():
        print("Bu metod sınıfa aittir.")
    def metod_n(self):
        print("Bu metod nesneye aittir.",self.sayi)
    def metod_n1(self,a,b=15):
        print("nesneye ait metod" ,a,b)

n1=Ornek()
n1.adi = "Betül"
n1.okul = "KTÜ"
n1.sayi = 123456
print(n1.adi)

Ornek.metod_s() #Sınıfa ait olduğu için Ornek. olarak çağırdık.

#self ibaresi nesne olduğunu bize verir.
n1.metod_n()
n1.metod_n1(10,156)