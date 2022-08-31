# hatanın ne olduğunu öğrenmek için;
try:
    y = 1 / 0
except Exception as e:
    print(e)

#except (ValueError, ZeroDivisionError) as hata:
#    print("Bir hata oluştu!")
#    print("orijinal hata mesajı: ", hata)
