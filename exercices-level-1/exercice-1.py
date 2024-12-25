'''Definir una función max() que tome como argumento dos números y devuelva el mayor de ellos.
Es cierto que python tiene una función max() incorporada, pero hacerla nosotros mismos es un
muy buen ejercicio'''


def numero_mayor(n1, n2):
    if n1 > n2:
        print(f"el numero mayor es:{n1} ")
        return n1
    else:
        print(f"el numero mayor es {n2}")
        return n2


a = int(input("Ingrese numero para evaluar cual es mayor: "))
b = int(input("Ingrese numero para evaluar cual es mayor: "))

numero_mayor(a, b)
