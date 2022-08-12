#contoh program segitiga
# segitiga = 1
# while segitiga <= 6:
#     print("*" * segitiga)
#     segitiga += 1
# print("terimakkasih atas program segitiganya")


#ini adalah program sederhana dari tebak angka
tryed = 0
limit = 3
secret_number = 7
while tryed < limit :
	input_user = input("Masukan angka yang akan anda pilih : ")
	input_user = int(input_user)
	if secret_number == input_user :
		print("selamat angka yang anda masukan sesuai dengan angka rahasia")
		tryed += 1
		break


