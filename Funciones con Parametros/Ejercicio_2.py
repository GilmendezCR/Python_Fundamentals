#Confeccionar una función que reciba tres enteros
#y los muestre ordenados de menor a mayor.
#En otra función solicitar la carga de 3 enteros por teclado y proceder a llamar a la primer función definida.

def ingresoValores(num1,num2,num3):
    if num1 > num2:
        print(num2,num1)
    if num1 > num3:
        print(num3,num1)
    if num2 > num3:
        print(num3,num2)
    print("Los numeros ordenados de menor a mayor son: ",num1,num2,num3)

    #main
    ingresoValores(1,2,3)
