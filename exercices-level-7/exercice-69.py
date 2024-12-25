'''Escribir un programa que cree un diccionario vacío y lo vaya llenado con 
información sobre una persona (por ejemplo nombre, edad, sexo, teléfono, correo electrónico, etc.)
 que se le pida al usuario. Cada vez que se añada un nuevo dato debe imprimirse el contenido del diccionario.'''

persona = {}
claves = ['Nombre', 'Edad', 'Sexo', 'Telefono', 'Correo']
while True:
    for clave in claves:
        usuario = input(f"complete los datos {clave}: ")
        persona[clave] = usuario

    print(persona)
    break
