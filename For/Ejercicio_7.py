#Confeccionar un programa que lea n pares de datos, cada par de datos corresponde a la medida de la base y la altura de un triángulo. El programa deberá informar:
#a) De cada triángulo la medida de su base, su altura y su superficie.
#b) La cantidad de triángulos cuya superficie es mayor a 12.

triangulosCantidad = int(input("Ingrese la cantidad de triangulos: "))
for i in range (triangulosCantidad):
    base = float(input("Ingrese la base del triangulo: "))
    altura = float(input("Ingrese la altura del triangulo: "))
    superficie = base * altura
    print("La superficie del triangulo es: ", superficie)
    if superficie > 12:
        print("La superficie del triangulo es mayor a 12")
    else:
        print("La superficie del triangulo es menor a 12")