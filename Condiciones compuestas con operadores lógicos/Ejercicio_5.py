#Escribir un programa que pida ingresar la coordenada de un punto en el plano,
# es decir dos valores enteros x e y (distintos a cero).
#Posteriormente imprimir en pantalla en que cuadrante se ubica dicho punto. 
#(1º Cuadrante si x > 0 Y y > 0 , 2º Cuadrante: x < 0 Y y > 0, etc.)

x = int(input('Favor ingresar la primer coordenada:'))
y = int(input('Favor ingresar la segunda coordenada:'))

if x > 0 and y > 0:
    print('Se encuentra en el primer cuadrante')
elif x < 0 and y > 0:
    print('Se encuentra en el segundo cuadrante')
