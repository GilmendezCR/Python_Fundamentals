#Confeccionar un programa que permita cargar un número entero positivo de hasta tres cifras
#y muestre un mensaje indicando si tiene 1, 2, o 3 cifras.
#Mostrar un mensaje de error si el número de cifras es mayor.

numero = int(input('Ingrese el valor:'))
if numero > 0 and numero < 10:
    print('Es un valor de 1 digito')
elif numero > 10 and numero < 100:
    print('Es un valor de 2 digitos')
elif numero > 100 and numero < 1000:
    print('Es un valor de 3 digitos')
else:
    print('Error')