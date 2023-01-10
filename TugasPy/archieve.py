import zipfile

# Buat objek ZipFile baru
with zipfile.ZipFile('fajar_arsip.zip', 'w') as zip:
   # Daftar nama file yang akan ditambahkan ke dalam arsip zip
   file_list = ['read.txt', 'biodata.txt']
   # Tambahkan file ke dalam arsip zip
   for file in file_list:
       zip.write(file)

# Buka arsip zip
with zipfile.ZipFile('fajar_arsip.zip', 'r') as zip:
   # Cetak daftar nama file di dalam arsip zip
   print(zip.namelist())
   # Baca file pertama di dalam arsip zip
   data = zip.read(zip.namelist()[0])
   print(data)













# import xlwt
# sekolah = ['SDN Jaticempaka', 'SDN Cipinang Melayu', 'SDN Duren Sawit']#isi data
# letak = ['Jakarta Timur', 'Jakarta Utara', 'Jakarta Timur']#isi data
# book = xlwt.Workbook()#penggunaan module xlwt
# ws = book.add_sheet("SEKOLAH DASAR")#membuat sheet dengan nama SEKOLAH DASAR
# ws.write(0,0, 'Nama Sekolah Dasar')#menempatkan nama sekolah pada kolam 0 baris 0
# ws.write(0,1,'Kota')#menempatkan nama kota pada kolam 0 baris 1
# i=1
# for x,y in zip(sekolah,letak):#looping
#     ws.write(i,0,x)
#     ws.write(i,1,y)
#     i+=1
# print('DATA TELAH TERSIMPAN')#jika sukses tersimpan maka akan diprint
# book.save("dataSekolah.xls")#save dengan nama dataSekolah
