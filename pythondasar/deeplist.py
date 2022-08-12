list_1 = [1,3]
list_2 = [4,8]

data = [list_1,list_2,20]
data_copy=data.copy()
print(f"data = {data}")
print(f"data copy = {data_copy}")

data_baru=data[0][0]
print(f"data baru = {data_baru}")

# memanggil addres 
print(f"addres data = {hex(id(data))}")
print(f"addres data copy = {hex(id(data_copy))}\n")

print("memanggil addres pada index list")
print(f"addres member data = {hex(id(data[0]))}")
print(f"addres member data copy = {hex(id(data_copy[0]))}\n")

# menggunakan deep copy
from copy import deepcopy

data = [list_1,list_2,20]
data_deep=deepcopy(data)

print(f"addres data = {hex(id(data))}")
print(f"addres data copy = {hex(id(data_copy))}\n")

print("memanggil addres pada index list")
print(f"addres member data = {hex(id(data[0]))}")
print(f"addres member data copy = {hex(id(data_copy[0]))}\n")

data[0][0]=15
print(f"data ={data}")
print(f"data copy = {data_copy}")
print(f"data deep = {data_deep}")
# saat bagian data deep tidak berubah seperti data & data copy