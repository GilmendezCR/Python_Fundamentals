#Desarrollar una funcion que reciba un string como parametro
#y nos muestre la cantidad de vocales.
#Llamarla desde el bloque principal del programa 3 veces con string distintos.

def IngresarString(mensaje):
  acumulador = 0
  print(f'El mensaje ingresado es: {mensaje}')
  for x in range(len(mensaje)):
    if mensaje[x] == 'a' or mensaje[x] == 'e' or mensaje[x] == 'i' or mensaje[x] == 'o' or mensaje[x] =='u':
      acumulador += 1
  print(f'El mensaje ingresado tiene un total de vocales: {acumulador}')

#main
IngresarString('Hola me llamo Ossus')


 
    