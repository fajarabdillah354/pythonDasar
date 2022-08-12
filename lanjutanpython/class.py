# contoh dasar class
from msilib.schema import PublishComponent


class manusia():
    nama="name"
    def email(self):
        print(self.nama, "mempunyai email ",self.nama, "@gmail.com")
    def asal(self, bagian):
        kota = "jakarta"
        print(self.nama," berasal dari kota ", kota , bagian)
    def alamat(self,lokasi):
        letak = "pondok gede"
        print(self.nama, "bertempat tinggal di ",letak, lokasi)    
fajar=manusia()
fajar.nama = "fajar abdillah ahmad"
print(fajar.nama)
fajar.email()
fajar.asal("timur"),fajar.alamat("jaktim")
