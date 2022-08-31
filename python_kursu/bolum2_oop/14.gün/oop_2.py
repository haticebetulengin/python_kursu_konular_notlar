# overriding - eski metodu devre dışı bırak

class Ornek():
    okul = "Karadeniz Teknik Üniversitesi"
    def __init__(self):
        self.sayi = 123456
        self.adi = "Betül"

    def metod_n(self, *args, **kwargs):
        print("Nesnenin parametresiz metodudur.")

    
class YeniOrnek(Ornek):
    def __init__(self):
        super().__init__()
    
    def metod_n(self): #Miras aldığın sınıfın metodunu kullanma, kendi metodunu kullan.
        print("Nesnenin parametresiz metodudur. override edilmiş.")
    
n1 = YeniOrnek()
n1.metod_n()