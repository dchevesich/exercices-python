'''Escribir un programa que permita gestionar la base de datos de clientes de una empresa. 
Los clientes se guardarán en un diccionario en el que la clave de cada cliente será su NIF,
 y el valor será otro diccionario con los datos del cliente (nombre, dirección, teléfono, correo, preferente), 
 donde preferente tendrá el valor True si se trata de un cliente preferente. El programa debe preguntar al usuario
  por una opción del siguiente menú: (1) Añadir cliente, (2) Eliminar cliente, (3) Mostrar cliente,
   (4) Listar todos los clientes, (5) Listar clientes preferentes, (6) Terminar. 
   En función de la opción elegida el programa tendrá que hacer lo siguiente:

Preguntar los datos del cliente, crear un diccionario con los datos y añadirlo a la base de datos.
Preguntar por el NIF del cliente y eliminar sus datos de la base de datos.
Preguntar por el NIF del cliente y mostrar sus datos.
Mostrar lista de todos los clientes de la base datos con su NIF y nombre.
Mostrar la lista de clientes preferentes de la base de datos con su NIF y nombre.
Terminar el programa.'''

diccionaro_rut = {}

while True:
    diccionario_datos = {}
    rut = input("Ingrese rut: ")
    diccionario_datos["rut"] = rut
    nombrep = input("Ingrese nombre porfavor: ")
    direccion = input("Ingrese direccion porfavor: ")
    telefono = input("Ingrese telefono porfavor: ")
    correo = input("Ingrese correo porfavor: ")
    preferente = input("Ingrese si es prefrente porfavor: ")
    diccionario_datos["nombre"] = nombrep
    diccionario_datos['direccion'] = direccion
    diccionario_datos['telefono'] = telefono
    diccionario_datos['correo'] = correo
    diccionario_datos['preferente'] = preferente
    print(f"diccionario datos:{diccionario_datos} ")
    diccionaro_rut[rut] = diccionario_datos
    break

print(f"oka { diccionario_datos} {diccionaro_rut}")
