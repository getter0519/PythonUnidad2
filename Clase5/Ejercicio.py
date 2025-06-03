import getpass

clientes = {
    "Juan": "1234"
}

while True:
    print("1) Iniciar sesión\n2) Registrarse")
    opcion = input("Seleccione una opción: ")
    if opcion == '1':
        nombre = input("Ingrese su nombre de usuario: ")
        contrasenia = getpass.getpass("Ingrese su contraseña: ")  # Corregido aquí
        if nombre in clientes.keys():
            if contrasenia == clientes.get(nombre):
                print(f"Sesion Iniciada {nombre}")
            else:
                print("Contraseña incorrecta")
        else:
            print("Usuario no encontrado, por favor regístre0se primero.")
    elif opcion == '2':
        nombre = input ("Ingrese su nombre de usuario: ")
        if nombre in clientes.keys():
            print("El usuario ya existe, por favor elija otro nombre.")
        else:
            contrasenia = getpass.getpass("Ingrese su contraseña: ")
            clientes[nombre] = contrasenia
            print ("Usuario registrado exitosamente.")
            print(clientes)

