import random

def calcular_danio(tipo_arma, distancia):
    danio = 0
    if tipo_arma == 'pistola' and (0 <= distancia <= 50):
        danio = 10
    elif tipo_arma == 'pistola' and (51 <= distancia <= 100):
        danio = 5
    elif tipo_arma == "sniper":
        danio = 50
    elif tipo_arma == "escopeta" and (0 <= distancia <= 50):
        danio = 60
    elif tipo_arma == "escopeta" and (51 <= distancia <= 100):
        danio = 30
    return danio

def actulizar_salud(salud_actual, cantidad_danio):
    nueva_salud = salud_actual - cantidad_danio
    if nueva_salud < 0:
        nueva_salud = 0
    return nueva_salud

def puntos_ganados(tipo_enemigo):
    if tipo_enemigo == 'zombi':
        return 50
    elif tipo_enemigo == 'alien':
        return 100
    elif tipo_enemigo == 'robot':
        return 150
    else:
        return 0

def recargar_arma(arma_actual):
    max_balas = {'pistola': 10, 'escopeta': 6, 'sniper': 5}
    nombre_arma = arma_actual[0]
    arma_actual[1] = max_balas.get(nombre_arma, 5)
    print(f"Arma {nombre_arma} recargada. Balas disponibles: {arma_actual[1]}")
    return arma_actual

def cambiar_arma(arma_actual):
    print(" Elige  un arma: 1.pistola, 2.escopeta, 3.sniper")
    eleccion = input("opcion: ")
    if eleccion == '1':
        return ['pistola', 10, 0.8]
    elif eleccion == '2':
        return ['escopeta', 6, 0.6]
    elif eleccion == '3':
        return ['sniper', 5, 0.9]
    print("Arma no válida, manteniendo arma actual.")
    return arma_actual

def calcular_precision(precision, distancia):
    if distancia < 10:
        return precision
    elif 10 <= distancia < 30:
        return precision * 0.8
    else:
        return precision * 0.5

def elegir_enemigo():
    print("Elige el tipo de enemigo: 1. zombi  2. alien  3. robot")
    eleccion = input("Opción: ")
    if eleccion == '1':
        return 'zombi', 60
    elif eleccion == '2':
        return 'alien', 100
    elif eleccion == '3':
        return 'robot', 150
    else:
        print("Enemigo no válido, se usará zombi por defecto.")
        return 'zombi', 60

def elegir_arma_inicial():
    print("Elige tu arma inicial: 1.pistola, 2.escopeta, 3.sniper")
    eleccion = input("opcion: ")
    if eleccion == '1':
        return ['pistola', 10, 0.8]
    elif eleccion == '2':
        return ['escopeta', 6, 0.6]
    elif eleccion == '3':
        return ['sniper', 5, 0.9]
    else:
        print("Opción no válida, se usará pistola por defecto.")
        return ['pistola', 10, 0.8]

def principal():
    arma_actual_usuario = elegir_arma_inicial()
    vida_usuario = 100
    tipo_enemigo, vida_enemigo = elegir_enemigo()
    puntos = 0

    while True:
        print(f"\nTu vida: {vida_usuario} | Vida enemigo: {vida_enemigo}")
        print(f"Tu arma: {arma_actual_usuario[0]} | Balas: {arma_actual_usuario[1]}")
        print(f"Enemigo: {tipo_enemigo}")
        opcion = input("1. Disparar\n2. Recargar arma\n3. Cambiar arma\n4. Cambiar enemigo\n5. Salir\n:")
        if opcion == '1':
            if arma_actual_usuario[1] > 0:
                distancia = random.randint(5, 100)
                prob = calcular_precision(arma_actual_usuario[2], distancia)
                if random.random() < prob:
                    danio = calcular_danio(arma_actual_usuario[0], distancia)
                    vida_enemigo = actulizar_salud(vida_enemigo, danio)
                    print(f"¡Disparo certero! Daño al enemigo: {danio}")
                else:
                    print("¡Fallaste el disparo!")
                arma_actual_usuario[1] -= 1
            else:
                print("No tienes balas, recarga el arma.")

            if vida_enemigo <= 0:
                print(f"¡Enemigo eliminado! Ganaste {puntos_ganados(tipo_enemigo)} puntos.")
                puntos += puntos_ganados(tipo_enemigo)
                tipo_enemigo, vida_enemigo = elegir_enemigo()
        elif opcion == '2':
            arma_actual_usuario = recargar_arma(arma_actual_usuario)
        elif opcion == '3':
            arma_actual_usuario = cambiar_arma(arma_actual_usuario)
        elif opcion == '4':
            tipo_enemigo, vida_enemigo = elegir_enemigo()
        elif opcion == '5':
            print(f"¡Gracias por jugar! Puntos totales: {puntos}")
            break
        else:
            print("Opción inválida.")

principal()