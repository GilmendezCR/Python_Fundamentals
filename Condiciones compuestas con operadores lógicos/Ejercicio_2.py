#Se ingresan por teclado tres números,
#si todos los valores ingresados son menores a 10, 
#imprimir en pantalla la leyenda "Todos los números son menores a diez".

nmr1 = int(input('Ingrese el numero:'))
nmr2 = int(input('Ingrese el numero:'))
nmr3 = int(input('Ingrese el numero:'))

if nmr1 < 10 and nmr2 < 10 and nmr3 < 10:
    print('Todos los numeros son menos a diez')
else:
    print('Error')