# soal 1 = ---0++++5----8++++11-----
# bagian ---0++++
inputUser = float(input("nilai yang di bawah 0 sampai rentang 11 = "))
kurangdari = inputUser < 0
print(kurangdari)
# bagian +++5---
lebihdari = inputUser > 5
print(lebihdari)
# bagian ---8+++
kurangdari = inputUser < 8 
print(kurangdari)
# bagian+++11---
lebihdari = inputUser > 11
print(lebihdari)
# hasil dengan logic or
hasil = kurangdari or lebihdari
print("nilai kebenarannya menggunakan Atau  = ",hasil)
# hasil dengan logic and
hasil = lebihdari and kurangdari
print("nilai kebenarannya menggunakan Dan = ",hasil)
# hasil dengan logic XOR
hasil = lebihdari ^ kurangdari
print("nilai kebenarannya menggunakan XOR = ",hasil)
