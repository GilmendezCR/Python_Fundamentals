#Realizar un programa que pida cargar una fecha cualquiera, luego verificar si dicha fecha corresponde a Navidad.

dia = input('Ingrese el dia')
mes = input('Ingrese el mes')
año = input('Ingrese el año')

if dia == '25' and mes == '12' and año == '2021':
    print('Es navidad')
else:
    print('No es navidad')