#Almacenar en una lista los sueldos (valores float) de 5 operarios. Imprimir la lista y el promedio de sueldos.
lista = []
suma = 0
for x in range(5):
    sueldo = float(input("Ingrese el sueldo del operario: "))
    lista.append(sueldo)
    suma = suma + sueldo
promedio = suma / 5
print("Los sueldos ingresados son: ", lista)
print("El promedio de sueldos es: ", promedio)

