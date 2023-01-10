print("==== selamat datang =====")
file_teks = open("read.txt","r")
baca = file_teks.readlines()
print(baca[0])
print(baca[1])
# kita bisa menggunakan for jika data yang akan kita baca terlalu banyak dengan cara:
# for read in baca:
#     print(read)
file_teks.close()