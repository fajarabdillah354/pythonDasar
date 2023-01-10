from os import stat
def get_biodata():
	nama = input("Masukan Nama : ")
	tgl = input("Masukan Tempat Tanggal Lahir : ")
	alamat = input("Masukan Alamat : ")
	status = input("Masukan Status : ")
	pekerjaan = input("Masukan Pekerjaan : ")
	univ = input("Masukan Asal Kampus :")
	nim = input("Masukan NIM : ")
	print("********** Biodata Anda ********* ")
	print("Nama : "+ nama)
	print("Tempat Tanggal Lahir : "+tgl)
	print("Alamat : "+alamat)
	print("Status : "+status)
	print("Pekerjaan : "+pekerjaan)
	print("Asal Kampus : "+univ)
	print("Nim : "+nim)

def run():
	while True:
		get_biodata()
		input_again = input("Pilih jika ingin Menulis biodata lagi(y/n) :")
		if input_again == 'y':
			continue
		elif input_again == 'n':
			break

if __name__ == '__main__':
	run()