'''Escribir una función que tome un carácter y devuelva True si es una vocal, de lo contrario
devuelve False.'''


def contar_vocales(lista):
    while True:
        usuario_opcion = input("Ingrese letra a evaluar si es vocal o no ")
        if len(usuario_opcion) != 1:
            print("Ingresar solamente 1 letra porfavor")
            return False
        if usuario_opcion in lista:
            print(f"La letra {usuario_opcion} es una vocal!")
            return True
        else:
            print(f"letra {usuario_opcion} no es una vocal!")


lista_vocales = ["a", "e", "i", "o", "u"]
contar_vocales(lista_vocales)
