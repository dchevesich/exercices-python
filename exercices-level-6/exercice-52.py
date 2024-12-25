""""''Escribir un programa que muestre el eco de todo lo que el usuario introduzca
 hasta que el usuario escriba “salir” que terminará.'''"""

cancelar = input("Ingresa palabra a repetir: ")
while cancelar != "salir":
    print(cancelar)
    cancelar = input("Escribe 'salir' para terminar: ")
