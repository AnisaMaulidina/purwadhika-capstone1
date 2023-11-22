from tabulate import tabulate

# Database Buku di Sebuah Perpustakaan
listBuku = [
    {'ID_Buku': 1407, 'Genre': 'Novel', 'Judul': 'Gadis Kretek', 'Penulis': 'Ratih Komala', 'Stock Buku': 2},
    {'ID_Buku': 1409, 'Genre': 'Novel', 'Judul': 'Dear Nathan', 'Penulis' : 'Nada Arumi', 'Stock Buku': 1},
    {'ID_Buku': 1501, 'Genre': 'Bahasa', 'Judul': 'IELTS 2023', 'Penulis' : 'Proyo Suhadi', 'Stock Buku': 5},
    {'ID_Buku': 1602, 'Genre': 'Teknik', 'Judul': 'Geodesi dan Geomatika', 'Penulis' : 'Joenil Kahar', 'Stock Buku': 3},
    {'ID_Buku': 1604, 'Genre': 'Teknik', 'Judul': 'Ilmu Fotogramteri dan Pengalikasiannya', 'Penulis' : 'Hasanuddin', 'Stock Buku': 4}
]

# menampilkan Daftar Buku dalam Bentuk Tabel
def Displaytabel(listBuku):
    headers = listBuku[0].keys()
    rows = [book.values() for book in listBuku]
    print(tabulate(rows, headers=headers, tablefmt='grid'))

#  Menampilakn Daftar Buku Sesuai dengan Genre
def tampilkan_genre(listBuku):
    genre_input = input("Masukkan genre buku yang ingin ditampilkan: ")
    buku_genre_tertentu = [buku for buku in listBuku if buku['Genre'] == genre_input] #Membuat list baru untuk menampung buku dengan genre yang sesuai
    if buku_genre_tertentu:
        print("Daftar buku dengan genre '{}':".format(genre_input))
        for buku in buku_genre_tertentu:
            print(f"ID: {buku['ID_Buku']} | Judul: {buku['Judul']} | Penulis: {buku['Penulis']} | Stock: {buku['Stock Buku']}")
    else:
        print(f"Tidak ada buku dengan genre '{genre_input}' dalam daftar.")

peminjaman = [] #untuk menyimpan database peminjam

# Database Peminjam 
def databasepeminjam(listBuku, peminjaman):
    while True:
        print(' Anda Hanya Bisa Meminjam 1 Buku!')
        ID_buku = int(input('Masukkan ID Buku Yang Ingin Anda Pinjam : '))
        ID_peminjam = int(input('Masukkan ID Anda : '))
        nama_peminjam = input('Masukkan Nama Peminjam: ')
        tanggal_peminjaman = input('Masukkan Tanggal Peminjaman (Format YYYY-MM-DD): ')

        # Mengecek apakah ID buku ada dalam listBuku
        existing_ids = [buku['ID_Buku'] for buku in listBuku]
        if ID_buku in existing_ids:
            # Menemukan informasi buku yang cocok dengan ID yang dimasukkan
            book = next((buku for buku in listBuku if buku['ID_Buku'] == ID_buku), None)
            if book:
                sure = input('Apakah Anda Ingin Meminjam Buku dengan ID {} | Genre {} | Judul : {} ? (Y/N) '.format(book['ID_Buku'], book['Genre'], book['Judul']))
                if sure.upper() == 'Y':
                    peminjaman_baru = {
                        'ID_Peminjam': ID_peminjam,
                        'Nama_Peminjam': nama_peminjam,
                        'ID_Buku': ID_buku,
                        'Tanggal_Peminjaman': tanggal_peminjaman
                    }
                    peminjaman.append(peminjaman_baru)  # Simpan entri peminjaman baru ke dalam database peminjaman
                    print('Data peminjaman berhasil disimpan, Silahkan Ambil Buku yang Akan Anda Pinjam !!')
                    break  # Keluar dari loop setelah data disimpan
                else:
                    print('Peminjaman buku dibatalkan.')
            else:
                print('Informasi buku tidak ditemukan.')
        else:
            print('ID Buku tidak ditemukan dalam daftar buku. Masukkan ID Buku yang valid.')

