#Realizar un programa que lea los lados de n triángulos, e informar:
#a)De cada uno de ellos, qué tipo de triángulo es:
#equilátero (tres lados iguales), isósceles (dos lados iguales), o escaleno (ningún lado igual)
#b)Cantidad de triángulos de cada tipo.

cantidadEquilateros = 0
cantidadIsosceles = 0
cantidadEscalenos = 0

triangulosCantidad = int(input("Ingrese la cantidad de triangulos: "))
for x in range(triangulosCantidad):
    lado1 = int(input("Ingrese el primer lado: "))
    lado2 = int(input("Ingrese el segundo lado: "))
    lado3 = int(input("Ingrese el tercer lado: "))
    if lado1 == lado2 and lado2 == lado3:
        cantidadEquilateros += 1
        print("El triangulo es equilatero")
    elif lado1 == lado2 or lado2 == lado3 or lado1 == lado3:
        cantidadIsosceles += 1
        print("El triangulo es isosceles")
    else:
        cantidadEscalenos += 1
        print("El triangulo es escaleno")

print("Cantidad de triangulos equilateros: ", cantidadEquilateros)
print("Cantidad de triangulos isosceles: ", cantidadIsosceles)
print("Cantidad de triangulos escalenos: ", cantidadEscalenos)

