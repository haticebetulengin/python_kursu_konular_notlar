# Miras - inheritance
# Bir sınıfın özelliklerini başka bir sınıfa aktarma.

# personel - yönetici - çalışan - müşteri

class personel: #base class - temel sınıf - üst sınıf - upper  sınıf
    def __init__(self,ad,soyad):
        self.ad = ad
        self.soyad = soyad

    def metot_n(self):
        print("Nesneye ait",self.ad)


# alt sınıf - sub class - türetilmiş sınıf.
class yonetici(personel): #Miras aldık. Personeldeki özellikler buraya aktarılmış olur.
    def __init__(self, ad, soyad):
        super().__init__(ad, soyad) #Super ile sınıfın öğelerini kullan demiş oluyoruz. super() bize personel sınıfını ifade eder.

p1 = personel("Buse","Özköse")
print(p1.ad , p1.soyad)
print(p1.metot_n())
y1 = yonetici("Betül", "Engin")
print(y1.ad , y1.soyad)   
print(y1.metot_n())

print(y1.__str__)