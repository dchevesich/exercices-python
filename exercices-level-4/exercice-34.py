'''Escribir un programa que pida al usuario dos números y muestre por pantalla su división. 
Si el divisor es cero el programa debe mostrar un error. '''


def divisor(num, num2):
    while True:
        try:
            if num2 == 0:
                raise ZeroDivisionError("el divisor no puede ser 0")
            return num / num2
        except ZeroDivisionError:
            print("No se pude dividir por 0 ")
            num2 = int(input("Ingrese numero mayor a 0: "))


usuario = int(input("Ingrese numero a evaluar: "))
usuario2 = int(input("Ingrese segundo numero a evaluar: "))
resultado = divisor(usuario, usuario2)
print(f"el resultado de la division es {resultado}")
