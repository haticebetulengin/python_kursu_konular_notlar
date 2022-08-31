# Mantıksal operatörler: and, or, not
# Bitsel operatörler 
# & -> and
# | -> or
# ~ -> not
# ^ -> xor

print(55 < 66 and 45 > 77) #False çıktısı verir.

print(55 < 66 & 45 > 77) #False çıktısı verir.

# 0, 1 -> makine dili 
# Bitsel ifadeler sayıları ikili sayı sistemine dönüştürür ve bitler üzerinde işlem yapar. 

i = 15
j = 22
print(j and i) #15 değerini verdi
print(j & i) #6 değerini verdi. sayıları ikili sayı sistemine çevirip and işlemi uyguladı.
