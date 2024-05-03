from naufal_app import ShoppingCart             
import unittest                                

class ShoppingCartTesting(unittest.TestCase): 
    def test_addItem(self):                   
        '''
            Untuk menjalankan test addItem
        '''
        sc = ShoppingCart()                     
        sc.addItem ('Apel', 5000)
        self.assertEqual(len(sc.itemList), 1)

    def test_removeItem(self):
        '''
            Untuk menjalankan test removeItem
        '''
        sc = ShoppingCart()
        sc.addItem('Apel', 5000)
        sc.removeItem('Apel')
        self.assertEqual(len(sc.itemList), 0)
    
    def test_Total(self):
        '''
            Untuk menjalankan test Total
        '''
        sc = ShoppingCart()
        sc.addItem('Apel', 5000)
        sc.addItem('Pisang', 2500)
        sc.addItem('Anggur', 10000)
        total_belanja = sc.totalShopping()
        self.assertEqual(total_belanja, 17500)

if __name__ == '__main__':
    unittest.main()