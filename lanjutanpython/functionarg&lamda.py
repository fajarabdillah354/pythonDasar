# contoh menggunakan argumen sederhana
def kampus(univ):
    print("nama universitas = ",univ)

# contoh dengan keyword 
def mahasiswa(nama,nim,ttg):
    kampus("UHAMKA")
    print("nama mahasiswa = ",nama)
    print("NIM = ",nim)
    print("tanggal lahir = ",ttg)
mahasiswa(nama = "fajar",nim=2103015111,ttg="30-12-2000")

# contoh dengan default
def matakuliah(dosen,matkul="fisika",usia=30):
    print("nama dosen = ",dosen)
    print("mata kuliah = ",matkul)
    print("usia dosen = ",usia,"tahun")
matakuliah(dosen="harry ramza",matkul="Math",usia=80)
# pada bagian matkul dan usia opsional boleh di isi atau mengikuti default
# sedangkan pada variabel dosen kita harus memberi valuenya

# membuat fungsi dengan lamda
# lambda args : expression  (syntax)
bilangan = [2,3,4,5,6]
hasil =  map(lambda x: x*x ,bilangan)
print(list(hasil))

angka = lambda x,y :x + y
print(angka(43,89))

nama = lambda siswa : "hello"
print(list(nama(2)))
