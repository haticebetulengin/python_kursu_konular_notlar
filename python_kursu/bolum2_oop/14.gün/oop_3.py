# Çokbiçimlilik - Polymorphism
# Kaç tane sınıf miras alınırsa alınsın,metod çağırılırken hangi nesne hangi sınıftan üretilmişse ona göre hareket eder.

class Ornek():
    okul = "Karadeniz Teknik Üniversitesi"
    def __init__(self):
        self.sayi = 123456
        self.adi = "Betül"

    def metod_n(self):
        print("Nesnenin parametresiz metodudur.", self.adi)
  
class YeniOrnek(Ornek):
    def __init__(self):
        super().__init__()
    
n1 = Ornek()
n1.adi = "Mehmet"
n1.metod_n()

n2 = YeniOrnek()
n2.adi = "Ayşe"
n2.metod_n()