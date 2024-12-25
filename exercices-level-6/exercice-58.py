'''Escribir un programa que almacene las asignaturas de un curso 
(por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista, 
pregunte al usuario la nota que ha sacado en cada asignatura y elimine de la lista
 las asignaturas aprobadas. Al final el programa debe mostrar por pantalla las asignaturas
  que el usuario tiene que repetir.'''

lista = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
notas = []
reprobadas = []

for elemento in lista:
    nota = int(input(f"Que nota has sacado en {elemento}?: "))
    notas.append(nota)


for i in range(len(lista)):
    print(f"en la asignatura: {lista[i]} tuve la nota {notas[i]}")


for notitas in notas:
    if notitas <= 3:
        reprobadas.append(notitas)

for listap, notasp in zip(lista, reprobadas):
    print(f"la materia {listap} obtuvo: {notasp} y reprobo")
