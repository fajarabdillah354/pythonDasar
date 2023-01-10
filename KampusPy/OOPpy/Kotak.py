from ctypes.wintypes import PLARGE_INTEGER


class Kotak :
    def __init__(self,p,t,l) :
        self.panjang = p
        self.tinggi = t
        self.lebar = l
    def hitungVolume(self):
        return self.panjang * self.tinggi * self.lebar
    def cetakData(self):
        print("panjang\t : ",self.panjang)
        print("lebar\t : ",self.lebar)
        print("tinggi\t : ",self.tinggi)
    def cetakVolum(self):
        print("Volume\t : ",self.hitungVolume())
kotak1 = Kotak(6,9,2)
x = Kotak(11,13,9)

print("Object kotak 1 memiliki :")
kotak1.cetakData()
kotak1.cetakVolum()

print("="*50)

class Segitiga:
    def __init__(self,a,t) :
        self.tinggi = t
        self.alas = a
    def hitungLuas(self):
        return (self.alas * self.tinggi)/2
    def cetakData(self):
        print("tinggi\t : ",self.tinggi)
        print("alas\t : ",self.alas)
    def cetakLuas(self):
        print("Luas\t : ",self.hitungLuas())
segitiga1 = Segitiga(3,8)
x=Segitiga(3,8)

print("Object Segitiga 1 memiliki : ")
segitiga1.cetakData()
segitiga1.cetakLuas()

