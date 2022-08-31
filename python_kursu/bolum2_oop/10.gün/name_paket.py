def fonksiyon():
    print("Merhaba paket")
    print(__name__) # çıktısı __main__ dir. 
    # eğer bu dosya modül olarak kullanılmayacaksa 
    # __name__ değeri kullanılır. 

if __name__ == "__main__": # modül olarak çağırılmadığında çalışır. 
    fonksiyon()

# bütün kodların çalışmasını engellemek için kullanılır.
# __name__ -> __main__ ise dosyanın kendisi çalışır.
# __name__ -> __name__paket__ ise yani dosya adı ise modul olarak çalışır. 