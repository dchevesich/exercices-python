'''Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla
 la cuenta atrás desde ese número hasta cero separados por comas.'''


def cuenta_atras(num):
    for _ in range(num, -1, -1):
        print(_)


while True:
    try:
        usuario = int(input("Ingrese numero entero positivo: "))
        if usuario > 0:
            cuenta_atras(usuario)
            break
        else:
            print("nmero mayort a 0 ")
    except ValueError:
        print("solamente numeros.")
