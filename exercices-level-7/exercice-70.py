'''Escribir un programa que cree un diccionario de traducción español-inglés.
 El usuario introducirá las palabras en español e inglés separadas por dos puntos, y 
 cada par <palabra>:<traducción> separados por comas. El programa debe crear un diccionario con
  las palabras y sus traducciones. Después pedirá una frase en español y utilizará el diccionario
   para traducirla palabra a palabra. Si una palabra no está en el diccionario debe dejarla sin traducir.'''


espanish_ingles = {}


size = int(input("Ingrese el tama;o a evaluar: "))
for char in range(1, size+1):
    spanish = input("Ingrese palabra en espa;ol: ")
    inglish = input(f"como se dice {spanish} en ingles?: ")
    espanish_ingles[spanish] = inglish

pregunta_usuario = input("Ingrese palabra a evaluar si esta: ")
if pregunta_usuario in espanish_ingles:
    print(
        f"la traduccion de {pregunta_usuario} es: {espanish_ingles[pregunta_usuario]}")
else:
    print(f"palabra {pregunta_usuario} no se encuentra")
