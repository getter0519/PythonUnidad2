def calcular_promedio(lista):
    if len (lista) == 0:
        return None
    suma = sum(lista)
    for numero in lista:
        suma += numero
    return suma / len(lista)
numeros = []
while True:
    entrada = input("Ingrese un número (o 'salir' para terminar): ")
    if entrada.lower() == 'salir':
        break
    if entrada.isdigit() or (entrada.startswith('-') and entrada[1:].isdigit()):
        numeros.append(int(entrada))
    else:
        print("Entrada no válida. Por favor, ingrese un número entero o 'salir'.")
    
promedio = calcular_promedio(numeros)
if promedio is None:
    print("No se ingresaron números.")
else:
    print("Lista de números ingresados:", numeros)
    print("El promedio de los números es:", promedio)