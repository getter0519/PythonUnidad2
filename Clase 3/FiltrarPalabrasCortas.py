def filtrar_palabras_cortas(lista):
    resultado = []
    for palabra in lista:
        if len(palabra) < 5:
            resultado.append(palabra)
    return resultado

palabras = []
while True:
    entrada = input("Ingrese una palabra (o 'fin' para terminar): ")
    if entrada.lower() == 'fin':
        break
    palabras.append(entrada)

cortas = filtrar_palabras_cortas(palabras)
print("Palabras cortas (menos de 5 caracteres):", cortas)

print("Palabras largas (5 o más caracteres):", [p for p in palabras if len(p) >= 5])