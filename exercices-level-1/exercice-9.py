'''Definir una función generar_n_caracteres() que tome un entero n y devuelva el caracter
multiplicado por n. Por ejemplo: generar_n_caracteres(5, "x") debería devolver "xxxxx".'''


def generar_n_caracteres(n1, caracter):
    return caracter * n1


n1 = int(input("ingresar la cantidad de veces que quiere que aparezca la letra : "))
caracter = input(
    "ingresar una letra: ")

print(generar_n_caracteres(n1, caracter))
