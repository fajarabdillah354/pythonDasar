# operasi bitwase
# menggunakan or

from traceback import format_exc


a = 9
b = 5
c = a | b
print('=======dengan OR========')
print('nilai = ',a,' ,binary = ',format(a,'08b'))
print('nilai = ',b,' ,binary = ',format(b,'08b'))
print('----------------------------------------(|)')
print('nilai = ',c, ',binary = ',format(c,'08b'))

# menggunakan and
c = a & b
print('=========dengan AND==========')
print('nilai = ',a,' ,binary = ',format(a,'08b'))
print('nilai = ',b,' ,binary = ',format(b,'08b'))
print('----------------------------------------(&)')
print('nilai = ',c, ',binary = ',format(c,'08b'))


# menggunakan XOR(^)
c = a^b
print('=========dengan XOR==========')
print('nilai = ',a,' ,binary = ',format(a,'08b'))
print('nilai = ',b,' ,binary = ',format(b,'08b'))
print('----------------------------------------(^)')
print('nilai = ',c, ',binary = ',format(c,'08b'))

# menggunakan not(~)
# nb =jika kita ingin membuat not kita perlu flip menggunankan  XOR(^)
c = ~a
print('=======dengan NOT=======')
print('nilai = ',a,' ,binary = ',format(a,'08b'))
print('--------------------------(~)')
print('nilai = ',c ,' ,binary = ',format(c,'08b'))
print('--------------------------(^)')
d = 0b0000001001
e = 0b1111111111
print('nilai = ',d^e,' ,binary = ',format(d^e,'08b'))

# MENGGUNAKAN  SHIFT(GESER-  GESERAN)
# SHIFTING RIGHT (GESER KANAN)
c = a >> 3
print('=========shift right==========')
print('nilai a = ',a,' , binary = ',format(a,'08b'))
print('------------------------------(>> 3)')
print('nilai = ',c,' ,binary = ',format(c,'08b'))

# shitfint left (geser kiri)
c = a << 1
print('===========shift Left============')
print('nilai a = ',a,' ,binary = ',format(a,'08b'))
print('-------------------------------(<< 1)')
print('nilai c = ',c,' ,binary = ',format(c,'08b'))



