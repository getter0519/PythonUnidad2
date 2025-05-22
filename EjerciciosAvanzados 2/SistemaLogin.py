def cargar_usuarios():
    usuarios ={}
    import os 
    if os.path.exists("usuarios.txt"):
        f = open ("usuarios.txt", "r")
        for linea in f:
            partes = linea.strip().split(",")
            if len(partes) == 2:
                usuarios, clave = partes
                usuarios[usuarios] = clave
        f.close()
    else:
        f = open ("usuarios.txt", "w")
        f.close()
    return usuarios
def login (usuarios):
    while True:
        print("\n=====Inicio de Sesión=====")
        usuario = input("Usuario: ").strip()
        clave = input("Contraseña: ").strip()
        if not usuarios or not clave:
            print("Error: ambos campos son obligatorios")
            continue
        if usuario in usuarios and usuarios[usuario] == clave:
            print (f"Bienvenido {usuario}!")
            return usuario
        else:
            print("Error: Usuario o contraseña incorrectos intente nuevamente")
            
def menu_principal(usuario):
    while True:
        print (f"\n-----Mneu Principal (Usuario: {usuario})-----")
        print("1. Ver Perfil")
        print("2. Cerrar Sesión")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            print (f"Perfil de {usuario}")
        elif opcion == "2":
            print("Cerrando sesión...")
            break
        else:
            print("Opción inválida, intente nuevamente")
def main():
    usuarios = cargar_usuarios()
    while True:
        usuario = login(usuarios)
        menu_principal(usuario)
if __name__ == "__main__":
    main()