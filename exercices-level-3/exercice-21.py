'''Escribir un programa que pregunte el nombre del usuario en la consola y un número entero e 
imprima por pantalla en líneas distintas el nombre del usuario tantas veces como 
el número introducido.'''


def repetir_nombre():
    nombre = input("Cual es tu nombre? :")
    veces = int(input("Ingrese cuantas veces se va a repetir el nombre: "))
    for _ in range(veces):
        print(nombre)


repetir_nombre()
