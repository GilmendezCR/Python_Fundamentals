#Realizar un programa que solicite la carga de valores enteros por teclado y los sume.
#Finalizar la carga al ingresar el valor -1. Dejar como comentario dentro del código fuente el enunciado del problema.

suma = 1
x = 0
while x != -1:
    x = int(input("Ingrese un numero: "))
    suma = suma + x
print("La suma de los numeros ingresados es: ", suma)


