'''Escribir un programa que pregunte al usuario los números ganadores de 
la lotería primitiva, los almacene en una lista y los muestre por pantalla ordenados de menor a mayor. '''


def menor_mayor(num):
    mayor = []
    for numeros in num:
        if numeros <= max(num):
            mayor.append(numeros)

    print("afasfsa ", mayor)


lista = []
while True:
    usuario = input(
        "Ingrese numeros a la bondola de loteria ingrese 'stop' para detener el ingreso: ")
    if usuario.lower() == 'stop':
        menor_mayor(lista)
        break
    try:
        numero = int(usuario)
        if numero < 0:
            print("Numero debe ser mayor a 0!")
        else:
            lista.append(numero)
    except ValueError:
        print("Debe ser un numero entero mayor a 0 !")
