#Se ingresan un conjunto de n alturas de personas por teclado.
#Mostrar la altura promedio de las personas.

n = 0
sumatoria = 0
alturaCantidad = int(input('Ingrese el conjunto de alturas:'))
while n < alturaCantidad:
    altura = int(input('Ingrese la altura de la persona:'))
    sumatoria = sumatoria + altura
    n +=1
promedio = sumatoria  / alturaCantidad
print(f'La altura promedio de los empleados es:{promedio}')