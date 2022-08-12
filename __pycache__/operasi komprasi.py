# print("\n=====program komparasi=====\n")

# # operasi > kurang dari
# a = 5
# b = 2
# hasil = a > b
# print("hasil a > b = ",hasil)

# # operasi < lebih dari
# hasil = a<b
# print("hasil a < b = ",hasil)

# # operasi <= kurang dari samadengan
# hasil = a<=b
# print("hasil a <= b = ",hasil)

# # operasi >= lebih dari samadengan
# hasil = a>=b
# print("hasil a >= b = ",hasil)

# # operasi == pembanding nilai 
# hasil = a==b
# print("hasil a == b = ",hasil)

# # operasi objek identity dengan is
# a = 5
# b = 5

# hasil = a is b
# print("nilai a = ",a,"id = ",hex(id(a)))
# print("nilai b = ",b,"id = ",hex(id(b)))
# print("hasil a is b = ",hasil)

# # operasi objek identitty dengan is not
# a = 6
# b = 4
# hasil = a is not b
# print("nilai a = ",a,"id = ",hex(id(a))) 
# print("nilai B = ",b,"id = ",hex(id(b))) 
# print("hasil a is not b = ",hasil)


# latihan komparasi dan logika
inputUser = float(input("masukan angka yang kurang dari 3 atau lebih dari 10 = "))
# membuat rentang angka ++++3-----10++++
# bagian ++++3
kurangdari = inputUser < 3
print(kurangdari)
# bagian ---10++++
lebihdari = inputUser > 10
print(lebihdari)
# hasil dengan logika
hasil = kurangdari or lebihdari
print("maka nilai kebenaran menggunakan atau : ",hasil) 
hasil = kurangdari and lebihdari
print("maka nilai kebenaran menggunakan Dan : ",hasil)
hasil = kurangdari ^ lebihdari
print("maka nilai kebenaran menggunakan XOR : ",hasil)