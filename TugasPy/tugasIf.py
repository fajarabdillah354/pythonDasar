#tugas membuat pemilihan dengan dengan if
print("************** Program pengecekan absen siswa baru ***************")
siswa = ["Udin petot","Zimbay parimbay","Fajar abdillah ahmad","Ujhe pajhejhe","Jupriy juripiy"]
for i in siswa:
    print(i)
print("============================")
nama = (str(input("Cari nama : ")))
nim = (int(input("Cari nim : ")))

if nama == "fajar abdillah ahmad" and  2103015111:
    print("absen anda adalah 17")
elif nama == "Udin petot" and 2103015044:
    print("absen anda adalah 20")
elif nama == "Zimbay parimbay" and 2103015123:
    print("absen anda adalah 33")
elif nama == "Ujhe pajhejhe" and 2103015678:
    print("absen anda adalah 22")
elif nama == "Jupriy juripiy" and 2103015047:
    print("absen anda adalah 18")
else:
    print("anda tidak terdaftar")


