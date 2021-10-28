#Solicitar el ingreso de una clave por teclado
#y almacenarla en una cadena de caracteres.
#Controlar que el string ingresado tenga entre 10 y 20 caracteres para que sea válido,
#en caso contrario mostrar un mensaje de error.\

ingresoContrasena = input("Ingrese una contraseña: ")
if ingresoContrasena.len() >= 10 and ingresoContrasena.len() <= 20:
    print("Contraseña válida")
else:
    print("Contraseña inválida")

