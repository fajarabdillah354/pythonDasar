# mengembalikan nilai dengan return
def angka(kuadrat):
    hasil = kuadrat**2
    print("hasil dari kuadrat",kuadrat, "=", hasil)
    return hasil
print(f"hasilnya adalah {angka(9)}")

def operasi1(penjumlahan1,penjumlahan2):
    total = penjumlahan1 + penjumlahan2
    print("hasil dari",penjumlahan1,"+",penjumlahan2,"=",total)
    return total
def operasi2(perkalian1,perkalian2):
    total = perkalian1 * perkalian2
    print("hasil dari",perkalian1,"*",perkalian2,"=",total)
    return total 
a = operasi2(7,operasi1(3,8))
print(f"hasil dari operasi2 yang di beri value operasi1 = {a}")


