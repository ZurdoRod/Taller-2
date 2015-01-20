'''
Created on 19/1/2015

@author: ZurdoRod
'''
import unittest
from datetime import datetime
from Reservacion import funciones

class Test(unittest.TestCase):
    
#    def test03 (self):
#        self.assertEqual(80, funciones.reservacion('13-10-2014 2:00', '13-10-2014 8:45', 20.0, 10.0), 'diurna-nocturna')
    
    def test02 (self):
        self.assertEqual(80, funciones.reservacion('13-10-2014 2:00', '13-10-2014 8:00', 20.0, 10.0), 'diurna-nocturna')

    def test01 (self):
        self.assertEqual(30, funciones.reservacion('13-10-2014 2:30', '13-10-2014 4:35', 20.0, 10.0), 'solo nocturna')
        
    def testDiaMasMas4 (self):
        self.assertEqual(datetime.strptime('2-5-2012 00:15', '%d-%m-%Y %H:%M'), funciones.aumentarDia(datetime.strptime('1-5-2012 00:15', '%d-%m-%Y %H:%M')), 'Aumentar un dia a mes')
        
    def testDiaMasMas3 (self):
        self.assertEqual(datetime.strptime('1-6-2012 00:15', '%d-%m-%Y %H:%M'), funciones.aumentarDia(datetime.strptime('31-5-2012 00:15', '%d-%m-%Y %H:%M')), 'Aumentar un dia a mes de 31')
        
    def testDiaMasMas2 (self):
        self.assertEqual(datetime.strptime('1-5-2012 00:15', '%d-%m-%Y %H:%M'), funciones.aumentarDia(datetime.strptime('30-4-2012 00:15', '%d-%m-%Y %H:%M')), 'Aumentar un dia a mes de 30')
        
    def testDiaMasMas (self):
        self.assertEqual(datetime.strptime('1-1-2012 00:15', '%d-%m-%Y %H:%M'), funciones.aumentarDia(datetime.strptime('31-12-2011 00:15', '%d-%m-%Y %H:%M')), 'Aumentar un dia a diciembre')
        
    def testfechaIncorrecta(self):
        self.assertEqual('ERROR! Fechas incorrectas', funciones.reservacion('1-0-1 00:10', '2-4-2000',  40.0,   20.0), 'mes invalido')

    def testfechaMenor(self):
        self.assertEqual('ERROR! La reservacion es menor a 15 minutos', funciones.reservacion('12-12-2012 01:20','12-12-2012 01:30', 12.0, 20.0), 'La reservacion es menor a 15 minutos')
        
    def testfechaMayor(self):
        self.assertEqual('ERROR! La reservacion es mayor a 72 horas', funciones.reservacion('12-12-2012 01:20','15-12-2012 01:30', 12.0, 20.0), 'La reservacion es mayor a 72 horas')
        


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testfechaMenor']
    unittest.main()
    
