print("========= Program Exception Handling ========\nCreated By : Fajar abdillah ahmad\nKelas : 3f\nNIM : 2103015111")
print("====== FrameWork Statistika ======\n1. Mencari median\n2. Mencari jangkauan antarkuartil\n3. Mencari Quartil\n4. Mencari Desil\n5. Mencari Persentil")
pilih = int(input("masukan pilihan anda : "))
try:
    if pilih == 1:
        print("==== Mencari Median ====")
        nilaiN = float(input("masukan banyak data yang ada : "))
        pembagi = float(input("masukan pembagi : "))
        hasil = nilaiN/pembagi
        print(hasil)
    elif pilih == 2:
        print("===== mencari jangkauan antarQuartil =====")
        nilaiQ1 = float(input("masukan nilai q1 : "))
        nilaiQ3 = float(input("masukan nilai q3 : "))
        pembagikuartil = int(input("masukan pembagi : "))
        hasilQuartil = (nilaiQ3-nilaiQ1)/pembagikuartil
        print(hasilQuartil)
    elif pilih == 3:
        print("***** rumus Untuk quartil (qi*n/4) *****\ndimana i =1/2/3")
        pilihI = str(input("Masukan nilai i yang dicari(i1,i2,i3) :"))
        try : 
            if pilihI == "i1":
                nilaiN = int(input("masukan nilai n :"))
                pembagiI1 = int(input("Masukan nilai pembagi untuk i1 : "))
                hasili1 = (1*nilaiN)/pembagiI1
                print(hasili1)
            elif pilihI == "i2":
                nilaiN = int(input("masukan nilai n :")) 
                pembagiI2 = int(input("masukan nilai pembagi untuk i2 : "))
                hasili2 = (2*nilaiN)/pembagiI2
                print(hasili2)
            elif pilihI == "i3":
                nilaiN = int(input("masukan nilai n :"))
                pembagiI3 = int(input("masukan nilai pembagi untuk i3 : "))
                hasili3 = (3*nilaiN)/pembagiI3
                print(hasili3)
            else : 
                print("perintah tidak di ketahui")
        except ValueError as err:
            print("value tidak boleh String : ",err)
        except ZeroDivisionError as err:
            print("nilai pembagi tidak boleh 0 : ",err)
    elif pilih == 4:
        print("***** rumus Untuk desil (di*n/10) *****\ndimana i =1/2/3...9")
        pilihD= str(input("masukan nilai i yang dicari(i1,i2....i9) : "))
        try:
            if pilihD == "i1":
                nilaiN = int(input("masukan nilai n :"))
                pembagiI1 = int(input("Masukan nilai pembagi untuk i1 : "))
                hasili1 = (1*nilaiN)/pembagiI1
                print(hasili1)
            elif pilihD == "i2":
                nilaiN = int(input("masukan nilai n :"))
                pembagiI2 = int(input("Masukan nilai pembagi untuk i1 : "))
                hasili2 = (2*nilaiN)/pembagiI2
                print(hasili2)
            elif pilihD == "i3":
                nilaiN = int(input("masukan nilai n :"))
                pembagiI3 = int(input("Masukan nilai pembagi untuk i1 : "))
                hasili3 = (3*nilaiN)/pembagiI3
                print(hasili3)
            elif pilihD == "i4":
                nilaiN = int(input("masukan nilai n :"))
                pembagiI4 = int(input("Masukan nilai pembagi untuk i1 : "))
                hasili4 = (4*nilaiN)/pembagiI4
                print(hasili4)
            elif pilihD == "i5":
                nilaiN = int(input("masukan nilai n :"))
                pembagiI5 = int(input("Masukan nilai pembagi untuk i1 : "))
                hasili5 = (5*nilaiN)/pembagiI5
                print(hasili5)
            elif pilihD == "i6":
                nilaiN = int(input("masukan nilai n :"))
                pembagiI6 = int(input("Masukan nilai pembagi untuk i1 : "))
                hasili6 = (6*nilaiN)/pembagiI6
                print(hasili6)
            elif pilihD == "i7":
                nilaiN = int(input("masukan nilai n :"))
                pembagiI7 = int(input("Masukan nilai pembagi untuk i1 : "))
                hasili7 = (7*nilaiN)/pembagiI7
                print(hasili7)
            elif pilihD == "i8":
                nilaiN = int(input("masukan nilai n :"))
                pembagiI8 = int(input("Masukan nilai pembagi untuk i1 : "))
                hasili8 = (8*nilaiN)/pembagiI8
                print(hasili8)
            elif pilihD == "i9":
                nilaiN = int(input("masukan nilai n :"))
                pembagiI9 = int(input("Masukan nilai pembagi untuk i1 : "))
                hasili9 = (9*nilaiN)/pembagiI9
                print(hasili9)
        except ValueError as err:
            print("value tidak boleh Stirng : ",err)
        except ZeroDivisionError as err:
            print("nilai pembagi tidak boleh 0 : ",err)
    elif pilih == 5:
        print("***** rumus Untuk desil (pi*n/100) *****\ndimana i =1/2/3...100")
        try:
            nilaiPi = int(input("masukan nilai i yang dicari(i1,i2,i3....i100) : "))
            nilaiN = int(input("masukan nilai n : "))
            pembagi = int(input("masukan nilai pembagi : "))
            hasilP = (nilaiPi*nilaiN)/100
            print(hasilP)
        except ValueError as err:
            print("value tidak boleh Stirng : ",err)
        except ZeroDivisionError as err:
            print("nilai pembagi tidak boleh 0 : ",err)
    else:
        print("perintah tidak diterima!")
except ZeroDivisionError as error:
    if pilih == 1:
        print("pembagi data tidak boleh kosong atau nol -> ",error)
    if pilih == 2:
        print("pembagi quartil tidak boleh kosong atau nol -> ",error)
    if pilih == 3:
        print("pembagi data tidak boleh kosong atau nol -> ",error)
except ValueError :
    print("nilai tidak boleh string")
else :
    print("********* program selesai *********")
finally:
    print("======== Terimakasih telah berkunjung ========") 

