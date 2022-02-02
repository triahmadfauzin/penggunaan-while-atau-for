print("Membuat deret fibonacci")

banyak_bilangan = int(input("Masukkan banyaknya bilangan : "))
d1 = 1
d2 = 0

for i in range(banyak_bilangan):
    print(d2, end=",")
    total = d1 + d2
    d1 = d2
    d2 = total