# filter dictionary untuk mencari daftar buku
def search(input):
    search = (list(filter(lambda data : data ['Judul'] == (input), listBuku)))
    return search

# membaca daftar buku
def menuread():
    while True:
        inputread = input('''
            Menu Daftar Buku
            1. Menampilkan Seluruh Daftar Buku
            2. Menampilkan Daftar Buku Sesuai Genre
            3. Mencari Daftar Buku
            4. Kembali ke Menu Utama
            Pilih Menu Yang Anda Inginkan: ''')

        if inputread == '1' and len(listBuku):
            Displaytabel(listBuku)
        elif inputread == '2' and len(listBuku):
            tampilkan_genre(listBuku)
        elif inputread == '3' and len(listBuku):
            caribuku = input('Masukkan Judul Yang Ingin di Cari: ')
            hasil_cari = search(caribuku)
            if len(hasil_cari):
                Displaytabel(hasil_cari)
            else:
                print('Buku dengan judul yang anda inginkan tidak ada')
        elif inputread == '4':
            # Jika ingin kembali ke menu utama, bisa menggunakan 'break' untuk keluar dari loop 'while'
            break
        else:
            print('Data Tidak Ditemukan')

# menambah daftar buku
def tambahBuku():
    userinputadd = input('''
            Menu Menambahkan Buku Baru : 
                1. Menambahkan Buku Baru ke dalam Daftar Buku
                2. Kembali Ke Menu Utama 
            Pilih Menu yang Anda Inginkan : ''' )
    if userinputadd == '1':  
        masukanID = (int(input('Masukan ID Buku Baru : ')))
        existing_ids = [buku['ID_Buku'] for buku in listBuku] # memerikasa apakah ID sudah ada dalam daftar buku
        if masukanID in existing_ids:
            print("ID sudah ada dalam daftar buku!")
            tambahBuku()
        else :
            buku_baru = {'ID_Buku' : masukanID}  
            buku_baru['Genre'] = input('Masukkan Genre Buku baru: ')
            buku_baru['Judul'] = input('Masukkan Judul Buku baru: ')
            buku_baru['Penulis'] = input('Masukkan Nama Penulis Buku baru: ')
            buku_baru['Stock Buku'] = int(input('Masukkan Stok Buku baru: '))

        listBuku.append(buku_baru)  # Menambahkan buku baru ke dalam listBuku
        print('Buku baru berhasil ditambahkahkan! Silahkan Lihat Daftar Buku Terbaru di Bawah ini') 
        Displaytabel(listBuku)
        tambahBuku()
    elif userinputadd == '2' :
        Mainmenu()

# menghapus daftar buku
def delete() : 
    inputdelete = input('''
            Menu Mengapus Data Buku : 
                1. Menghapus Data Buku
                2. Kembali Ke Menu Utama 
            Pilih Menu yang Anda Inginkan : ''' )
    if inputdelete == '1' :
        Displaytabel(listBuku)
        deletedata = (int(input('Masukan ID buku yang ingin anda hapus : ')))
        existing_ids = [buku['ID_Buku'] for buku in listBuku]
        if deletedata in existing_ids:
            index_to_delete = existing_ids.index(deletedata)
            answer = input("Apakah anda yakin untuk mengubah data buku ini ? Y/N : " )
            if answer == 'Y' :
                del listBuku[index_to_delete]
                print("Buku dengan ID {} berhasil dihapus" .format(deletedata))
                Displaytabel(listBuku)
                delete()
            elif answer == 'N' :
                print("Penghapusan data buku dibatalkan.")
                delete()
        else:
            print("ID buku tidak ditemukan dalam daftar.")
            delete()
    elif inputdelete == '2': 
        Mainmenu()

