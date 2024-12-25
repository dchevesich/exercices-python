'''Definir una función que calcule la longitud de una lista o una cadena dada. (Es cierto que python
tiene la función len() incorporada, pero escribirla por nosotros mismos resulta un muy buen
ejercicio.'''


def largo_cadena(cadena):
    contador = 0
    for _ in cadena:
        contador += 1
    
    print(f"la cadena contiene {contador-1} letras")

hola = input("ingresar cadena a evaluar longitud: ")
largo_cadena(hola)
