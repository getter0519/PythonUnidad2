productos = []
precios = []
while True:
    nombre = input("ingrese el nombre del producto (o 'salir' para terminar): ")
    if nombre.lower() == 'salir':
        break
    precio = input("ingrese el precio del producto (solo números): ")
    while not precio.replace('.', '', 1).isdigit():
        print("Por favor, ingrese solo números para el precio.")
        precio = input("ingrese el precio del producto (solo números): ")
    productos.append(nombre)
    precios.append(precio)
print("\nLista de productos y precios:")
for i in range(len(productos)):
    print(f"{productos[i]}: ${precios[i]}")