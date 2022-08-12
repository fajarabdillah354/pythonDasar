# macam - macam list

# 1. dengan string
data_string = ["fajar","nissa","love"]
print(data_string)

# 2 . dengan menggunakan number
data_num = [1,2,3,4,5,6]
print(data_num)

# 3 .dengan menggunakan boolean
data_bool=[True,False,True,False,False]
print(data_bool)

# 4. dengan campuran
data_campuran = [1,"ayam","mati",4,"bebek","dimakan",True]
print(data_campuran)

# 5. dengan range
data_range = range(1,9,3)
list_range = list(data_range)
print(list_range)

# 6. membuat list dengan for loop
data_loopfor = [i*2 for i in range (1,10)]
print(data_loopfor)

# 7. membuat list dengan for dan if
data_forif = [i for i in range(1,10) if i%2==0]#akan membuat hasil bilangan genap semuanya
print(data_forif)

data_forif = [i for i in range(1,10) if i%2 !=0]#akan membuat hasil bilangan ganjil semuanya
print(data_forif)

data_forif = [i for i in range(1,10) if i !=5]#akan menghilangkan angka 5 saat list berlangsung
print(data_forif)

print("="*30)
# ini adalah menjumlahkan semua list
# 1.dengan function sum
print("\nini adalah metode menjumlahkan list dengan function SUM")
nama = [3,5,8,9,2,1]
jumlah = sum(nama)
print(jumlah)
# 2.dengan menggunakan looping for
nama = [3,5,8,9,2,1]
awal_nama = 0
nama.sort()
print(f"ini adalah hasil urutan sebelum di jumlahkan semuanya {nama}")
print(f"ini adalah list terbesar = {nama[-1]}")
for i in nama :
    awal_nama = awal_nama + i
print(f"ini hasil jummlahnya {awal_nama}")
print("="*30)

#mencari nilai max pada list
# 1. dengan function max
print("dengan function max pada var")
nilai = [4,23,12,68,6,3,55]
nilai_max = max(nilai)
print(f"nilai maximal = {nilai_max}\n")
# 2. dengan perulangan dan if
print("dengan menggunakan perulangan dan if state")
nilai = [4,23,12,68,6,3,55]
max_nomor = nilai[0]
for i in nilai:
    if i>max_nomor:
        max_nomor = i
print(f" nilai maximal = {max_nomor}\n")
# 3. dengan menggunakan function sort
print("dengan menggunakan function sort")
nilai=[4,23,12,68,6,3,55]
nilai.sort()
print(nilai)
print(f"nilai maximal = {nilai[-1]}")


