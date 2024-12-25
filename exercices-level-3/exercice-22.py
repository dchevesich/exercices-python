'''Escribir un programa que pregunte el nombre completo del usuario en la consola
y después muestre por pantalla el nombre completo del usuario tres veces, una con todas las letras minúsculas,
otra con todas las letras mayúsculas y otra solo con la primera letra del nombre y de los apellidos en mayúscula.
 El usuario puede introducir su nombre combinando mayúsculas y minúsculas como quiera. '''


def manipular_strings(string):
    return string.lower()


def maximizar(resultado):
    return resultado.upper()


def pedimiento_raro(resultado):
    return resultado.title()


resultado = manipular_strings("Danko Chevesich")
print(resultado)

resultado_mayus = maximizar(resultado)
print(resultado_mayus)

resultado_raro = pedimiento_raro(resultado)
print(resultado_raro)
