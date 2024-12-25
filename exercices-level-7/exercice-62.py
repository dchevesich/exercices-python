'''Escribir un programa que almacene en una lista los siguientes 
precios, 50, 75, 46, 22, 80, 65, 8, y muestre por pantalla el menor y el mayor de los precios.'''


lista = [50, 75, 463456543, 22, 80, 100, 8]


mayor = 0
menor = 500

for num in lista:
    if num > mayor:
        mayor = num
    elif num < menor:
        menor = num

print(f"el mayor numero es {mayor} y el menor es {menor}")
