# <<
# >>
# Sayıyı ikilik sayıya dönüştürür ve bitleri sağa ya da sola kaydırır. 
# bin() -> bir sayının ikilik sistemdeki karşılığını görmek için kullanılır.
# hex() -> bir sayının onaltılık sistemdeki karşılığını görmek için kullanılır.
# oct() -> bir sayının sekizlik sistemdeki karşılığını görmek için kullanılır. 
sayi1 = 5 
print(bin(sayi1)) # 101

sayi2 = 5>>1 #biti bir bit sağa kaydır. 
print(bin(sayi2)) # 10 -> 5 olan sayı 2'ye döndü
print(sayi2)

sayi3 = sayi1>>2 #iki bit kaydırdık 
print(sayi3)

sayi4 = sayi1<<1 # 1010 olur sola kaydırınca.
print(bin(sayi4))
print(sayi4)

# 0,1 --> Makine dili, bit
# 01100011 --> Byte ( 1 byte 8 bittir)
# 1024 Byte --> 1 KiloByte
# 1024 KB --> 1 MegaByte
# 1024 MB --> 1 GigaByte
# 1024 GB --> 1 TeraByte