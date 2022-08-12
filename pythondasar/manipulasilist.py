# mengambil index pada list
#             0        1       2 (hitungan list)
#             -3         -2        -1
print("=====menghitung index pada list=====")
data_list = ["ucup","sotong","epen"]
data = data_list[0] 
print(f"data index ke-1 = {data}")
# akan mengambil list ke 0....nb= jika kita akan menghitung dari urutan belakang maka kita hanya beri - (min) lalu pilih index ke berapa

data = data_list[-1]
print(f"index terakhir = {data}")

data = data_list[-3]
print(f"index pertama = {data}")

data = data_list[2]
print(f"data index ke -3 adalah = {data} ")

print("\n===menentukan panjang list===")

#menentukan panjang list menggunakan fungsi (len)
data = len(data_list)
print(f"panjang list = {data}")

# menambah data pada list sesuai posisi dengan menggunakan fungsi (insert)
print("===menambah data sesuai posisi===")
print(f"ini adalah data sebelum di tambah {data_list}")
data_list.insert(1,"ujeh")
print(f"ini adalah data setelah di tambah {data_list}\n")

# menambah data hanya pada bagian terakhir saja
print("===menambah di bagian terakhir saja===")
print(f"ini adalah data awal {data_list}")
data_list.append("konto")
print(f"setelah di tambahkan di akhir {data_list}\n")


# menghapus list yang sudah ada dengan fungsi (remove)
print("===menghapus list yang sudah ada===")
print(f"data awal = {data_list}")
data_list.remove("ujeh")
print(f"ini data baru yaitu list ujeh di hilangkan dari daftar = {data_list} \n")

# menghapus list hanya yang paling akhir saja dengan fungsi (pop)
print("===menghapus list hanya yang paling akhir saja===\n")
print(data_list)
bau = data_list.pop()
print(f"bagian akhir list ini hilang {data_list}")
print(f"data yang hilang adalah = {bau}\n")

# menambah beberapa list dengan fungsi (extend)
print("===menambah beberapa list===")
print(f"data lama = {data_list}")
data_baru = "jojo","juju","jeje"
data_list.extend(data_baru)
print(f"list yang baru = {data_list}")






 

