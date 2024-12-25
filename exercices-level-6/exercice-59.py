'''Escribir un programa que almacene el abecedario en una lista, elimine de la lista 
las letras que ocupen posiciones múltiplos de 3, y muestre por pantalla la lista resultante.'''


import string


oka = string.ascii_lowercase

lista = []

lista.append(oka)

for char in lista[-1, 1, -3]:
    lista.remove(char)


print(f"nuieva lista {lista}")
