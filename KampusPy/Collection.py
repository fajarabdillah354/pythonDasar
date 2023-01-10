###### 1. LIST #######
print((30*"="),"LIST",("="*30))
# dengan menggunakan String double quotes
my_list1 = ["kucing","ikan","kelinci"]
print(my_list1)

# dengan menggunakan number
my_list2 = [3,4,5]
print(my_list2)

# dengan menggunakan boolean
my_list3 = [True,False,True]
print(my_list3)

# dengan menggunakan campuran(Stirng,float,Boolean,Tuples)
my_list4 = ["fajar",354.2,True,("kucing","kambing","sapi")]
print(my_list4)

# dengan menggunakan range
# di bawah ini akan mencetak range atau panjang dari suatu list
my_list5 = range(3,5,4)
list_range = list(my_list5)
print(list_range)

# dengan menggunakan forloop
# di bawah ini mempunyai range dari 1 sampe 9
data_forlop = [i*2 for i in range(1,10)]
print(data_forlop)

# dengan menggunakan for if
data_forif = [i for i in range(1,30) if i%2==0]#akan mencetak nilai yang jika dibagi 2 habis(angka genap)
print(data_forif)

### OPERASI PADA LIST
list_data = ["burung","kucing","ikan"]
# 1. indexing(mengambil data list)
ambil = list_data[1]
print(ambil)

# 2.  mengambil panjang dari list dengan function len()
panjang = len(list_data)
print(panjang)

# 3. menambah data list dengan posisi costom dengan insert(index,obj)
list_data.insert(1,"gajah")
# parameter pertama adalah posisi indexnya ,parameter kedua isi object yang mau ditambah ke list
print(list_data)

# 4. menambah data yang paling akhir dengan append(obj)
list_data.append("kelinci")
print(list_data)

# 5. menambah list dengan list menggunakan function extend(Iterable[str])
list_awal = ["singa","macan"]
list_data.extend(list_awal)
print(list_data)

# 6. meremove data list dengan function remove(obj)
list_data.remove("macan")
print(list_data)

# 7. meremove data yang paling akhir dengan function pop()
list_data.pop()# saat ini terjadi maka list singa akan ke apus
print(list_data)
list_hilang = list_data.pop()
print(list_hilang)# akan memanggil list yang hilang

#### OPERASI PADA LIST PART 2
#1. menghitung pada data pada list dengan function count(obj)
# yang dihitung adalah datanya bukan panjang listnya
list_data.insert(3,"gajah")
print(list_data)
hitung_data = list_data.count("gajah")
print(f"banyak list dengan nama gajah : {hitung_data}")

#2. mengambil index pada data list dengan function index(obj)
getIndex = list_data.index("ikan")
print(f"ikan berada pada index ke : {getIndex}")

#3. mensorting list dengan function sort(), dan membalik/reverse dengan function reverse()
my_list2 = [8,34,12,32,7,9,2]
print(my_list2)
my_list2.sort()# akan diurut dari yang kecil sampai ke besar
print(f"hasil setelah di sorting asending : {my_list2}")
my_list2.reverse()
print(f"hasil setelah di desending : {my_list2}")


####### 2. TUPLES #######
print((30*"="),"TUPLE",("="*30))
# Tuple adalah sebuah list yang imutable yaitu tidak bisa diubah lagi datanya,hal ini karna tuple berisi data-data paten
#1. mengubah suatu data menjadi tuple,dengan menggunakan function tuple
ubahTuple = tuple(my_list1)
print(ubahTuple)

#2. mengecek index pada tuple
k = ubahTuple.index("kelinci")
print(f"kelinci ada pada index ke : {k}")

#3. melihat panjang dari tuple dengan functiion len()
# pada my_list1 tetap dihitung 1 
ubahTuple = (my_list1,"harimau","rusa","monyet")
panjang=len(ubahTuple)
print(f"panjang dari tuple :  {panjang}")

#4. melihat data max pada tuples dengan function max()
data_num = tuple(my_list2)
tuple_max = max(data_num)
print(f"data terbesar pada tuples : {tuple_max}")

#5. melihat data terkecil dari tuple dengan function min()
tuple_min = min(data_num)
print(f"data terkecil dari tuple : {tuple_min}")

#6. jumlah dari semua tuple dengan function sum()
tuple_sum = sum(data_num)
print(f"jumlah dari tuples {data_num} : {tuple_sum}")

#7. mensorting tuple dengan function sort()
tuple_sort = sorted(data_num)
print(f"sorting tuple : {tuple_sort}")


######## 3. SET ############

print((30*"="),"SET",("="*30))
# SET merupakan sebuah kumpulan data yang unique(yaitu tidak boleh ada yang duplicate),SET tidab bisa berisi list namun tuple bisa,pada SET tidak memiliki index seperti pada list sehingga kita tidak bisa mengaksees indexnya

#1. membuat set dengan tuple
data_set = set(data_num)
print(data_set)

#2. menambah isi set dengan function add(),ini hanya untuk 1 object yang di tambah
data_set.add(25)
print(f"ini setelah ditambah 25 : {data_set}")

#3. menambah data dengan function update()

data_set.update((9,3,7))
print(f"ini setelah di update dengan tuple baru : {data_set} ")


#4. menghapus data set dengan function discard() atau remove()

#discard()
data_set2 = set(list_data)
print(f"ini adalah tuple awal : {data_set2}")
data_set2.discard("kucing")
print(f"menghapus set pada kucing : {data_set2}")

#remove()
data_set2.remove("ikan")
print(f"menghapus set ikan : {data_set2}")







