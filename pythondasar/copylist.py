print("=====program mengcopy list======")
a = ["ujeh","uyen","usen"]
print(f"list 1 = {a}")
b = a
print(f"list 2 = {b}\n")
# kita membuat var baru lalu kita masukan nilai var yang lama di dalamnya
print("ini ketika di beri var baru yaitu B")
a[1]="uden"
print(f"list 1 = {a}")
print(f"list 2 = {b}\n")
# hasil di atas sama dikarenakan kedua var memiliki addres yang sama sehingga jika kita mengubah isi salah satu list maka list yang lain juga akan ikut terubah
print("melihat hexa pada list")
print(f"hexa list 1 = {hex(id(a))}")
print(f"hexa list 2 = {hex(id(b))}\n")

# solusinya kita menggunakan copy agar addresnya berbeda sehingga kita bisa mengubah listnya

print("ini adalah list baru dengn copy")
c = a.copy()
print(f"hexa list 1 = {hex(id(a))}")
print(f"hexa list 2 = {hex(id(b))}")
print(f"hexa list 3 = {hex(id(c))}")
c[0]="ubon"
print(f"list 1 = {a}")
print(f"list 2 = {b}")
print(f"list 3 = {c}\n")  
# akan berubah pada list yang ke 0 pada var c

b = a.copy()
b[1]="unon"
print(f"hexa list 1 = {hex(id(a))}")
print(f"hexa list 2 = {hex(id(b))}")
print(f"hexa list 3 = {hex(id(c))}\n")
print(f"list 1 = {a}")
print(f"list 2 = {b}")
print(f"list 3 = {c}\n") 