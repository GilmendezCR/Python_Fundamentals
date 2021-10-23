#Se ingresan tres notas de un alumno,
#si el promedio es mayor o igual a siete mostrar un mensaje "Promocionado".

nota1 = int(input('Ingrese la nota del estudiante:'))
nota2 = int(input('Ingrese la nota del estudiante:'))
nota3 = int(input('Ingrese la nota del estudiante:'))
Promedio = (nota1 + nota2 + nota3)/3

if Promedio >= 7:
    print('Promocionado')
else:
    print('Reprobado')