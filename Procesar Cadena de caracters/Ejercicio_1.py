#Cargar una oración por teclado. Mostrar luego cuantos espacios en blanco se ingresaron. Tener en cuenta que un espacio en blanco es igual a
#" ", en cambio una cadena vacía es ""

oracion = input("Ingrese una oración: ")
oracion = oracion.count(" ")
print("La oración tiene", oracion, "espacios en blanco")
