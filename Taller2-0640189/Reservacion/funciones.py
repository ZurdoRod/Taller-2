'''
Created on 19/1/2015

@author: Carlos_Rodriguez
'''
from datetime import datetime
from Reservacion import Tarifa

def aumentarDia (fechaIn):
    dia = fechaIn.date().day
    mes = fechaIn.date().month
    anio = fechaIn.date().year
    if dia > 0 and dia < 28:
        return fechaIn.replace(day = dia + 1)
    elif dia == 29 and mes != 2:
        return fechaIn.replace(day = dia + 1)
    elif dia == 30 and (mes != 4 and mes != 6 and mes != 9 and mes != 11):
        return fechaIn.replace(day = dia + 1)
    elif dia == 31 and mes != 12:
        return fechaIn.replace(month = mes + 1, day = 1)
    elif dia == 31 and mes == 12:
        return fechaIn.replace(year = anio + 1, month = 1, day = 1)
    elif dia == 30 and (mes == 4 or mes == 6 or mes == 9 or mes == 11):
        return fechaIn.replace(month = mes + 1, day = 1)
    elif dia == 29 and mes == 2:
        return fechaIn.replace(month = mes + 1, day = 1)
    elif dia == 28 and mes == 2 and (anio % 4 == 0 or (anio % 100 == 0 and anio % 400 != 0)):
        return fechaIn.replace(day = 29)
    else:
        return fechaIn.replace(month = mes + 1, day = 1)
        
def calcularDia (fechaIn, fechaOut, fechaDia, tarifa, acum):
    return 0    #FALTA
        
    

def calcularCosto (fechaIn, fechaOut, tarifa):
    if fechaIn  > fechaOut:
        return 'ERROR! fecha de salida menor que fecha de entrada'
    diferencia = fechaOut - fechaIn
    if diferencia < (datetime.strptime('1-1-2012 00:15', '%d-%m-%Y %H:%M') - datetime.strptime('1-1-2012 00:00', '%d-%m-%Y %H:%M')):
        return 'ERROR! La reservacion es menor a 15 minutos'
    if diferencia > (datetime.strptime('4-1-2000 00:15', '%d-%m-%Y %H:%M') - datetime.strptime('1-1-2000 00:15', '%d-%m-%Y %H:%M')):
        return 'ERROR! La reservacion es mayor a 72 horas'
    
    return calcularDia(fechaIn, fechaOut, aumentarDia(fechaIn), tarifa, 0)
        

def reservacion (fechaIn, fechaOut, costoD, costoN):
    try:
        fecha1 = datetime.strptime(fechaIn, '%d-%m-%Y %H:%M')
        fecha2 = datetime.strptime(fechaOut, '%d-%m-%Y %H:%M')
    except ValueError:
        return 'ERROR! Fechas incorrectas'
    
    if costoD<0 or costoN<0:
        return 'ERROR! Costos no pueden ser negativos'
    else:
        tarifa = Tarifa.Tarifas (costoD, costoN)
        return calcularCosto(fecha1, fecha2, tarifa)
    
        
