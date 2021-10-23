#Se ingresa por teclado un valor entero,
#mostrar una leyenda que indique si el número es positivo, 
#negativo o nulo (es decir cero)

numero = int(input('Ingrese el valor'))
if numero > 0:
    print('El valor es positivo')
elif numero < 0:
    print('El valor es negativo')
else:
    print('El valor es nulo')