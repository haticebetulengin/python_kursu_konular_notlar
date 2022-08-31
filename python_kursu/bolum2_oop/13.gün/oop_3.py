from curses.ascii import isdigit


class Ornek():
    def __init__(self,sayi):
        self.sayi = sayi
        # Nesne ilk oluştuğunda çalışması gereken bütün kodlar.
        # Başka bir fonksiyon çalıştırabiliriz. 
        # Farklı bir kütüphane çalıştırabiliriz. 
        # Kullanılacak verileri KONTROL ETMEK gerekebilir. 
        if (isdigit(sayi)):
            self.sayi1 = sayi
