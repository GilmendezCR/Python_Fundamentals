#Se ingresan por teclado tres números,
#si al menos uno de los valores ingresados es menor a 10, 
#imprimir en pantalla la leyenda "Alguno de los números es menor a diez".

nmr1 = int(input('Ingrese el valor'))
nmr2 = int(input('Ingrese el valor'))
nmr3 = int(input('Ingrese el valor'))

if nmr1 < 10 or nmr2 < 10 or nmr3 < 10:
    print('Alguno de los numeros es nenor a diez')