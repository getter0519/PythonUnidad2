computador = {
    'CPU' : 'Intel i7',
    'Tarjeta de Video': 'Nvidia RTX 3060',
    'RAM': '16GB ddr4',
    'Disco Duro': ' 1TB ssd',
    'Fuente de Poder': 'Corsair 650w',
    'Gabinete': 'Corsair Carbide',
    'Monitor': 'LG 27 pulgadas',
    'Perifericos': 'Teclado y Mouse Logitech',
    'Ventiladores': [ 'XYZ PULSAR A-RGB PWM',' Antec Fusion 120 ARGB PWM', 'Cooler Master SickleFlow 120 V2 ARGB PWM'],
    'Precio':  1000000,
    'Disponible': True,
    'Stock': 5,
}
#print(f"El computador es: {computador}")
#print(f"La CPU del computador es: {computador['CPU']}")
#for componentes in computador.values():
    #print(f"El computador tiene: {componentes}")
#for componentes in computador.keys():
    #print(f"El computador tiene: {componentes}")
#for clave, valor in computador.items():
    #print(f"{clave} - {valor}")

while True:
    opcion = input ("Desea comprar el computador? (S/N):\n"). upper()
    if opcion == 'S':
        computador['Stock'] -= 1
        print (f"El stock del computador es: {computador.get('Stock')}")
    elif opcion == 'N': 
        print("Gracias por visitar nuestra tienda")
        break
    else:
        print("Opción no válida")