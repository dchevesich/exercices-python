import random
import string


def adivinanzas_dankoche(resultado):
    guiones_bajos = ["-" for letra in resultado]
    letras_acertadas = []
    while True:
        intento_usuario = input(
            f"Ingrese letra a evaluar si esta en la palabra secreta: {guiones_bajos}")
        if intento_usuario not in resultado:
            print(
                f"Error la letra {intento_usuario} no se encuentra en la palabra secreta")
        elif intento_usuario in letras_acertadas:
            print(
                f"Letra ya ha sido acertada anteriormente intente con otra! {intento_usuario}")
        else:
            letras_acertadas.append(intento_usuario)
            for index, letra in enumerate(resultado):
                if letra in letras_acertadas:
                    guiones_bajos[index] = letra


posibles_caracteres = string.punctuation + string.digits + string.ascii_letters
resultado = "".join(random.choice(posibles_caracteres.lower())
                    for _ in range(2))

print(resultado)
adivinanzas_dankoche(resultado)
