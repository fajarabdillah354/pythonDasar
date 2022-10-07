def get_biodata():
    nama = input('input nama: ')
    alamat = input('input alamat: ')
    ttl = input('input tempat dan tanggal lahir: ')
    pekerjaan = input('input pekerjaan: ')
    status = input('input status: ')
    print('================================')
    print('Biodata anda adalah: ')
    print('nama: ' + nama)
    print('alamat: ' + alamat)
    print('ttl: ' + ttl)
    print('pekerjaan: ' + pekerjaan)
    print('status: ' + status)
		
print('==================================')
 

def run():
    while True:
        get_biodata()
        input_again = input('apakah input lagi? (y/n): ')
        if input_again == 'y':
            continue
        elif input_again == 'n':
            break
 
if __name__ == '__main__':
    run()