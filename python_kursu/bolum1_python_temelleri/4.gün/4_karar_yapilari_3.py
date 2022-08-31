#Alışveriş sitesinde 100 tl ve üzeri kargo bedava

alisveris_tutari = int(input("Ne kadarlık alışveriş yaptınız? :"))
kargo_bedeli = 20

#Kullanıcıya toplam ödeme miktarını söyleyeceğiz.

if(alisveris_tutari >= 100):
    print(f"Kargonuz bedavadır. Ödeceyeciğiniz tutar {alisveris_tutari} kadardır.")
else:
    print(f"Kargo ücreti alışveriş tutarınıza eklenecektir. Ödeyeceğiniz tutar {kargo_bedeli+alisveris_tutari} kadardır.")
    