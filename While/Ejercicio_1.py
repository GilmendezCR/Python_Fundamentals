#Escribir un programa que solicite ingresar 10 notas de alumnos
#y nos informe cuántos tienen notas mayores o iguales a 7 y cuántos menores.
x= 0
contadorMayor= 0
contadorMenor = 0

while x < 10:
    nota = int(input('Ingrese la nota del {1-10}:'))
    if nota >= 7:
        contadorMayor += 1
    elif nota < 7:
        contadorMenor += 1
    x += 1
print(f'La cantidad de notas mayores o iguales a 7 son:{contadorMayor}')
print(f'La cantidad de notas menores a 7 son:{contadorMenor}')
    