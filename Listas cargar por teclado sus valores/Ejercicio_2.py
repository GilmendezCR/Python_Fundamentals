#Una empresa tiene dos turnos (mañana y tarde) en los que trabajan 8 empleados (4 por la mañana y 4 por la tarde)   
# Confeccionar un programa que permita almacenar los sueldos de los empleados agrupados en dos listas.
#Imprimir las dos listas de sueldos.
#Imprimir la union de ambas listas

lista_mañana = []
lista_tarde = []
for x in range(4):
    lista_mañana.append(int(input("Ingrese el sueldo del empleado: ")))
for y in range(4):
    lista_tarde.append(int(input("Ingrese el sueldo del empleado: ")))
print("Sueldos de la mañana: ", lista_mañana)
print("Sueldos de la tarde: ", lista_tarde)
lista_mañana.extend(lista_tarde)
print("Sueldos de la mañana y tarde: ", lista_mañana)
lista_mañana[3]=5
print("Lista modificada:",lista_mañana)



