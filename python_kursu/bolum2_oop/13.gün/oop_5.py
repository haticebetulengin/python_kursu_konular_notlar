# Normal kullanım ile nesne ya da sınıfın kendine ait olan verileri ifade etmek için __ kullanılır. 
# Gizli öğe tanımlaması deriz.

class Ornek():
    okul = "Arhavi Halk Eğitim"
    __il__ = "Artvin" # Gizli eleman. ama tam olarak gizli değil.
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


print(dir(Ornek))
print(Ornek.__il__)

print(hasattr(Ornek(),"okul")) # Bu sınıfın böyle bir özelliği var mı? True/False cevabıdır.

print(Ornek.__dict__) #Sınıfla ilgili bilgileri verir. Sınıfın özelliklerini verir. 

# __name__ - kendi içindeyken sınıf adıdır. Modul adı sorulduğunda, import edildiğinde ise dosyanın adı olacaktır.
#  