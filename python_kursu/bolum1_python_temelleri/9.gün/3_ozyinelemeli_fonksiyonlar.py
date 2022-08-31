# Kendi kendini çağıran fonksiyonlar
def faktoriyel(n):
    if n==1:
        return 1
    else:
        return n * faktoriyel(n-1)

print(faktoriyel(4))

def fonk(n):
    sonuc = n * (n-1)
    return sonuc
