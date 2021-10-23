#Calcular el sueldo mensual de un operario
#conociendo la cantidad de horas trabajadas
#y el valor por hora.

hrtrabajadas = int(input('Favor ingresar las horas trabajadas del operario:'))
vlrhora = int(input('Favor ingresar el valor por hora del operario:'))

sueldo = hrtrabajadas * vlrhora
print('El sueldo del empleado es:' + str(sueldo))
