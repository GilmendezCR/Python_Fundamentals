#Ingresar una oración que pueden tener letras tanto en mayúsculas como minúsculas.
#Contar la cantidad de vocales. 
#Crear un segundo string con toda la oración en minúsculas para que sea más fácil disponer la condición que verifica que es una vocal.
contadorVocales = 0
oracion = input("Ingrese una oración: ")
oracion.count("a")
oracion.count("e")
oracion.count("i")
oracion.count("o")
oracion.count("u")
oracion.count("A")
oracion.count("E")
oracion.count("I")
oracion.count("O")
oracion.count("U")
print("La cantidad de vocales es: ", oracion.count("a") + oracion.count("e") + oracion.count("i") + oracion.count("o") + oracion.count("u") + oracion.count("A") + oracion.count("E") + oracion.count("I") + oracion.count("O") + oracion.count("U"))
oracion2 = input("Ingrese una oración: ").lower()
print("La cantidad de vocales es: ", oracion2.count("a") + oracion2.count("e") + oracion2.count("i") + oracion2.count("o") + oracion2.count("u"))