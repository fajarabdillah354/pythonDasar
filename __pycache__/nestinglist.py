# pada kali ini kita akan membuat list dalam list atau yang biasa di sebut dengan nesting list

# membuat nama - nama list 
peserta_0 = ["fajar",21,"laki-laki",2103015111]
peserta_1 = ["anisa",21,"perempuan",2103015047]
peserta_2 = ["iday",21,"laki-laki",2103015076]

# membuat variabel baru untuk penempatan nesting list
list_peserta = [peserta_0,peserta_1,peserta_2]

for peserta in list_peserta:
    print(f"nama\t = {peserta[0]}")
    print(f"usia\t = {peserta[1]}")
    print(f"gender\t = {peserta[2]}")
    print(f"NIM\t = {peserta[3]}\n")