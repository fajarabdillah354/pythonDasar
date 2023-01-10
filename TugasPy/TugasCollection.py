# ####### ========= LIST ========== ##########
# print((30*"="),"LIST",("="*30))
# #membuat list
# fajarabdillahahmad_list = [1, 4.5 ,6, 9, 4, 8]
# fajarabdillahahmad_list2 = [20,21,32,45,56,61]
# print(fajarabdillahahmad_list)
# #akses dan slicing anggota list
# print(fajarabdillahahmad_list[4])
# print (fajarabdillahahmad_list[0:5])
# print (fajarabdillahahmad_list[:4])
# print (fajarabdillahahmad_list[-2])
# print (fajarabdillahahmad_list[2:])
# print (fajarabdillahahmad_list[2:5])
# #menambahkan anggota list dengan function append()
# fajarabdillahahmad_list.append(16)
# print (fajarabdillahahmad_list)
# fajarabdillahahmad_list3= fajarabdillahahmad_list+fajarabdillahahmad_list2
# print(fajarabdillahahmad_list3)
# #merubah data dengan langsung merubah index yang ingin di ubah
# fajarabdillahahmad_list[3]=4
# print (fajarabdillahahmad_list)
# #variabel x sama dengan variabel data
# x = fajarabdillahahmad_list
# print(x)
# x[5]=25
# print(x)
# w= x+fajarabdillahahmad_list
# print(w)

# #mencopy variabel baru
# y=fajarabdillahahmad_list2[:]
# print (y)
# print (fajarabdillahahmad_list2)
# z= y+fajarabdillahahmad_list2
# print(z)
# print()
# #list di dalam list
# fajarabdillahahmad_list4 = [fajarabdillahahmad_list, fajarabdillahahmad_list2]
# print (fajarabdillahahmad_list4)
# #akses list dalam multidimensi list
# print (fajarabdillahahmad_list4[0])
# print (fajarabdillahahmad_list4[0][3])
# print(fajarabdillahahmad_list4[1][2:5])
# #mendapatkan panjangnya list dengan function len
# print(len(fajarabdillahahmad_list4))
# print (len(fajarabdillahahmad_list2))
# #sorting pada list
# print (fajarabdillahahmad_list)
# print (sorted(fajarabdillahahmad_list))








# ####### ====== TUPLE ======== ###### 
# print((30*"="),"TUPLE",("="*30))
# # TUPLE adalah sebuaah collection yang datanya tidak bisa diubah lagi (imutable)
# fajarabdillahahmad_tuple =(1, 2, 3, 4, 5, 2,3, 2, 4)
# fajarabdillahahmad_tuple2 = (10,11,12,13,14)
# print (fajarabdillahahmad_tuple)
# #akses anggota tuple
# print (fajarabdillahahmad_tuple[2])
# print (fajarabdillahahmad_tuple[4])
# print (fajarabdillahahmad_tuple[-1])
# #melakukan pengecekan keanggotaan (in dan not in)
# print (5 in fajarabdillahahmad_tuple)
# print (6 not in fajarabdillahahmad_tuple)
# print (5 not in fajarabdillahahmad_tuple)
# #penggunaan methode count() dan index()
# print (fajarabdillahahmad_tuple.count(1))
# print (fajarabdillahahmad_tuple.count(3))
# print (fajarabdillahahmad_tuple.index(2))
# #menambahkan data dalam bentuk tuple
# fajarabdillahahmad_tuple3 = fajarabdillahahmad_tuple+fajarabdillahahmad_tuple2
# print(fajarabdillahahmad_tuple3)
# #menghapus tuple
# del fajarabdillahahmad_tuple3
# print ("---- data fajarabdillahahmad_tuple3 telah terhapus ----")
# #pengulangan tuple dengan angka
# print ("wk"*4)
# #penggunaan function
# print (len(fajarabdillahahmad_tuple))
# print (max(fajarabdillahahmad_tuple))
# print (min(fajarabdillahahmad_tuple))


# ####### ======= SET ======== ######## 
# print((30*"="),"SET",("="*30))
# # bersifat unik,JIKA ada data yang duplicate maka akan ditolak
# fajarabdillahahmad_dataset={1, 2, 3 , 4, 5 }
# fajarabdillahahmad_set1 = [1, 4.5 ,5, 3, 2, 6]
# fajarabdillahahmad_set2 = (1,2,3,4,5, 10,11,12,13,14)
# print (fajarabdillahahmad_dataset)
# fajarabdillahahmad_dataset2= set ([1, 2,3,4,5, 10,11,12,13,14])
# print (fajarabdillahahmad_dataset2)
# print(type(fajarabdillahahmad_dataset2))
# print(type(fajarabdillahahmad_set1))
# print(type(fajarabdillahahmad_set2))
# #di dalam set, anggotanya bisa berbentuk tuple tapi tidak bisa untuk list
# fajarabdillahahmad_dataset3= {"belajar", 'pemrograman', 2021, ('java','python','c')}
# print(fajarabdillahahmad_dataset3)
# #menambahkan data
# fajarabdillahahmad_dataset.add(5)
# print(fajarabdillahahmad_dataset)
# fajarabdillahahmad_dataset.add(6)
# print(fajarabdillahahmad_dataset)
# #operasi matematika gabungan, irisan
# print ()
# print (fajarabdillahahmad_dataset)
# print (fajarabdillahahmad_dataset2)
# #print (dataset.union((dataset2)))
# #print (dataset|dataset2)
# print (fajarabdillahahmad_dataset.intersection(fajarabdillahahmad_dataset2))
# print (fajarabdillahahmad_dataset.pop())
# print(fajarabdillahahmad_dataset)
# print (fajarabdillahahmad_dataset.pop())
# print(fajarabdillahahmad_dataset)
# fajarabdillahahmad_dataset.remove(4)
# print(fajarabdillahahmad_dataset)






######### ======== DICTIONIORY ======= #### 
print((30*"="),"DICTINIORY",("="*30))
#  terdapat key dan nilai
fajarabdillahahmad_dict = {
 "nama" : "Afiq",
 "jurusan" : "TI",
 "angkatan" : 2020
}
print (fajarabdillahahmad_dict)
fajarabdillahahmad_dict2 = {
 "nama" : "Dion",
 "jurusan" : "TI",
 "angkatan" : 2020,
 "hobi" : {
 "jarang" : "membaca",
 "sering" : "tidur"
 },
 "keahlian" : ("javascript","python","c","html"),
 "multilangual" : ["indonesia",'inggris','jawa','batak']
}
print (fajarabdillahahmad_dict2)
print (type(fajarabdillahahmad_dict))
# akses dengan key
print (fajarabdillahahmad_dict2['nama'])
print (fajarabdillahahmad_dict['jurusan'])
#mengubah data
fajarabdillahahmad_dict2['nama']= 'Dion Paris'
print (fajarabdillahahmad_dict2)
fajarabdillahahmad_dict2 ['jarang'] ='pernah'
print(fajarabdillahahmad_dict2)
fajarabdillahahmad_dict2 ['hobi']['jarang']='menulis'
print (fajarabdillahahmad_dict2)
fajarabdillahahmad_dict2.clear()
print(fajarabdillahahmad_dict2)
del fajarabdillahahmad_dict2
print("---- dict dengan nama fajarabdillahahmad_dict2 telah terhapus ----")


