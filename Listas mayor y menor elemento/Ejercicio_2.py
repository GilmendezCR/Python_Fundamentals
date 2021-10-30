#Cargar una lista con 5 elementos enteros.
#Imprimir el mayor y un mensaje si se repite dentro de la lista
#(es decir si dicho valor se encuentra en 2 o más posiciones en la lista)
mayor = 1
elementos = []
elementoRepetido = 1
for x in range(5):
    elementos.append(int(input("Ingrese un numero: ")))
    if elementos[x] > mayor:
        mayor = elementos[x]
    if elementos[x] == elementoRepetido:
        elementoRepetido = elementos[x]
print("El mayor elemento es: ", mayor)
print("El elemento se repite una cantidad de: ", elementoRepetido)

