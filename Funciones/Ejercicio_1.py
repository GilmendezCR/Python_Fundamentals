#Desarrollar un programa que solicite la carga de tres valores y muestre el menor.
#Desde el bloque principal del programa llamar 2 veces a dicha función (sin utilizar una estructura repetitiva)

def ingresar_valor():
    valor1 = int(input("Ingrese un valor: "))
    valor2 = int(input("Ingrese un valor: "))
    valor3 = int(input("Ingrese un valor: "))
    if valor1 < valor2 and valor1 < valor3:
        print("El menor es: ", valor1)
    elif valor2 < valor1 and valor2 < valor3:
        print("El menor es: ", valor2)
    else:
        print("El menor es: ", valor3)
 
 #main
ingresar_valor()
ingresar_valor()
