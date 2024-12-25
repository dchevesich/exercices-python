'''Escribir un programa que almacene las asignaturas de un curso
 (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista, 
 pregunte al usuario la nota que ha sacado en cada asignatura, y después las muestre por pantalla 
 con el mensaje En <asignatura> has sacado <nota> donde <asignatura> es cada una des las asignaturas
  de la lista y <nota> cada una de las correspondientes notas introducidas por el usuario.'''


lista = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
notas = []

for elemento in lista:
    nota = input(f"Que nota has sacado en {elemento}?: ")
    notas.append(nota)

        
for i in range(len(lista)):
    print(f"en la asignatura: {lista[i]} tuve la nota {notas[i]}")
