# Nesneye Yönelik Programlama - Object Oriented Programming (OOP)
# Programlamada bir yöntemdir.
# Yöntem - Bazı kuralların tanımlandığı, program geliştirmeyi kolaylaştırır. 
# Nesneye kadar olan kısma fonksiyonel programlama - prosedürel programlama denir. Fonksiyonları kullanarak program yazılır.

# Sınıf (Class) - Nesne (Object) iki önemli kavramdır. 
a = 5
print(type(a))

b : int = 6 # veri türünü belirledik. int -> veri türü // sınıf - class(int)
print(type(b))
# b - değişken
# b - nesne - object 
# bizim b yi tanımlamamızı sağlayan yapı da int yani sınıftır.  
# python'da her şey bir sınıftır.

c : int = 8
d : int = 10
# SINIFI TEKRAR TEKRAR KULLANARAK NESNELER ÜRETİYORUZ.
# pasta kalıbı - sınıf - tekrar tekrar nesne üretmek için kullanıyoruz. 
# yapılan kek - nesne

# program geliştirirken 
# kullanılacak yapıyı kurallarını belirterek bir sınıf oluştururuz. 
# Sınıflar 1 kez oluşturulur.
# Sınıflardan nesne üreterek tekrar tekrar kullanırsınız. 

ad : str = "aaa"
ad2 : str = "bbb"
ad3 : str = "ccc"
ad4 = str("Betül")

sayi = int(34)

# CLASS - özel bir veri türü üretme işlemidir. 
# fonk. veri tutmaz. fonksiyon çalışır - işlemi yapar - kaybolur.
# sınıflarda veriler tutulur. bu verileri işleyebiliriz. 
# Sınıflarda fonksiyon tanımlayabiliriz.

liste1 = list([1,2,3])
print(liste1)
liste1.insert(3,6) # 3. index'e 6'yı ekle. 
print(liste1)
# class - veri//değişken - fonksiyon//metod ==> Object üretiyoruz. 