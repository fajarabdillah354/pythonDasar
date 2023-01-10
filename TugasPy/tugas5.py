import pymysql

db = pymysql.connect(
    host="localhost",
    user="root",
    passwd="",
    database=""
)

cursor = db.cursor()
cursor.execute("SHOW TABLES")
data = cursor.fetchall()
print("isi tabel : ",data)

cursor = db.cursor()
sql = "SELECT * FROM pembayaran"
cursor.execute(sql)

result = cursor.fetchall()

for data in result:
    print(data)













# T = int(input("Tinggi segitiga : "))
# for i in range(1,T+1):
#     print(i * "*")
    # print(((T-i+1) * " ")+(i*"*"))
    # print(((T-i+1) * " ")+(i*"*") +((i-1)*"*") )

# i = int(input("Tinggi Segitiga : "))
# j = 1
# while j <= i:
#     k = 1
#     while k <=  j:
#         print("*", end=" ")
#         k += 1
#     print()
#     j += 1


    



# def enterAge(age):
#     if age < 0:
#         raise ValueError("angka bernilai negatif ")
#     elif age % 2 == 0:
#         print('entered age is even')
#     else:
#         print("YOUR AGE IS ACCEPT because your age ganjil")

# try:
#     num = int(input("please enter your age : "))
#     enterAge(num)
# except ValueError: 
#     print('terjadi error : ',ValueError)



