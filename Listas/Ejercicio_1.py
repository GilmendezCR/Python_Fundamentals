#Definir por asignación una lista con 8 elementos enteros.
#Contar cuantos de dichos valores almacenan un valor superior a 100.
contador = 0 
lista = [2,4,101,5,6,7,800,9]
for x in range(len(lista)):
    if lista[x] > 100:
        contador = contador + 1
print(contador)