# memperbarui daftar buku
def update() :
    inputbarui = input('''
            Menu Memperbarui Data Buku : 
                1. Memperbarui Data Buku 
                2. Kembali Ke Menu Utama 
            Pilih Menu yang Anda Inginkan : ''' )
    if inputbarui == '1' :
        Displaytabel(listBuku)
        updatedata = (int(input('Masukan ID buku yang ingin diubah : ')))
        existing_ids = [buku['ID_Buku'] for buku in listBuku] # memerikasa apakah ID sudah ada dalam daftar buku
        if updatedata in existing_ids:
            index_to_update = existing_ids.index(updatedata)
            answer = input("Apakah anda yakin untuk mengubah data buku ini ? Y/N : " )
            if answer.upper() == 'Y' :
                kategori = input('''Apa yang akan anda ubah ?  '
                                1. ID Buku
                                2. Genre
                                3. Judul
                                4. Penulis
                                5. Stock Buku
                                Pilih Ketegori yang akan diubah : ''')
                if kategori == '1':
                    new_id = int(input('Masukkan ID Buku Baru : '))
                    listBuku[index_to_update]['ID_Buku'] = new_id
                    print('Pembaruan Berhasil!!')
                    Displaytabel(listBuku)
                    update()
                elif kategori == '2':
                    new_genre = input('Masukkan Genre Baru : ')
                    listBuku[index_to_update]['Genre'] = new_genre
                    print('Pembaruan Berhasil!!')
                elif kategori == '3':
                    new_title = input('Masukkan Judul Baru : ')
                    listBuku[index_to_update]['Judul'] = new_title
                    print('Pembaruan Berhasil!!')
                    update()
                elif kategori == '4':
                    new_author = input('Masukkan Penulis Baru : ')
                    listBuku[index_to_update]['Penulis'] = new_author
                    print('Pembaruan Berhasil!!')
                    update()
                elif kategori == '5':
                    new_stock = int(input('Masukkan Stock Baru : '))
                    listBuku[index_to_update]['Stock Buku'] = new_stock
                    print('Pembaruan Berhasil!!')
                    update()
                else:
                    print("Pilihan tidak valid!")
                    update()
            else :
                print('Pembaruan dibatalkan')
                update()
        else:
            print("ID Buku tidak valid, Pembaruan dibatalkan.")
            update()
    elif inputbarui == '2' :
        Mainmenu()
    else :
        print('Pilihan Tidak Valid!!!')
        update()
   
# fungsi untuk meminjam buku
def borrow():
    while True:
        input_br = input('''
            Menu Meminjam Buku : 
                1. Meminjam Buku 
                2. Kembali Ke Menu
            Pilih Menu yang Anda Inginkan : ''')
        
        if input_br == '1':
            Displaytabel(listBuku)
            databasepeminjam(listBuku, peminjaman)  
        elif input_br == '2':
            break  # Keluar dari fungsi dan kembali ke menu utama 
        else:
            print("Pilihan tidak valid. Silakan pilih menu yang sesuai.")
    
# fungsi untuk mengembalikan buku
def return_book():
    input_ID_peminjam = int(input('Masukkan ID Peminjam: '))
    found = False

    for peminjam_data in peminjaman:
        if peminjam_data['ID_Peminjam'] == input_ID_peminjam:
            found = True
            print('Pengembalian buku oleh ID Peminjam {} - {}'.format(input_ID_peminjam, peminjam_data['Nama_Peminjam']))
            print("ID Buku yang dipinjam: {}" .format(peminjam_data['ID_Buku']))

            peminjaman.remove(peminjam_data)  # tanda buku sebagai dikembalikan dengan menghapus entri dari database peminjaman
            print("Buku berhasil dikembalikan.")
            

    if not found:
        print("ID Peminjam tidak ditemukan dalam database peminjaman.")

#  Fungsi Menu Utama
def Mainmenu():
    while True:
        choice = input('''
            Selamat Datang di Sistem Data dan Informasi Perpustakaan Lestari

            Pilih Menu Yang Anda :
            1. Menampilkan List Buku
            2. Tambahkan Buku
            3. Delete Data Buku
            4. Update Data Buku
            5. Pinjam Buku
            6. Pengembalian Buku
            7. Exit 

            Masukkan angka Menu yang ingin dijalankan: ''')

        if choice == '1':
            menuread()
        elif choice == '2' :
            tambahBuku()
        elif choice == '3' :
            delete()
        elif choice == '4':
            update()
        elif choice == '5':
            borrow()
        elif choice == '6' :
            return_book()
        elif choice == '7':
            break
        else:
            print('Invalid Choice')

# Memanggil fungsi utama untuk menjalankan program
Mainmenu()