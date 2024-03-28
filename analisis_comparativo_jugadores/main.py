import time
import os
import platform

from menu.interfaz import interfaz
from estadisticos.show_all_players import show_all_players
from estadisticos.read_json import read_json_fn
from estadisticos.two_playes import show_two_players


# Path::data
TRACK = "data/jugadores.json"

# Operative System
sistema_operativo = platform.system()
if sistema_operativo == "Linux":
    delete = "clear"
elif sistema_operativo == "Windows":
    delete = "cls"


def doing():
    data = read_json_fn(TRACK)
    while True:
        option = interfaz()
        if option == 0:
            break

        elif option == 1:
            time.sleep(2)
            os.system(delete)
            show_all_players(data)

        elif option == 2:
            time.sleep(2)
            os.system(delete)
            show_two_players(data)  
        else:
            print("Option not available")
            time.sleep(2)
            os.system(delete)
            doing()


if __name__ == '__main__':
    doing()
