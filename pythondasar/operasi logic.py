# latihan ooeperassi logic
# menggunakan and(dan)
from operator import truediv


a = True
b = False
c= a and b
print("nilai a dan b = ",c)

a =  True
b = True
c = a and b
print("nilai a dan b jika true keduanya = ",c)
print("nilai dan akan bernilai benar jika true dan true")

# menggunakan ATAU (or)
a = False
b = True
c = a or b
print("nilai a atau b = ",c)

a = True
b = True
c = a or b
print("nilai a atau b jika true keduanya = ",c)

a = False
b = False
c = a or b 
print("nilai a atau b jika keduannya false = ",c)

# menggunakan XOR(harus saling berbeda)
a = True
b = True
c = a ^ b
print("nilai a XOR b jika keduanya true = ",c)

a= True
b= False
c= a^b
print("nilai a XOR b harus saling berselisih = ",c)

