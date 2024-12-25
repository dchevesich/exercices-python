'''Escribir un programa que pida al usuario un número entero y muestre por pantalla si es par o impar.'''


def espar_ono(num):
    return 'es par' if num % 2 == 0 else 'es inpar'


usuario = int(input("Ingrese numero a evaluar si es par o no: "))
resultado = espar_ono(usuario)
print(f"el resultado es: {resultado}")
