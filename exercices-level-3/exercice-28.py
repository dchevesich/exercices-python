'''Escribir un programa que pregunte por consola el precio de un
 producto en euros con dos decimales y muestre por pantalla el número de euros y 
el número de céntimos del precio introducido.'''

usuario = input("Ingrese un numero real con: ")

try:
    usuario = input("Ingrese un numero real con: ")
    oka, prokap = usuario.split(".")
    print(f"Euros: {oka}, Céntimos: {prokap}")
except ValueError:
    print("Error: El número debe contener un punto decimal.")
