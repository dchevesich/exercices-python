'''Definir una función inversa() que calcule la inversión de una cadena. Por ejemplo la cadena
"estoy probando" debería devolver la cadena "odnaborp yotse"'''


def darvuelta_cadena(cadena):
    # cadena = cadena[::-1]
    # print(cadena)

    cadenainvertida = ""
    for char in cadena:
        cadenainvertida = char + cadenainvertida
        print(cadenainvertida)


a = input("Ingresar cadena a voltear: ")
darvuelta_cadena(a)
