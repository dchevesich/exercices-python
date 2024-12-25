'''Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el nombre. 
El grupo A esta formado por las mujeres con un nombre anterior a la M y los hombres con un nombre
 posterior a la N y el grupo B por el resto. Escribir un programa que pregunte al usuario su nombre y sexo,
  y muestre por pantalla el grupo que le corresponde.'''


def validar_sexo(sexo, nombre):
    primeraletra = nombre[0].upper()
    print(primeraletra)
    if sexo == "mujer" and ord(primeraletra) < ord("M"):
        return "Grupo A"
    elif sexo == "hombre" and ord(primeraletra) > ord("N"):
        return "GRUPO a"
    else:
        return "Grupo B"


pregunta_sexo = input(
    "Ingrese sexo. M para mujeres y H para hombres: ").lower()
pregunta_nombre = input("Ingrese nombre: ")
grupo = validar_sexo(pregunta_sexo, pregunta_nombre)
print(f"Pertenece al grupo {grupo}")
