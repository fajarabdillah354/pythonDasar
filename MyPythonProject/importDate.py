import datetime as dt
from re import A
print("======program mencari tanggal lahir=======")
print("masukan tanggal lahir anda,bulan lahir anda , dan tahun lahir anda")

tanggal = int(input("masukan tanggal = "))
bulan = int(input("masukan bulan lahir = "))
tahun = int(input("masukan tahun lahir = "))
tanggal_lahir = dt.date(tahun , bulan , tanggal)
print(f"tanggal lahir anda adalah = {tanggal_lahir}")
print(f"harinya adalah hari = {tanggal_lahir:%A}")
hari_ini = dt.date.today()
print(f"hari ini adalah hari = {hari_ini}")
umur_hari = hari_ini - tanggal_lahir
umur_tahun = umur_hari.days // 365
umur_sisa_bulan = (umur_hari.days % 365) // 30
print(f"Umur hari anda = {umur_hari}")
print(f"umur tahun anda = {umur_tahun} tahun , {umur_sisa_bulan} bulan")
