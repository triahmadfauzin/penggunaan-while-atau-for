print("Memeriksa bilangan ganjil genap")

bil = int(input("Masukkan bilangan ganjil: "))

while bil <= 0 or bil % 2 == 0:
    bil = int(input("anda memasukkan bilangan genap, masukkan bilangan lagi : "))
    
else:
    print("benar")