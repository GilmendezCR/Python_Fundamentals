#Realizar un programa que solicite la carga por teclado de dos números,
#si el primero es mayor al segundo informar su suma y diferencia, 
#en caso contrario informar el producto y la división del primero respecto al segundo.

numero1 = int(input('Favor ingresar el valor:'))
numero2 = int(input('Favor ingresar el valor:'))

if numero1 > numero2 :
    suma = numero1 + numero2
    diferencia = numero1 - numero2
    print(f'La suma de los valores es {suma} y su diferencia es: {diferencia}')
else:
    producto = numero1 * numero2
    division = numero1 // numero2
    print(f'El producto de los valores es: {producto} y su division es {division}')
 