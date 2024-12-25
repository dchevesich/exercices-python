'''Definir una función superposicion() que tome dos listas y devuelva True si tienen al menos 1
miembro en común o devuelva False de lo contrario. Escribir la función usando el bucle for
anidado. '''


def superposicion(lista1, lista2):
    for num1 in lista2:
        for num2 in lista1:
            if num1 == num2:
                return True
    return False


lista1 = [1, 2, 3, 4, 5, 6]
lista2 = [7, 8, 9, 10, 11, 99]

superposicion(lista1, lista2)

resultado = superposicion(lista1, lista2)

print(resultado)
