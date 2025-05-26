def convertir_temperaturas(lista_celsius):
    lista_fahrenheit = []
    for c in lista_celsius:
        f = c * 9/5 + 32
        lista_fahrenheit.append(f)
    return lista_fahrenheit

# Ejemplo de uso
celsius = []
while True:
    entrada = input("Ingrese una temperatura en °C (o 'fin' para terminar): ")
    if entrada.lower() == 'fin':
        break
    if entrada.replace('.', '', 1).lstrip('-').isdigit():
        celsius.append(float(entrada))
    else:
        print("Por favor, ingrese solo números o 'fin'.")

fahrenheit = convertir_temperaturas(celsius)
print("Temperaturas en Fahrenheit:", fahrenheit)