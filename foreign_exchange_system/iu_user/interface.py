# IMPORTS
import os


def interface_iu(data: list, delete: str):
    print("Foreing exchange system")
    print("Choose an exchange: ")
    id_exchanges = {}
    for index, exchange in enumerate(data):
        index += 1
        print(f"{index}- {exchange}")
        id_exchanges[index] = exchange
    
    print("-" * len("Choose an exchange: "))
    option = int(input("Choose an exchange: "))

    choose_exchange = id_exchanges[option]

    return choose_exchange