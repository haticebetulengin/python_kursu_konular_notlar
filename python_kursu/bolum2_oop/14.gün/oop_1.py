# Metodları aşırı yükleme - overloading
from typing import overload


class Ornek():
    okul = "Karadeniz Teknik Üniversitesi"
    def __init__(self):
        self.sayi = 123456
        self.adi = "Betül"

    def metod_n(self, *args, **kwargs):
        print("Nesnenin parametresiz metodudur.")
    
    
    
n1 = Ornek()
n1.metod_n()
n1.metod_n(36)