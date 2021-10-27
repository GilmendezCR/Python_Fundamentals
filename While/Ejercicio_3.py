#En una empresa trabajan n empleados cuyos sueldos oscilan entre $100 y $500,
#realizar un programa que lea los sueldos que cobra cada empleado
#e informe cuántos empleados cobran entre $100 y $300 
#y cuántos cobran más de $300.


n = 0
sueldoMenor = 0
sueldoMayor = 0
empleadosCantidad = int(input('Ingrese la cantidad de empleados:'))
while n < empleadosCantidad:
    sueldo = int(input('Ingrese el sueldo del empleado:'))
    if sueldo >= 100 and sueldo <= 300:
        sueldoMenor += 1
    elif sueldo > 300:
        sueldoMayor += 1
    n += 1
print('Cantidad de empleados que cobran entre $100 y $300:', sueldoMenor)
print('Cantidad de empleados que cobran más de $300:', sueldoMayor)







