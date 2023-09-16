import unittest

# from my folder def import my program
from my_sum import sum

class TestSum(unittest.TestCase): # usando la libreria unittest
    def test_list_int(self):
        '''
        Test that it can sum a list of integers
        '''
        data = [1, 2, 3]
        result = sum(data)

        self.assertEqual(result, 6)

    def test_tutple_int(self):
        '''
        probando si funciona la suma de tuplas
        '''
        datatupla = (1, 2, 3)
        result = sum(datatupla)

        self.assertEqual(result, 6)

    def test_list_float(self):
        '''
        probando la  suma de flotantes
        '''
        datalistfloat = [1.0, 2.0, 3.0]
        result = sum(datalistfloat)

        self.assertEqual(result, 6)
        

if __name__ == '__main__':
    unittest.main()
