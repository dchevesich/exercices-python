'''Escribir un programa que almacene la cadena de caracteres contraseña en una variable,
pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta.'''

caracteres_paswoord = input("Ingrese password ")

while True:

    print(f"Palabra secreta contiene {len(caracteres_paswoord)} letras")
    intento_usuario = input("Intente adivinar la password")
    if intento_usuario == caracteres_paswoord:
        print("adivinaste!")
        break
