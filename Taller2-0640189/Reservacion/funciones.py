'''
Created on 19/1/2015

@author: Carlos_Rodriguez
'''
from datetime import datetime
from Reservacion import Tarifa

def calcularCosto (fechaIn, fechaOut, tarifa):
    return 0

def reservacion (fechaIn, fechaOut, costoD, costoN):
    try:
        fecha1 = datetime.datetime.strptime(fechaIn, '%Y-%m-%dT%H:%M')
        fecha2 = datetime.datetime.strptime(fechaOut, '%Y-%m-%dT%H:%M')
    except ValueError:
        return 'ERROR en las fechas introducidas'
    
    if costoD<0 or costoN<0:
        return 'ERROR! Costos no pueden ser negativos'
    tarifa = Tarifa (costoD, costoN)
    return calcularCosto(fecha1, fecha2, tarifa)
    
        
        