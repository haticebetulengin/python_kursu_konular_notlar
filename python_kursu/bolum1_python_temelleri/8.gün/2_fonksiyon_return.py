# Fonksiyon veri üretir. (veriyi saklayamaz)
# Fonksiyon ürettiği veriyi geri döndürmemiz gerekir -> veri lazımsa
# RAM'e kayıt edilmesi gerekir.

# veri = input("Veri gir: ")

# return -> Fonksiyondaki veriyi geri döndürür.

# Veriyi geri döndüren fonksiyonlar
def carpma(a,b,c):
    sonuc = a * b * c
    return sonuc # üretilen veriyi ram'e kaydetmeyi sağlar.

carpma_sonucu = carpma(3,4,5) # RAM'e kaydettik. 
print(carpma_sonucu)
