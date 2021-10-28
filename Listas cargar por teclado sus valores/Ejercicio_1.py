#Cargar por teclado y almacenar en una lista las alturas de 5 personas (valores float)
#Obtener el promedio de las mismas. Contar cuántas personas son más altas que el promedio y cuántas más bajas.
contadorMayor = 0
contadorMenor = 0
promedio = 0
suma = 0
lista = []

for x in range(5):
    altura = float(input("Ingrese altura: "))
    lista.append(altura)
    suma += altura
    promedio = suma / 5
    if lista[x] > promedio:
        contadorMayor += 1
    else:
        contadorMenor += 1
        
print("El promedio de las alturas es: ", promedio)
print("La cantidad de personas más altas es: ", contadorMayor)
print("La cantidad de personas más bajas es: ", contadorMenor)