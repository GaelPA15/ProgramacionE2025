def saludar(nombre):
    
    saludo = f"¡Hola, {nombre}! Espero que tengas un gran día."
    return saludo


nombre_usuario = input("Por favor, ingresa tu nombre: ")
print(saludar(nombre_usuario))
