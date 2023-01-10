sudah kelar
a = int(input("masukan tinggi bintang : "))
for i in range(0,a):
    for j in range(0,i+1):
        print("*",end='')
    print('')
for i in range(0,a):
    for j in range(0,a-1):
        print("*",end='')
    a-=1
    print('')