# Realizar un programa que lea cuatro valores numéricos e informar su suma y promedio.

Valor1 = int(input("Favor ingrese el valor:"))
Valor2 = int(input("Favor ingrese el valor:"))
Valor3 = int(input("Favor ingrese el valor:"))
Valor4 = int(input("Favor ingrese el valor:"))

Suma = Valor1 + Valor2 + Valor3 + Valor4
Promedio = Suma // 4
print(f'La suma de los valores es: {Suma} y su promedio es:{Promedio}')