#Desarrollar un programa que solicite la carga de 10 números
#e imprima la suma de los últimos 5 valores ingresados.
suma = 0
for x in range(10):
    numero = int(input("Ingrese un numero: "))
    if x >= 5:
        suma = suma + numero
print("La suma de los ultimos 5 numeros es: ", suma)

