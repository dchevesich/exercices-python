'''Escribir un programa que pida al usuario un número entero positivo
 y muestre por pantalla todos los números impares desde 1 hasta ese número separados por comas. '''


def mostrar_impares(num):
    for i in range(1, num):
        if i % 2 != 0:
            print(i)


while True:
    try:
        usuario = int(input("Ingrese un número mayor a 0: "))
        if usuario > 0:
            mostrar_impares(usuario)
            break  # Sale del bucle si el número es válido
        else:
            print("Por favor, ingrese un número mayor a 0.")
    except ValueError:
        print("Entrada no válida. Asegúrese de ingresar un número entero.")
