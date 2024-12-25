'''Escribir un programa que pregunte el correo electrónico del usuario en la consola y 
muestre por pantalla otro correo electrónico con el mismo nombre 
(la parte delante de la arroba @) pero con dominio ceu.es.'''

pregunta = input("Cual es tu correo electronico?: ")
match pregunta:
    case pat1 if "@" in pat1:
        encontrando_arroba = pat1.find("@")
        nuevo_dominio = pat1[:encontrando_arroba]
        print(f"{nuevo_dominio}@ceu.es")
    case _:
        print("el nombre no contiene arroba")
