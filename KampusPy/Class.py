import math

alas = int(input("masukan alas : "))
tinggi = int(input("masukan tinggi : "))


def menu_awal():
    pilih_menu = int(input("\nMau ngapain ?\n1.Luas Segitiga\n2. Sisi Miring\n3. Keliling\n4. Keluar\n:"))
    if pilih_menu == 1:
        luas_segitiga()
    elif pilih_menu == 2:
        sisi_miring()
    elif pilih_menu == 3:
        keliling()
    else :
        keluar()

def luas_segitiga():
    luas = (alas*tinggi)/2
    print("\n Luas Segitiga : ",luas)
    menu_awal()

def sisi_miring():
    sisiMiring = int(math.sqrt(tinggi**2 + alas**2))
    print("\n Sisi Miring : ",sisiMiring)
    menu_awal()

def keliling():
    sisi_miring = int(math.sqrt(tinggi**2 + alas**2))
    keliling = alas+tinggi+sisi_miring
    print("\n Keliling Segitiga : ",keliling)
    menu_awal()

def keluar():
    print("\n==== TERIMAKASIH ====")
menu_awal()



            
