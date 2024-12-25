'''Para tributar un determinado impuesto se debe ser mayor de 16 años y tener unos ingresos 
iguales o superiores a 1000 € mensuales. Escribir un programa que pregunte al usuario su edad y sus 
ingresos mensuales y muestre por pantalla si el usuario tiene que tributar o no. '''


def tiene_quepagar(plata, edad):
    if plata >= 1000 and edad > 16:
        print("tiene que tributar!")
    else:
        print("no debe tributar")


plata = int(input("Ingrese su ingresos mensuales: "))
edad = int(input("Ingrese su edad: "))
tiene_quepagar(plata, edad)
