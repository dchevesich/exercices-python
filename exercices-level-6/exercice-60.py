'''Escribir un programa que pida al usuario una palabra y muestre por pantalla si es un palíndromo.'''


usuario = input("ingrese palabra a verificar: ")
vueltiña = ""

for char in usuario[::-1]:
    vueltiña += char


print(usuario)
print(vueltiña)
