'''Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo 
como el de más abajo, de altura el número introducido.

*
**
***
****
***** '''


def cuadritos_locos(num):
    for _ in range(num):
        print(_ * "*")


while True:
    try:
        usuario_pregunta = int(input("Ingrese un numero entero:"))
        if usuario_pregunta > 0:
            cuadritos_locos(usuario_pregunta)
            break
        else:
            print("numero debe ser mayor")
    except ValueError:
        print("ENUmero amyor")
