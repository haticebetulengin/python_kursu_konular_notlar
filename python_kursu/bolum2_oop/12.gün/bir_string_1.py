# Stringler değiştirilemez. Ekleme, silme yapamıyoruz.
isim = "arhavihem"
# isim[3] = "b"
# print(isim)

# Özel değişken
# İndeksleme vardır.
print(isim[3:6])

isim2 = "hopa"
adres = "ortahopa"
# çok satırı """ veya ''' ile başlatırız. 
cok_satır = """ortahopa mahallesi  
turgay ciner caddesi 
hopa/artvin
08600"""
print(cok_satır)

char_1 = 'a'
char_2 = " " #space
print(ord(char_1)) # ord -> harflerin sayı karşılığını verir.
print(ord(char_2))

print(chr(97)) # chr -> ile sayının harf karşılığını buluyoruz.
print(chr(945))

# stringlerde append(), remove() vs yapamıyoruz. ama ekleme yapabiliyoruz.
alphabet = "bcdefghijklmnopqrstuvwxy"
alphabet = "a" + alphabet
alphabet = alphabet + "z"
print(alphabet)

print(list("abcabc")) # list() ile stringi listeye çeviririz. 

