# operasi assigment
from operator import truediv
from pickle import FALSE


a = 5 #operasi assigment pada a
print('nilai a =',a)
# operasi penjumlahan 
a += 10 #nilai a di tambah 2
print('nilai a += 2 = ',a)
# operasi pengurangan
a -= 3 #nilai a di kurang 3
print('nilai a -= 3 = ',a)
# operasi perkalian
a *= 5 # nilai a dikali 5
print('nilai a *= 5 = ',a)
# operasi pembagian
a /= 4 #nilai a dibagi 4
print('nilai a /= 3 = ',a)

# operasi pangkat / eksponen
a  **= 2
print('nilai a **= 2 = ',a)

# operasi modulus(sisa bagi)
a %= 4
print('nilai a %= 4 = ',a)

# operasi florr division
a //= 3
print('nilai  a //= 3  = ',a)


# operasi bitwase
# OR(|)
c =True
print('==========OR===========')
print('nilai c = ',c)
c |= False
print('nilai or jika true atau false = ',c)
print('=====================')

# AND(&)
c = False
print('==========AND===========')
print('nilai c = ',c)
c &= True
print('nilai and jika false dan true = ',c)
print('======================')

# XOR (^)				
c = False	
print('==========XOR===========')
print('nilai c = ',c)
c ^= True
print('nilai xor jika false ^ true = ',c)
print("------------------------")
c = True
print('nilai c = ',c)
c ^= True
print('nilai XOR jika true ^ true = ',c)
print('======================')


# bitwase geser - geser
# geser ke kanan
print('=======GESER KE KANAN========')
a = 0b00010
print('nilai a ',format(a,'05b'))
a >>= 1
print('nilai a >> 1 = ',format(a,'05b'))
print('maka nilai menjadi = ',a)
print('======================')

# geser ke kiri
print('=======GESER KE KIRI========')
a = 0b00010
print('nilai a ',format(a,'05b'))
a <<= 3
print('nilai a << 3 = ',format(a,'05b'))
print('maka nilai menjadi = ',a)
print('======================')
print(__name__)