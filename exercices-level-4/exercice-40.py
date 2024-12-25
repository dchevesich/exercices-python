'''Escribir un programa que pida al usuario una palabra y la muestre por pantalla 10 veces.'''


def mostrar_10veces(palabra):
    for _ in range(11):
        print(palabra)


usuario = input("Ingrese palabra para mostrarla 10 veces: ")
mostrar_10veces(usuario)
