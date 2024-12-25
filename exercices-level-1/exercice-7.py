'''Definir una función es_palindromo() que reconoce palíndromos (es decir, palabras que tienen el
mismo aspecto escritas invertidas), ejemplo: es_palindromo ("radar") tendría que devolver True.'''


def es_palindromo(cadena1, cadena2):
    # cadena = cadena[::-1]
    # print(cadena)

    cadenainvertida = ""
    for char in cadena2:
        cadenainvertida = char + cadenainvertida

    if cadena1 == cadenainvertida:
        print("es palindromo")
    else:
        print("no es palindromo")


a = input("Ingresar cadena a voltear: ")
b = input("Ingresar 2 palabra para evaluar si es palindromo: ")
es_palindromo(a, b)
