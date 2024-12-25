'''Escribir un programa que pida al usuario una palabra y muestre por pantalla
 el número de veces que contiene cada vocal.'''

usuario = input(
    "Ingrese palabra para evaluar cuantas veces se repite en las vocales: ")


vocales = ['a', 'e', 'i', 'o', 'u',]

contador = 0
for char in usuario:
    if char in vocales:
        contador += 1


print(f"hay un total de {contador} vocales en la palabra {usuario}")
