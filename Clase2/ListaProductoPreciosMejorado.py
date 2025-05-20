productos = []
precios = []

while True:
    print("\nMenú:")
    print("1. Agregar producto")
    print("2. Eliminar producto")
    print("3. Mostrar productos y precios")
    print("4. Salir")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        nombre = input("Ingrese el nombre del producto: ")
        precio = input("Ingrese el precio del producto: ")
        while not precio.replace('.', '', 1).isdigit():
            print("Por favor, ingrese solo números para el precio.")
            precio = input("Ingrese el precio del producto: ")
        productos.append(nombre)
        precios.append(precio)

    elif opcion == "2":
        if not productos:
            print("No hay productos para eliminar.")
            continue
        print("Productos actuales:")
        for prod in productos:
            print(f"- {prod}")
        nombre = input("Ingrese el nombre del producto a eliminar: ")
        if nombre in productos:
            # Buscar la posición manualmente y eliminar ambos SIN enumerate
            i = 0
            while i < len(productos):
                if productos[i] == nombre:
                    productos.remove(nombre)
                    precios.pop(i)
                    print("Producto eliminado.")
                    break
                i += 1
        else:
            print("Producto no encontrado.")

    elif opcion == "3":
        print("\nLista de productos y precios:")
        for i in range(len(productos)):
            print(f"{productos[i]}: ${precios[i]}")

    elif opcion == "4":
        break
    else:
        print("Opción inválida.")