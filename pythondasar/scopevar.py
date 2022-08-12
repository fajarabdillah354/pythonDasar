# membuat scope lokal
from os import get_inheritable


namahewan = "anjing"
def namaYangbARU (nama):
    namahewan=nama
    print("nama setelah di ubah ",nama)
namaYangbARU("buaya")
print("sekarang namanya =",namahewan)#nama yang dihasilkan dari sini anjing karna ini variabel lokal

# contoh scope global
guru = "toler tanaka"
def gurubaru(namaguru):
  global guru
  guru=namaguru
  print("nama baru =",namaguru)
gurubaru("endang soekamti")
print("guru yang baru bernama ",guru)

