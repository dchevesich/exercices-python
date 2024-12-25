'''Escribir un programa que pida al usuario que introduzca una frase en la consola y una vocal,
 y después muestre por pantalla
 la misma frase pero con la vocal introducida en mayúscula'''

vocales = ["a", "e", "i", "o", "u"]
frase_usuario = input("Ingrese frase: ")
nuevafrase = ""
for char in frase_usuario:
    if char in vocales:
        nuevafrase += char.capitalize()
    else:
        nuevafrase += char


print(nuevafrase)
