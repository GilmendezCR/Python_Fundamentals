#Se ingresan tres valores por teclado,
#si todos son iguales se imprime la suma del primero con el segundo 
#y a este resultado se lo multiplica por el tercero.

nmr1 = int(input('Favor ingresar el valor:'))
nmr2 = int(input('Favor ingresar el valor:'))
nmr3 = int(input('Favor ingresar el valor:'))

if nmr1 == nmr2 and nmr1 == nmr3:
    suma = nmr1 + nmr2
    multiplicacion = suma * nmr3
    print(f'La suma del primer valor con respecto al segundo es:{suma} y el resultado multiplicado por el tercer valor es: {multiplicacion}')