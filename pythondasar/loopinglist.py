# menggunakan comprehensif 
print("======menggunakan comprehhensif======")
himpunan = ["ujeh","uyen","usen"]
[print (f"data = {i}") for i in himpunan]

# menggunakan enumered
print("\n======menggunakan enumered======")
for index,data in enumerate(himpunan):
    print(f"index = {index}, data = {data}")

# menggunakan looping biasa
print("\n=====menggunakan looping biasa=====")
himpunan = ["ujeh","uyen","usen"]
for nama in himpunan:
    print(f"nama = {nama}")