'''
=================================================
Graded Challenge 1

Nama  : Naufal Andika Ramadhan
Batch : HCK-14

Program ini dibuat untuk me-manage keranjang belanja dengan menambah item,
mengurangi item, men-display keranjang belanjaan, dan menghitung total belanja
=================================================
'''
class CartItem():                       # membuat class 'CartItem()'
    '''
        __init__ = constructor executed saat class CartItem dipanggil
    '''
    def __init__(self, name, price):    # membuat objek dalam class 'CartItem()' dengan atribut 'name' dan 'price'
        self.name = name                # pembuatan variable baru 'name' dari atribut 'self.name'
        self.price = price              # pembuatan variable baru 'price' dari atribut 'self.price'

class ShoppingCart(CartItem):           # membuat class 'ShoppingCart' dengan 'CartItem' sebagai parent
    def __init__(self):                 # membuat objek dalam class 'ShoppingCart()'
        self.itemList = []              # pembuatan empty list '[]' untuk menampung hasil input data dari user
    
    def addItem(self, name, price):
        '''
            Digunakan untuk memasukkan 'name' dan 'price' ke dalam itemList
            melalui input kedalam class ShoppingCart 'self.itemList = []'
        '''
        itemList = CartItem(name, price)                                # itemList diisi dengan class CartItem dan dengan atribut 'name' dan 'price'                            
        self.itemList.append(itemList)                                  # atribut 'name' dan 'price' akan ditambahkan kedalam itemList
        print(f'Barang {name} telah dimasukkan ke dalam keranjang')     # print 'name' yang telah diinput
    
    def removeItem(self, name):
        '''
            Digunakan untuk menghapus 'name' dari itemList melalui
            input kedalam class ShoppingCart 'self.itemList = []'
        '''
        for index in self.itemList:                                     # memanggil index data dari itemList yang sudah disimpan
            if (name == index.name):                                    # jika 'name' yang diinput sesuai dengan index data maka akan di remove dari itemList
                self.itemList.remove(index)
                print(f'Barang: {name} berhasil dihapus dari keranjang')
            else:
                print(f'Barang {name} tidak ditemukan di keranjang')
            

    def displayCart(self):
        '''
            Digunakan untuk menampilkan 'name' dan 'price' yang sudah tersimpan didalam list itemList
        '''
        print('Barang yang di keranjang : ')
        for index in self.itemList:                                     # memanggil index data dari itemList yang sudah disimpan
            print(f'{index.name} - Rp. {index.price}')                  # index data dari atribut 'name' dan 'price' di print
    
    def totalShopping(self):
        '''
            Digunakan untuk menjumlah total belanjaan didalam itemList
        '''
        totalPrice = 0                                                  # membuat variable baru 'totalPrice' = (0) untuk penambah dari index 'price' yang sudah tersimpan di itemList
        for index in self.itemList:                                     # memanggil index data dari itemList yang sudah disimpan
            totalPrice += index.price                                   # totalPrice yang sebelumnya (0) akan ditambahkan index 'price' ke data yang disimpan di itemList

        print(f'Total belanja:  {totalPrice}')                          # print totalPrice
        return totalPrice                                               # pengembalian nilai baru yang dihasilkan dari 'totalPrice' ke 'itemList'

    def displayMenu(self):
        '''
            Digunakan untuk menunjukkan user interface dari menu
        '''
        print('''
Selamat Datang di Keranjang Belanja Toko Makmur!
              
Menu:
1. Menambah Barang
2. Hapus Barang
3. Tampilkan Barang di Keranjang
4. Lihat Total Belanja
5. Exit
              ''')

if __name__ == '__main__':
    sc = ShoppingCart()                                         # membuat variable baru dengan nama 'sc' dari class 'ShoppingCart' untuk menghindari kerancuan

    while True:                                                 # jika input nya 1,2,3,4,5 akan dinilai true dan akan menjalankan fungsi yang sesuai
        sc.displayMenu()                                        # men-display atau print menu
        print ('Pilih menu!')
        selectedMenu = int(input())                             # variable 'selectedMenu' dengan input yang diterima adalah integer
        
        if selectedMenu == 1:                                   # jika input yang diberikan adalah 1
            name = str(input('Masukkan nama barang: '))         # input dari perintah 'Masukkan nama barang:' akan disimpan dengan variable 'name'
            price = int(input('Masukkan harga barang: '))       # input dari perintah 'Masukkan harga barang:' akan disimpan dengan variable 'price'
            sc.addItem(name, price)                             # menjalankan fungsi 'addItem' dari class 'ShoppingCart'
            print('Barang ' f'{name}' ' telah ditambahkan!')    # print 'Barang telah ditambahkan!' dengan menjalankan function f untuk dapat memanggil nama barang dari 'itemList'
        
        elif selectedMenu == 2:                                 # jika input yang diberikan adalah 2
            print ('Masukkan nama barang yang ingin dihapus')    
            name = str(input(''))                               # input dari perintah 'Masukkan nama barang yang ingin dihapus' akan memanggil variable 'name'
            sc.removeItem(name)                                 # menjalankan fungsi 'removeItem' dari class 'ShoppingCart'
        
        elif selectedMenu == 3:                                 # jika input yang diberikan adalah 3
            sc.displayCart()                                    # menjalankan fungsi 'displayCart' dari class 'ShoppingCart'
            if len(sc.itemList) == 0:                           # jika tidak ada data didalam 'itemList'
                print('Keranjang belanjaan kosong')             # print 'keranjang belanjaan kosong'
        
        elif selectedMenu == 4:                                 # jika input yang diberikan adalah 4
            sc.totalShopping()                                  # menjalankan fungsi 'totalShopping' dari class 'ShoppingCart'
            
        elif selectedMenu == 5:                                 # jika input yang diberikan adalah 5
            print('Terima kasih sudah berbelanja')              # print 'terima kasih sudah berbelanja'
            break                                               # menghentikkan looping app
        
        else:                                                   # jika input tidak sesuai dengan pilihan 1,2,3,4,5
            print('Masukkan nomor yang sesuai dengan menu')     # akan looping kembali ke menu awal dan memberikan pesan 'masukkan nomor yang sesuai dengan menu'