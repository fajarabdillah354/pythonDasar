import xlrd#penggunaan module xlrd

data = {}#buat list
data_file = xlrd.open_workbook("dataSekolah.xls")#membuka file dengan nama dataSekolah
data_sheet = data_file.sheet_by_index(0)
jumlah_baris = data_sheet.nrows#untuk membuat baris baru
for i in range(1, jumlah_baris):#looping
    #isi looping
    data[data_sheet.cell_value(rowx =i, colx =0)] = data_sheet.cell_value(rowx =i, colx=1)
print(data)#mencetak hasil file
