#Ingresar por teclado los nombres de 5 personas y almacenarlos en una lista.
#Mostrar el nombre de persona menor en orden alfabético

nombres = []
mayor = ""
for x in range(5):
    nombres.append(input("Ingrese el nombre: "))
for y in range(4):
    if nombres[y] > mayor:
        mayor = nombres[y]
print("El nombre mayor es: ", mayor)

