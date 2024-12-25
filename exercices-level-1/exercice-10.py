'''Definir un histograma procedimiento() que tome una lista de números enteros e imprima un
histograma en la pantalla. Ejemplo: procedimiento([4, 9, 7]) debería imprimir lo siguiente:
****
*********
******* '''


def matriz(lista):
    for num in lista:
        print("*" * num)


lista = [1, 2, 7]
matriz(lista)
