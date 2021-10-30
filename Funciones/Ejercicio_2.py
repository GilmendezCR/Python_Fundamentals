#Desarrollar un programa con dos funciones.
#La primer solicite el ingreso de un entero y muestre el cuadrado de dicho valor.
#La segunda que solicite la carga de dos valores y muestre el producto de los mismos.
#LLamar desde el bloque del programa principal a ambas funciones.
cuadrado = 0
def ingreso_valor():
    numero = int(input("Ingrese un numero: "))
    cuadrado = numero * numero
    print("El cuadrado de ", numero, " es: ", cuadrado)
def ingreso_valor_multiple():
    numero1 = int(input("Ingrese un numero: "))
    numero2 = int(input("Ingrese un numero: "))
    producto = numero1 * numero2
    print("El producto de ", numero1, " y ", numero2, " es: ", producto)

#main
ingreso_valor()
ingreso_valor_multiple()