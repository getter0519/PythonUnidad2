def sumar_pares(lista):
    suma = 0
    for numero in lista:
        if numero % 2 == 0:
            suma += numero
    return suma

numeros = []
while True:
    entrada = input("Ingrese un número (o 'salir' para terminar): ")
    if entrada.lower() == 'salir':
        break
    if entrada.isdigit() or (entrada.startswith('-') and entrada[1:].isdigit()):
        num = int(entrada)
        if num % 2 == 0:
            print(f"{num} es par.")
        else:
            print(f"{num} es impar.")
        numeros.append(num)
    else:
        print("Entrada no válida. Por favor, ingrese un número entero o 'salir'.")

print("Lista de números ingresados:", numeros)
print("La suma de los números pares es:", sumar_pares(numeros))