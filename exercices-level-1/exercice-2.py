'''Definir una función max_de_tres(), que tome tres números como argumentos y devuelva el
mayor de ellos. '''


def numero_mayor(n1, n2, n3):
    if n1 >= n2 and n1 >= n3:
        print(f"El número mayor es: {n1}")
        return n1
    elif n2 >= n1 and n2 >= n3:
        print(f"El número mayor es: {n2}")
        return n2
    else:
        print(f"El número mayor es: {n3}")
        return n3


a = int(input("Ingrese un número para evaluar cuál es mayor: "))
b = int(input("Ingrese otro número para evaluar cuál es mayor: "))
c = int(input("Ingrese un tercer número para evaluar cuál es mayor: "))
numero_mayor(a, b, c)
