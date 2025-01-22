#en este ejercicio vamos a validad un usuario y contraseña de un usuario 

#se pide al usuario que ingrese su usuario
usuario = input("Ingresar usuario:")

#se pide al usuario que ingrese su contraseña
contraseña = input("Ingresar contraseña:")


#se valida si el usuario es igual a "admin" y la contraseña es igual a "admin123"
if usuario == "GaelPA15" and contraseña == "admin123":
    print("Bienvenido al sistema")