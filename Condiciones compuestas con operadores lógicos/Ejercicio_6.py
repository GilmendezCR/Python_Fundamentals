#De un operario se conoce su sueldo y los años de antigüedad.
#Se pide confeccionar un programa que lea los datos de entrada e informe:
#a)Si el sueldo es inferior a 500 y su antigüedad es igual o superior a 10 años,
# otorgarle un aumento del 20 %, mostrar el sueldo a pagar.
#b)Si el sueldo es inferior a 500 pero su antigüedad es menor a 10 años,
# otorgarle un aumento de 5 %.
#c)Si el sueldo es mayor o igual a 500 mostrar el sueldo en pantalla sin cambios.


sueldo = float(input('Ingrese el sueldo del operario:'))
anios = int(input('Ingrese los anios de antiguedad del operario:'))


if sueldo < 500 and anios >= 10:
    montoAumentar = (sueldo * 20) / 100
    montoFinal = sueldo + montoAumentar
    print(f'El aumento del operario quedaria en:{montoFinal}')
elif sueldo < 500 and anios < 10:
    montoAumentar = (sueldo * 5) / 100
    montoFinal = sueldo + montoAumentar
    print(f'El aumento del operario quedaria en:{montoFinal}')
elif sueldo >= 500 :
    print('No posee cambios en su salario')
else:
    print('Error')

