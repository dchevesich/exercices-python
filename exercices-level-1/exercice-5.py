'''Escribir una funcion sum() y una función multip() que sumen y multipliquen respectivamente
todos los números de una lista. Por ejemplo: sum([1,2,3,4]) debería devolver 10 y multip([1,2,3,4])
debería devolver 24.'''

suma = [1, 2, 3, 4, 5]
multi = [1, 2, 3, 4, 5]


sumando = 0
for num in suma:
    sumando = sumando + num
    print(sumando)


multiplicando = 1
for num in multi:
    multiplicando = multiplicando * num
    print(multiplicando)
