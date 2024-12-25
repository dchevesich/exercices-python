'''Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo 
como el de más abajo.

1
3 1
5 3 1
7 5 3 1
9 7 5 3 1'''

import random


def generar_numeros(num):
    numrandom = random.randint(0, 90)
    for i in range(1, num):
        print(i * )


while True:
    try:
        usuario = int(
            input("Ingrese numero a evaluar debe ser numero entero y mayor a 0: "))
        if usuario > 0:
            generar_numeros(usuario)
            break
        else:
            print("Numero mayor a 0 porfavor")
    except ValueError:
        print("Input no valido")
