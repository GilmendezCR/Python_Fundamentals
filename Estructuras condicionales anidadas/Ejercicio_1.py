#Se cargan por teclado tres números distintos.
#Mostrar por pantalla el mayor de ellos.

numero1 = int(input('Favor ingresar el valor'))
numero2 = int(input('Favor ingresar el valor'))
numero3 = int(input('Favor ingresar el valor'))

if numero1 > numero2 and numero1 > numero3:
    print('El mayor es el primer valor')
elif numero2 > numero1 and numero2 > numero3:
    print('El mayor es el segundo valor')
else:
    print('El mayor es el tercer valor')