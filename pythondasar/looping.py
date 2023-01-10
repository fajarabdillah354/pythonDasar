# ini adalah program loooping
# 1 . melooping dengan range
from datetime import date
from sqlite3 import Date


# angka = range(4)
# print(angka)

# for a in angka:
#     print("aku ganteng banget!!!!!")
#     print("serius niiii\n")

# # 2. melooping dengan list
# angka = [2,3,4,5]

# for data in angka :
#     print(f"data ke - {data}")

# # 3. melooping dengan str/string

# # angka = "aku lapar bingitttttt"
# # for apa in angka :
# #     print(apa)
# # macam - macam teknik melooping

# enumerete
# dengan fungsi ini kita bisa melooping lebih sederhana
# nama = ["nisa",#membuat list untuk nama
#         "bila",
#         "fitri",
#         "rena"]
# hobi = ['berenang',#membuat list untuk hobi
#         'baca buku',
#         'sepedaan',
#         'traveling']
# # looping dengan enumerete
# for i,d in enumerate(nama):#looping dengan menggunakan 2 variabel
#   print("="*5)#mencetak
#   print(i+1,d)#mencetak hasil looping
# print("="*100)#membut garis
# # looping dengan zip
# for name,hoby in zip(nama,hobi):#jika kita menggunakan zip kita dapat memberi banyak parameter dan var
#   print(name,"memiliki hoby",hoby)#mencetak hasil looping dengan zip
# print("="*50)

# # ini looping biasa
# x = 0
# for i in (nama):
#     x += 1
#     print(x,".",i)


#tugas looping
# barang = ["roti","nasgor","mie ayam"]#membuat list barang 
# print("***** selamat datang di warung gembira *****\n")
# print("Menu yang tersedia : ")#mencetak tampilan menu

# for i in barang:#looping untuk menampilkan menu
#   print(i)

# pilih = (str(input("masukan menu yang dimau : ")))#menkonver input dari user
# if pilih == "roti" :#perulangan if jika user memilih roti
#   harga = 5000#deklarasi variabel
#   print(f"harga 1 pcs roti = {harga}")#mencetak harga 1 pcs roti
# elif pilih == "nasgor":
#   harga = 10000
#   print(f"harga 1 pcs nasgor = {harga}")
# elif pilih == "mie ayam":
#   harga = 8000
#   print(f"harga 1 pcs mie ayam = {harga}")
# else:
#   print("barang tidak tersedia") 
  
# looping dengan dictobery
# print("====== nama peserta PKM yang lolos Pimnas ======")
# siswa = {"fajar abdillah ahmad":"uhamka",
#         "sandy maldini":"unsika",
#         "ryan adi wicaksono":"uny"}
# y = 0        
# for i,j in siswa.items():#dengan dic kita dapt memilih beberapa fungsi yang ada di emmet 
#   y+=1
#   print(y,"nama mahasiswa =",i,"kuliah di",j)

# nested loop
# n,i,j = 0,0,0
# print("============ Program membuat segitiga ============")
# n = input("masukan tinggi : ")
# n = int(n)
# for i in range(1,n+1):
#   for j in range(0,i):
#     print('*',end='')
#   print()


# loop yang diluar
for i in range(1, 11):
    # nested loop(loop yang di dalem)
    # itarasi dari 1 sampai 10
    for j in range(1, 11):#loop yang di dalem
        # mencetak perkalian 1 sampai 10
        print(i * j, end=' ')
    print()


