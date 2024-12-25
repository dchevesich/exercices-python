'''Escribir un programa que almacene el diccionario con los créditos de las asignaturas de
un curso {'Matemáticas': 6, 'Física': 4, 'Química': 5} y después muestre por
pantalla los créditos de cada asignatura en el formato <asignatura> tiene <créditos> créditos,
donde <asignatura> es cada una de las asignaturas del curso, y <créditos> son sus créditos.
Al final debe mostrar también el número total de créditos del curso.'''


hueas = [{'materia': 'Matematicas', 'Nota': 6},
         {'materia': 'Fisica', 'Nota': 4},
         {'materia': 'Quimica', 'Nota': 5},
         ]

for diccionario in hueas:
    print(f"{diccionario['materia']} tiene {diccionario['Nota']} donde {diccionario['materia']} es cada una de las asignaturas del curso y {diccionario['Nota']} son sus creditos")
