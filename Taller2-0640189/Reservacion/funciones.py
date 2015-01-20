'''
Created on 19/1/2015

@author: Carlos_Rodriguez_06-40189
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
    t = 0
    fechaDiurno = fechaIn.replace(hour = 6, minute = 0)
    fechaNocturno = fechaIn.replace(hour = 18, minute = 0)
    if fechaIn < fechaDiurno and fechaOut < fechaDiurno:
        t = (fechaOut.time().hour - fechaIn.time().hour) * tarifa.tn
        if fechaOut.time().minute > fechaIn.time().minute and fechaOut.time().hour < 5:
            t = t + tarifa.tn
        elif fechaOut.time().minute > fechaIn.time().minute and fechaOut.time().hour == 5:
            t = t + tarifa.ti
        return acum + t
    elif fechaIn >= fechaDiurno and fechaIn < fechaNocturno and fechaOut >= fechaDiurno and fechaOut < fechaNocturno:
        t = (fechaOut.time().hour - fechaIn.time().hour) * tarifa.td
        if fechaOut.time().minute > fechaIn.time().minute and fechaOut.time().hour < 17:
            t = t + tarifa.td
        elif fechaOut.time().minute > fechaIn.time().minute and fechaOut.time().hour == 17:
            t = t + tarifa.ti
        return acum + t
    elif fechaIn >= fechaNocturno and fechaOut < aumentarDia(fechaNocturno):
        t = fechaOut.time().hour - fechaIn.time().hour
        if t < 0:
            t = t + 24
        t = t * tarifa.tn
        if fechaOut.time().minute > fechaIn.time().minute and fechaOut.time().hour < 5:
            t = t + tarifa.tn
        elif fechaOut.time().minute > fechaIn.time().minute and fechaOut.time().hour == 5:
            t = t + tarifa.ti
        elif fechaOut.time().minute > fechaIn.time().minute and fechaOut.time().hour < 24:
            t = t + tarifa.tn
        return acum + t
    elif fechaIn < fechaDiurno and fechaOut < fechaNocturno:
        return acum + calcularDia(fechaIn, fechaDiurno.replace(hour = 5, minute = fechaIn.time().minute), None, tarifa, 0) + calcularDia (fechaDiurno.replace(minute = fechaIn.time().minute), fechaOut, None, tarifa, 0) + tarifa.ti 
    elif fechaIn < fechaDiurno and fechaOut < aumentarDia(fechaDiurno):
        return acum + calcularDia(fechaIn, fechaDiurno.replace(hour = 5, minute = fechaIn.time().minute), None, tarifa, 0) + calcularDia (fechaDiurno.replace(minute = fechaIn.time().minute), fechaNocturno.replace(hour = 17, minute = fechaIn.time().minute), None, tarifa, 0) + calcularDia (fechaNocturno, fechaOut, aumentarDia(fechaOut), tarifa, 0) + 2*tarifa.ti
    elif fechaIn < fechaNocturno and fechaOut < aumentarDia(fechaDiurno):
        return acum + calcularDia(fechaIn, fechaNocturno.replace(hour = 17, minute = fechaIn.time().minute), None, tarifa, 0) + calcularDia (fechaNocturno.replace(minute = fechaIn.time().minute), fechaOut, None, tarifa, 0) + tarifa.ti
    elif fechaIn < fechaDiurno and fechaOut <  fechaDia:
        return acum + calcularDia(fechaDiurno, fechaDiurno.replace(hour = 5, minute = fechaIn.time().minute), None, tarifa, 0) + calcularDia (fechaDiurno.replace(minute = fechaIn.time().minute), fechaNocturno.replace(hour = 17, minute = fechaIn.time().minute), None, tarifa, 0) + (fechaNocturno.replace(minute = fechaIn.time().minute), fechaOut, None, tarifa, 0) + 2*tarifa.ti
    elif fechaOut > fechaDia:
        return acum + calcularDia(fechaIn, fechaDia, fechaDia, tarifa, 0) + calcularDia(fechaDia, fechaOut, aumentarDia(fechaDia), tarifa, 0)
    return 0
    

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
    
        
