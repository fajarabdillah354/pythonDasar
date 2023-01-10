class Buku :
    def __init__(self,judulBuku,penerbit,tahunTerbit):
        self.judulBuku = judulBuku
        self.penerbit = penerbit
        self.tahunTerbit = tahunTerbit
buku1=Buku("Atomic Habbit","WC.donkey",2021)
buku2=Buku("Mindset","Gramedia",2019)
print("buku yang saya punya adalah : "+buku1.judulBuku)