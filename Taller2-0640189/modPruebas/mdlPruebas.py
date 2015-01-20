'''
Created on 19/1/2015

@author: Carlos_Rodriguez_06-40189
'''
import unittest
from datetime import datetime
from Reservacion import funciones

class Test(unittest.TestCase):
    
    '''
        NOTA: Las pruebas estan en orden inverso.
    '''

    def test20 (self):
        self.assertEqual(530, funciones.reservacion('31-1-2014 2:10', '1-2-2014 12:10', 10.0, 20.0), 'mas de un dia con cambio de mes')
    
    def test18 (self):
        self.assertEqual(1150, funciones.reservacion('31-12-2014 5:30', '3-1-2015 5:00', 20.0, 10.0), 'maximo de dias')

    def test17 (self):
        self.assertEqual(530, funciones.reservacion('13-10-2014 2:10', '14-10-2014 12:10', 10.0, 20.0), 'mas de un dia')

    def test16 (self):
        self.assertEqual(370, funciones.reservacion('13-10-2014 2:00', '14-10-2014 2:00', 10.0, 20.0), 'exactamente un dia')

    def test15 (self):
        self.assertEqual(430, funciones.reservacion('13-10-2014 2:10', '14-10-2014 4:15', 10.0, 20.0), 'mas de un dia')

    def test14 (self):
        self.assertEqual(370, funciones.reservacion('13-10-2014 2:10', '14-10-2014 1:55', 10.0, 20.0), '2 cambios')

    def test13 (self):
        self.assertEqual(250, funciones.reservacion('13-10-2014 2:10', '13-10-2014 19:55', 10.0, 20.0), '2 cambios')

    def test12 (self):
        self.assertEqual(150, funciones.reservacion('13-10-2014 17:45', '14-10-2014 5:55', 20.0, 10.0), 'cambio de turno diurno a nocturno')

    def test11 (self):
        self.assertEqual(100, funciones.reservacion('13-10-2014 14:45', '13-10-2014 20:25', 20.0, 10.0), 'cambio de turno diurno a nocturno')

    def test10 (self):
        self.assertEqual(20, funciones.reservacion('13-10-2014 5:25', '13-10-2014 6:20', 20.0, 10.0), 'cambio de turno nocturno a diurno')

    def test09 (self):
        self.assertEqual(100, funciones.reservacion('13-10-2014 1:25', '13-10-2014 8:20', 20.0, 10.0), 'cambio de turno nocturno a diurno')

    def test08 (self):
        self.assertEqual(20, funciones.reservacion('13-10-2014 18:30', '13-10-2014 19:35', 20.0, 10.0), 'solo nocturna, tarde')

    def test07 (self):
        self.assertEqual(70, funciones.reservacion('13-10-2014 18:30', '14-10-2014 00:35', 20.0, 10.0), 'solo nocturna, cambio dia')

    def test06 (self):
        self.assertEqual(50, funciones.reservacion('13-10-2014 2:30', '13-10-2014 5:40', 20.0, 10.0), 'nocturna + intermedia')

    def test05 (self):
        self.assertEqual(240, funciones.reservacion('13-10-2014 6:05', '13-10-2014 17:15', 20.0, 10.0), 'diurna + intermedia')

    def test04 (self):
        self.assertEqual(220, funciones.reservacion('13-10-2014 6:05', '13-10-2014 17:05', 20.0, 10.0), 'solo diurna')

    def test03 (self):
        self.assertEqual(220, funciones.reservacion('13-10-2014 6:05', '13-10-2014 16:10', 20.0, 10.0), 'solo diurna')

    def test02 (self):
        self.assertEqual(20, funciones.reservacion('13-10-2014 2:30', '13-10-2014 4:00', 20.0, 10.0), 'solo nocturna')

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
    
