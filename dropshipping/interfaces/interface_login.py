

def interface_login_fn(clean_interface_fn):
    clean_interface_fn(1)
    print("Bienvenidos al registro de envíos de paquetes")
    print("Por favor, ingrese su usuario y contraseña")
    print("1. Iniciar sesión")
    print("2. Registrarse")
    print("3. Salir\n")

    while True:
        try:
            option = int(input("Ingrese una opción: "))
            return option

        except ValueError:
            clean_interface_fn(.5)
            print("⚠️ Ingrese un número válido\n")
            print("1. Iniciar sesión")
            print("2. Registrarse")
            print("3. Salir\n")
