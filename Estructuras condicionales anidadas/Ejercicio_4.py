#Un postulante a un empleo, realiza un test de capacitación, se obtuvo la siguiente información: 
#cantidad total de preguntas que se le realizaron
#y la cantidad de preguntas que contestó correctamente.
#Se pide confeccionar un programa que ingrese los dos datos por teclado
# e informe el nivel del mismo según el porcentaje de respuestas correctas que ha obtenido,
# y sabiendo que:Nivel máximo:	Porcentaje>=90%.
	#Nivel medio:	Porcentaje>=75% y <90%.
	#Nivel regular:	Porcentaje>=50% y <75%.
	#Fuera de nivel:	Porcentaje<50%.

totalPreguntas = int(input('Ingrese el total de preguntas realizadas:'))
respuestasCorrectas = int(input('Ingrese la cantidad de respuestas contestas correctamente'))
porcentaje = (respuestasCorrectas * 100) // totalPreguntas

if porcentaje >= 90:
	print('Nivel maximo')
elif porcentaje >= 75 and porcentaje < 90:
	print('Nivel medio')
elif porcentaje >= 50 and porcentaje < 75:
	print('Nivel regular')
elif porcentaje < 50:
	print('Fuera de nivel')
else:
	print('Error')