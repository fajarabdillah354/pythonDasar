# penggabungan string
a = "aku"
b = "sehat"
c = "sekali"

lengkap = a + b + c
print(a + " " + b + " " + c)

# menghitung panjang string
panjang = len(lengkap)
print("panjang dari string ini adalah = " + str(panjang))

# mengecek string dalam string
x = "a"
status = x in lengkap
print(status)

# mengulang string dengan tanda *
print(("fajar" + " ")*5)
print(5*("wk" + " "))  

# index pada string
hap = "aku adalah seorang kapiten,mempunyai pedang panjang"
print("index ke-6 dari " + hap + "=" + hap[6])
print("index ke (5:10) = " + hap[5:12])
print("index ke - (1:10:2) " + hap[1:10:2])

# pengecekan method pada string
# count(mengecek kata yang ada dalam string)
data = "otong surotong pararotong"
count = data.count("o")
print("jumlah o pada " + data + " = " +  str(count))

tes = "lucu banget wkwkwkwkkwkwkwkwk"
hitung = tes.count("w")
hitung2 = tes.count("k")
print("TOTAL HURUF W ADALAH = " + str(hitung))
print("total huruf k adalah = " + str(hitung2))
total = hitung + hitung2
print("total wk = " + str(total))

# macam - macam pengecekan dengan is method
# 1. is lower(mengecek huruf kecil dalam string )
p = "dak sepeda itu rusak"
cek = p.islower()
print("apakah ini sudah benar = " + str(cek))
cek = p.isupper()
print("apakah ini sudah benar = " + str(cek))





