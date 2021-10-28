#Definir una lista que almacene por asignación los nombres de 5 personas. 
#Contar cuantos de esos nombres tienen 5 o más caracteres.

contador = 0
lista = ['Ossus', 'Juan', 'Pedro', 'Juan', 'Enrique']
for x in range(len(lista)):
    if len(lista[x]) >= 5:
        contador += 1
print(contador)
