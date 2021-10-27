#Se realiza la carga de 10 valores enteros por teclado. Se desea conocer:
#a) La cantidad de valores ingresados negativos.
#b) La cantidad de valores ingresados positivos.
#c) La cantidad de múltiplos de 15.
#d) El valor acumulado de los números ingresados que son pares.

negativos = 0
multiplos = 0
positivos = 0
suma = 0

for x in range(10):
    num = int(input("Ingrese un numero: "))
    if num < 0:
        negativos += 1
    if num > 0:
        positivos += 1
    if num % 15 == 0:
        multiplos += 1
    if num % 2 == 0:
        suma += num

