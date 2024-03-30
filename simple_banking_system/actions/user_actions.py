

def repeat():
    print("Desea realizar otra operación?")
    print("1. Si")
    print("2. Salir")
    option = int(input("Ingrese una opción: "))

    if option == 1:
        print("\n")
    elif option == 2:
        print("Adiós, vuelva otro día")
        return None



def depositar(user_name, read_json, write_json, track):
    data = read_json(track)
    deposito = float(input("Ingrese el monto a depositar: "))

    for user in data:
        if user['user'] == user_name['user']:
            user['saldo'] += deposito
            break

    write_json(data, track)
    print("Todo correcto compa")


def retirar(user_name, read_json, write_json, track):
    data = read_json(track)
    retiro = float(input("Ingrese el monto a retirar: "))

    for user in data:
        if user['user'] == user_name['user']:
            if user['saldo'] >= retiro:
                user['saldo'] -= retiro
                break
            else:
                print("Saldo insuficiente")
                break

    write_json(data, track)


def transferir(user_name, read_json, write_json, track):
    data = read_json(track)
    usuario_encontrado = False
    user_to_transfer = input("Ingrese el usuario al que desea transferir: ")
    print("-" * 20)
    transfer = float(input("Ingrese el monto a transferir: "))
    print("-" * 20)

    # Primero deseo saber si el usuario al que se desea transferir existe
    for for_user_to_tranfer in data:
        # Si el usuario existe, entonces procedo a transferir
        if for_user_to_tranfer['user'] == user_to_transfer:
            for user in data:
                if user['user'] == user_name['user']:
                    if user['saldo'] >= transfer:
                        user['saldo'] -= transfer
                        for_user_to_tranfer['saldo'] += transfer
                        usuario_encontrado = True
                        break
                    else:
                        print("Saldo insuficiente")
                        return None
        
    if usuario_encontrado:
        write_json(data, track)
        print("Transferencia realizada con éxito")
    else:
        print("Usuario no encontrado")

