'''Escribir un programa para una empresa que tiene salas de juegos para todas las edades y quiere calcular
 de forma automática el precio que debe cobrar a sus clientes por entrar. El programa debe preguntar al
  usuario la edad del cliente y mostrar el precio de la entrada. Si el cliente es menor de 4 años puede 
  entrar gratis, si tiene entre 4 y 18 años debe pagar 5€ y si es mayor de 18 años, 10€. '''


def salas_juegos():
    edad_cliente = int(input("Ingrese la edad del cliente: "))
    if edad_cliente <= 4:
        print("entra gratis")
    elif edad_cliente >= 18:
        print("El precio es de 10$")
    else:
        print("Paga 5 dolares")


salas_juegos()
