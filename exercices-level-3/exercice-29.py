'''Escribir un programa que pregunte al usuario la fecha de su 
nacimiento en formato dd/mm/aaaa y muestra por pantalla, el día, el mes y el año.
 Adaptar el programa anterior para que también funcione cuando
 el día o el mes se introduzcan con un solo carácter.'''


while True:
    try:
        pregunta_usuario = input(
            "Cual es tu fecha de nacimiento? usar formato dd/mm/aaaa: ")
        dia, mes, ano = pregunta_usuario.split("/")
        print(f"el {dia} del mes {mes} del ano {ano} naci yo")
        break
    except ValueError:
        print("Se debe seguir el formato solicitado: dd/mm/aaaa ")
