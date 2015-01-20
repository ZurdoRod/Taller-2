'''
Created on 19/1/2015

@author: ZurdoRod
'''
import unittest
from Reservacion import funciones

class Test(unittest.TestCase):


    def testfechaMenor(self):
        self.assertEqual('ERROR! La reservacion es menor a 15 minutos', funciones.reservacion('2012-12-12 01:20','2012-12-12 01:30', 12.0, 20.0), 'La reservacion es menor a 15 minutos')
        
    def testfechaMayor(self):
        self.assertEqual('ERROR! La reservacion es mayor a 72 horas', funciones.reservacion('2012-12-12 01:20','2012-12-12 01:30', 12.0, 20.0), 'La reservacion es mayor a 72 horas')



if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testfechaMenor']
    unittest.main()
    
