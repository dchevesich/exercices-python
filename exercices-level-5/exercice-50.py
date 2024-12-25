'''Escribir un programa que pida al usuario una palabra y luego muestre por pantalla una a una 
las letras de la palabra introducida empezando por la última.
        '''

usuario = input("Ingrese palabra")

for char in usuario[::-1]:
    print(char)
