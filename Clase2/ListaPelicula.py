peliculas = []
while True:
    nombre = input("Ingrese el nombre de la película (o 'salir' para terminar): ")
    if nombre.lower() == 'salir':
        break
    peliculas.append(nombre)
print("Lista de películas:")
print(peliculas)