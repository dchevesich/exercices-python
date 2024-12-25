'''La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes.
 Los ingredientes para cada tipo de pizza aparecen a continuación.

Ingredientes vegetarianos: Pimiento y tofu.
Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.

Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, 
y en función de su respuesta le muestre un menú con los ingredientes disponibles para que elija.
 Solo se puede eligir un ingrediente además de la mozzarella y el tomate que están en todas la pizzas.
  Al final se debe mostrar por pantalla si la pizza elegida es vegetariana o no y todos los ingredientes que lleva.'''


def pizzeriap(lista1, lista2):
    siemprevan = ["Mozarella", "Tomate"]
    usuario_opocion = input(
        "Bienvenido a la pizzeria tenemos 2 tipos de pizza vegie y no porfavor elegir V para VEGGIE y N para no: "
    )
    usuario_opocion = usuario_opocion.capitalize()
    if usuario_opocion == "V":
        print(
            f"estas son las opciones para vegana ten en cuenta que todas las pizzas de por si traen mozarella y tomate.\n{lista1}")
        respuesta_usuario = ""
        while respuesta_usuario not in lista1:
            respuesta_usuario = input("Elegir un ingrediente: ")
            if respuesta_usuario not in lista1:
                print("Ingrediente no se encuentra en la lista de ingredientes validos.")
            else:
                ingredientes_elegidos = siemprevan + [respuesta_usuario]
                print(
                    f"La pizza elegida es: Vegetariana y los ingredientes son los siguientes{ingredientes_elegidos}")
                break
    if usuario_opocion == "N":
        print(
            f"estas son las opciones para vegana ten en cuenta que todas las pizzas de por si traen mozarella y tomate.\n{lista2}")
        respuesta_usuario = ""
        while respuesta_usuario not in lista2:
            respuesta_usuario = input("Elegir un ingrediente: ")
            if respuesta_usuario not in lista2:
                print("Ingrediente no se encuentra en la lista de ingredientes validos.")
            else:
                ingredientes_elegidos = siemprevan + [respuesta_usuario]
                print(
                    f"La pizza elegida es: No veggie y los ingredientes son los siguientes{ingredientes_elegidos}")


vegetarianos = ["Pimiento", "Tofu"]
novegis = ["Peperoni", "Jámon", "Salmon"]
pizzeriap(vegetarianos, novegis)
