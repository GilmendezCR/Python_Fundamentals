#Se ingresa por teclado un número positivo de uno o dos dígitos (1..99)
# mostrar un mensaje indicando si el número tiene uno o dos dígitos.
#(Tener en cuenta que condición debe cumplirse para tener dos dígitos un número entero)

numero = int(input('Favor ingresar el valor positivo:'))

if numero < 10:
    print('El numero tiene solo un digito')
elif numero >= 10 and numero < 100:
    print('El numero tiene dos digitos')
else:
    print('Error')