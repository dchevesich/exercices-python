'''Escribir un programa que pregunte al usuario su nombre, edad, dirección y teléfono y
 lo guarde en un diccionario. Después debe mostrar por pantalla el mensaje <nombre> tiene <edad> años,
  vive en <dirección> y su número de teléfono es <teléfono>.'''

# Crear un diccionario vacío
datos_usuario = {}

# Usar un bucle para ingresar datos
while True:
    # Solicitar información al usuario
    datos_usuario['nombre'] = input(
        "Ingresa tu nombre (o 'salir' para terminar): ")

    # Opción para salir del bucle
    if datos_usuario['nombre'].lower() == 'salir':
        break

    datos_usuario['edad'] = input("Ingresa tu edad: ")
    datos_usuario['direccion'] = input("Ingresa tu dirección: ")
    datos_usuario['telefono'] = input("Ingresa tu número de teléfono: ")

    # Mostrar el mensaje con los datos ingresados
    print(f"{datos_usuario['nombre']} tiene {datos_usuario['edad']} años, vive en {datos_usuario['direccion']} y su número de teléfono es {datos_usuario['telefono']}.")

    # Limpiar el diccionario para nuevos datos
    datos_usuario.clear()
