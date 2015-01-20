'''
Created on 19/1/2015

@author: Carlos_Rodriguez
'''
from datetime import datetime
from Reservacion import Tarifa

def calcularCosto (fechaIn, fechaOut, tarifa):
    if fechaIn  > fechaOut:
        return 'ERROR! fecha de salida menor que fecha de entrada'
    diferencia = fechaOut - fechaIn
    if diferencia < (datetime.strptime('2000-1-1 00:15', '%Y-%m-%d %H:%M') - datetime.strptime('2000-1-1 00:00', '%Y-%m-%d %H:%M')):
        return 'ERROR! La reservacion es menor a 15 minutos'
    if diferencia > (datetime.strptime('2000-1-1 00:15', '%Y-%m-%d %H:%M') - datetime.strptime('2000-1-3 00:15', '%Y-%m-%d %H:%M')):
        return 'ERROR! La reservacion es mayor a 72 horas'
    
    
        

def reservacion (fechaIn, fechaOut, costoD, costoN):
    try:
        fecha1 = datetime.strptime(fechaIn, '%Y-%m-%d %H:%M')
        fecha2 = datetime.strptime(fechaOut, '%Y-%m-%d %H:%M')
    except ValueError:
        return 'ERROR! en las fechas introducidas'
    
    if costoD<0 or costoN<0:
        return 'ERROR! Costos no pueden ser negativos'
    else:
        tarifa = Tarifa.Tarifas (costoD, costoN)
        return calcularCosto(fecha1, fecha2, tarifa)
    
        
        