x = 123 #bu değişken

def fonk():
    x = 456
    print(x) #1.satırdaki değişken bu değişken ile aynı değildir.
    # local değişken olarak adlandırılır.

fonk() #ekrana 456 yazar
print(x) #ekrana 123 yazar

y = 45
def fonk2():
    global y # global değişkendir. bir önceki tanımlanan y ile aynı ifadeyi taşır. 
    y = 34
    print(y)

fonk2()
print(y)
