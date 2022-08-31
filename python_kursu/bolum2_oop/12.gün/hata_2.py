# x = 2 / 0
# ZeroDivisionError
# hatasız çalışması için

#program çalışmaya devam eder. try-except kısmından sonra gelen kodları da çalıştırır. 
try:
    x = 2 / 0
    print(x)
except:
    print("Hata oluştu.")

