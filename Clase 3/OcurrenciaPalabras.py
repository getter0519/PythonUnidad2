def contar_ocurrencias(lista, palabra):
    contador = 0
    for item in lista:
        if item == palabra:
            contador += 1
    return contador

print("=== Contador de Ocurrencias de Palabras ===")
palabras = []
while True:
    entrada = input("Ingrese una palabra (o 'fin' para terminar): ")
    if entrada.lower() == 'fin':
        break
    palabras.append(entrada)

if not palabras:
    print("No se ingresaron palabras.")
else:
    print("\nPalabras ingresadas:")
    for i, palabra in enumerate(palabras, 1):
        print(f"{i}. {palabra}")

    buscar = input("\nIngrese la palabra a buscar: ")
    veces = contar_ocurrencias(palabras, buscar)
    if veces == 0:
        print(f"La palabra '{buscar}' no aparece en la lista.")
    elif veces == 1:
        print(f"La palabra '{buscar}' aparece 1 vez en la lista.")
    else:
        print(f"La palabra '{buscar}' aparece {veces} veces en la lista.")