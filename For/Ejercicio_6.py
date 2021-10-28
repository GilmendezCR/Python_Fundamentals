#Escribir un programa que pida ingresar coordenadas (x,y) que representan puntos en el plano.
#Informar cuántos puntos se han ingresado en el primer, segundo, tercer y cuarto cuadrante.
# Al comenzar el programa se pide que se ingrese la cantidad de puntos a procesar.
primerContador = 0
segundoContador = 0
tercerContador = 0
cuartoContador = 0
puntosProcesar = int(input("Ingrese la cantidad de puntos a procesar: "))
for i in range(puntosProcesar):
    x = int(input("Ingrese la coordenada x: "))
    y = int(input("Ingrese la coordenada y: "))
    if x > 0 and y > 0:
        primerContador += 1
    elif x < 0 and y > 0:
        segundoContador += 1
    elif x < 0 and y < 0:
        tercerContador += 1
    elif x > 0 and y < 0:
        cuartoContador += 1     
print("La cantidad de puntos en el primer cuadrante es: ", primerContador)
print("La cantidad de puntos en el segundo cuadrante es: ", segundoContador)
print("La cantidad de puntos en el tercer cuadrante es: ", tercerContador)
print("La cantidad de puntos en el cuarto cuadrante es: ", cuartoContador)