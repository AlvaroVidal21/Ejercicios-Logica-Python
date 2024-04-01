# IMPORTS


def interface_iu_input(data: list) -> str:
    """
    Interface: obtener el tipo de moneda que queremos cambiar por otra divisa
    """
    print("Foreing exchange system")
    print("Choose an exchange: ")
    id_exchanges = {}
    for index, exchange in enumerate(data):
        index += 1
        print(f"{index}- {exchange}")
        id_exchanges[index] = exchange

    print("-" * (len("Choose an exchange: ") + 2))
    option = int(input("Choose an exchange: "))

    choose_exchange = id_exchanges[option]

    return choose_exchange


def interface_iu_output(input_exchange: str, data: list) -> str:
    """
    Interface: obtener el tipo de moneda que quremos cambiar por la moneda seleccionada
    """
    print("Foreing exchange system")
    print("\nChoose an exchange: ")
    print(f"Chosen exchange: {input_exchange}\n")
    print("-" * (len("Chosen exchange: {input_exchange}\n")))
    data_to_print = data.copy()
    data_to_print.pop(input_exchange)

    id_exchanges_output = {}

    for index, exchange in enumerate(data_to_print):
        index += 1
        print(f"{index}- {exchange}")
        id_exchanges_output[index] = exchange

    print("-" * (len("Choose an exchange: ") + 2))

    option = int(input("Choose an exchange:"))

    choose_exchange = id_exchanges_output[option]

    return choose_exchange


def interface_iu_size_exchange(input_exchange: str, output_exchange: str) -> float:
    """
    Interface: obtener la cantidad de dinero que queremos cambiar
    """
    print("Foreing exchange system")
    print("\nChoose an exchange: ")
    print(f"Chosen exchange: {input_exchange} to {output_exchange}\n")
    print(
        "-" * (len("Chosen exchange: {input_exchange} to {output_exchange}\n")))
    exchange_size = float(
        input("Enter the amount of money you want to exchange: "))

    return exchange_size


def interface_completed(input_exchange: str, output_exchange: str, exchange_size: float, exchange: float):
    """
    Interface: mostrar el resultado del intercambio
    """
    print("Foreing exchange system")
    print("\nChoose an exchange: ")
    print(f"Chosen exchange: {input_exchange} to {output_exchange}\n")
    print(f"Amount to exchange: {exchange_size}")
    print(f"Amount exchanged: {exchange}")
