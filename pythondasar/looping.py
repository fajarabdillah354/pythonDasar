# ini adalah program loooping
# 1 . melooping dengan range
from datetime import date
from sqlite3 import Date


angka = range(4)
print(angka)

for a in angka:
    print("aku ganteng banget!!!!!")
    print("serius niiii\n")

# 2. melooping dengan list
angka = [2,3,4,5]

for data in angka :
    print(f"data ke - {data}")

# 3. melooping dengan str/string

# angka = "aku lapar bingitttttt"
# for apa in angka :
#     print(apa)
# macam - macam teknik melooping

# enumerete
# dengan fungsi ini kita bisa melooping lebih sederhana
nama = ["fajar",
        "ryan",
        "sandy",
        "gilang"]
hobi = ['berenang',
        'baca buku',
        'motoran',
        'main bola']

# ini looping biasa
x = 0
for i in (nama):
    x += 1
    print(x,".",i)
# looping dengan enumerete
for i,d in enumerate(nama):#kita bisa menggunakan 2 variabel
  print("="*5)
  print(i+1,d)
print("="*100)
# looping dengan zip
for name,hoby in zip(nama,hobi):#jika kita menggunakan zip kita dapat memberi banyak parameter dan var
  print(name,"memiliki hoby",hoby)
print("="*50)

# looping dengan dic
siswa = {"fajar":"unpad",
        "sandy":"unsika",
        "ryan":"uny"}
y = 0        
for i,j in siswa.items():#dengan dic kita dapt memilih beberapa fungsi yang ada di emmet 
  y+=1
  print(y,"nama siswa =",i,"kuliah di",j)



