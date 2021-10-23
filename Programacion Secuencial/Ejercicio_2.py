#Escribir un programa en el cual se ingresen cuatro números,
#calcular e informar la suma de los dos primeros
#y el producto del tercero y el cuarto.

lado1 = int(input('Favor ingrese el valor:'))
lado2 = int(input('Favor ingrese el valor:'))
lado3 = int(input('Favor ingrese el valor:'))
lado4 = int(input('Favor ingrese el valor:'))

suma = lado1 + lado2
producto = lado3 * lado4

print(f'La suma de los primeros dos valores es: {suma}')
print(f'El producto de los ultimos dos valores es: {producto}')