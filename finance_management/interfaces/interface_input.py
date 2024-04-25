

def interface_input_fn(attemps = 2):

    if attemps == 0:
        print("Demasiados intentos fallidos.")
        exit()

    title = "Finance Management System"
    print("=" * len(title))
    print(title)
    print("=" * len(title))
    print("\nIngrese sus ingresos totales: ")

    try:
        income = float(input(">>>_ ").strip())
        return income
    except ValueError:
        print("Por favor, ingrese un número.")
        interface_input_fn(attemps - 1)



  
