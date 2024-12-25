meses = ['abril', 'octubre', 'prokap', 'prokip', 'prokep']  # Lista de meses

while True:
    try:
        pedido = input("Ingresar fecha con formato dd/mm/aaaa: ")
        dia, mes, ano = pedido.split("/")  # Separar la fecha
        mes = int(mes)  # Convertir el mes a un número entero

        # Asegurarse de que el mes esté dentro del rango válido para tu lista
        if 1 <= mes <= len(meses):
            # Usar el índice del mes
            print(f"El {dia} de {meses[mes - 1]} de {ano} nací yo")
        else:
            print("El mes ingresado no es válido.")
    except ValueError:
        print("Favor de seguir las instrucciones y usar el formato dd/mm/aaaa.")
