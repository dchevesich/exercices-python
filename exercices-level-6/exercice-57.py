'''Escribir un programa que almacene en una lista los números del 1 al 10 y los muestre 
por pantalla en orden inverso separados por comas.'''


print("Bienvenido a la maquina que ingresa numeros del 1 al 10!!!!")

lista = []

for _ in range(1, 11):
    lista.append(_)


sublista = lista[::-1]

print(sublista)
