'''Escribir un programa que almacene las asignaturas de un curso 
(por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista y la muestre por pantalla 
el mensaje Yo estudio <asignatura>, donde <asignatura> es cada una de las asignaturas de la lista. '''


lista = []

asd = print("Bienvenido a la prokap")

while asd != 'n':
    asd = input(
        "ingrese mateiras a agregar aprete 's' para agregar mas o 'n' para terminar el programa y r si desea leer la lista: ")
    if asd == 'n':
        break
    elif asd == 's':
        elementop = input("Ingrese curso a la lista:")
        lista.append(elementop)
        print(lista)
    elif asd == 'r':
        print(lista)
        for elemento in lista:
            print(
                f"soy Yo estudio {elemento} donde {elemento} es un elemento de la lista")
