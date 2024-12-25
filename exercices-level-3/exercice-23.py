'''Escribir un programa que pregunte el nombre del usuario en la consola y
 después de que el usuario lo introduzca muestre por 
 pantalla <NOMBRE> tiene <n> letras, donde <NOMBRE> es el nombre de usuario en mayúsculas y <n> es el número 
 de letras que tienen el nombre.'''


nombre = input("Cual es tu nombre?: ")
contador = len(nombre)
maximizar = nombre.capitalize()


print(f"{nombre} tiene {contador} letras donde {maximizar} ese el nombre de usuario en mayusculas.  ")
