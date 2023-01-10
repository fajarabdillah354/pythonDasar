from operator import truediv

print("********* tugas mencari luas segitiga *********")
def name():
	nama = input("nama : ")
	kelas = input("kelas : ")
	nim = input("nim : ")
	print("NAMA : "+nama)
	print("KELAS : "+kelas)
	print("NIM : "+nim)
	print("============================")

def segitiga():
	while True:
		name()
		a = float(input("masukan alas segitiga yang diinginkan : "))
		b = float(input("masukan tinggi segitiga yang diinginkan : "))
		hitungluas = 0.5*a*b
		print("hasil Luas segitiga : "+str(hitungluas))
		ulang = input("pilih jika ingin kembali mencari luas(y/n) : ")
		if ulang == 'y':
			continue
		elif ulang == 'n':
			break

if __name__== '__main__':
	segitiga()


