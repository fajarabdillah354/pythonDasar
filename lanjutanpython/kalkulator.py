# print(30*"=")
# print("program membuat kalkulator")
# print(30*"=" + "\n")
# angka_1 = float(input("masukan angka = "))
# operator = input("masukan operator (x,/,+,-) = ")
# angka_2 = float(input("masukan angka = "))

# if operator == "x":
#     hasil = angka_1 * angka_2
#     print(f"hasilnya adalah {hasil}")
# elif operator == "/":
#     hasil = angka_1 / angka_2
#     print(f"hasilnya adalah {hasil}")
# elif operator == "+":
#     hasil = angka_1 + angka_2
#     print(f"hasilnya adalah {hasil}")
# elif operator == "-":
#     hasil = angka_1 - angka_2
#     print(f"hasilnya adalah {hasil}")
# else:
#     print("maaf saya tidak mengerti")
# print("terimakasih , program telah selesai")

# program membuat kalkulator
common = ""
while common != "keluar":
    common = input("masukan operator = ")
    if common == "keluar":
        break

    if common != "+" and common != "-" and common != "/" and common != "x":
        print("maaf perintah ini tidak dikenali!!!!!!")
        continue

    angka_1 = int(input("masukan angka kesatu = "))
    angka_2 = int(input("masukan angka kedua = "))

    if common == "+":
        result = angka_1 + angka_2
    if common == "x" :
        result = angka_1 * angka_2
    if common == "-":
        result = angka_1 - angka_2
    if common == "/":
        result = angka_1 / angka_2
    
    print(f"hasil = {result}")
    break




