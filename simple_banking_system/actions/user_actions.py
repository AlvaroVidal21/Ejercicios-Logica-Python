

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


