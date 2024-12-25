'''Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, 
Física, Química, Historia y Lengua) en una lista y la muestre por pantalla. '''

lista = []

while True:
    print("Bienvenido a la agregadora de asignaturas automatica")
    usuario_asignatura = input("Agrega la asignatura que desees: ")
    lista.append(usuario_asignatura)
    cancelar = input("Escribe 'cancelar' cuando termines de asignar: ")
    if cancelar == 'cancelar':
        break
    else:
        print(f"la lista hasta el momento {lista}")
