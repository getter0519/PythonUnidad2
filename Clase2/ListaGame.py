videojuegos = ["Mario", "Pacman", "Tetris"]

nuevo_juego = input("Ingrese el nombre del nuevo videojuego: ")
videojuegos.append(nuevo_juego)

for juego in videojuegos:
    print(juego)
