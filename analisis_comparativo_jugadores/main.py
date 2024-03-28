import time
import os
import platform

from menu.interfaz import interfaz
from estadisticos.show_all_players import show_all_players


# Path::data
TRACK = "data/jugadores.json"

# Operative System
sistema_operativo = platform.system()
if sistema_operativo == "Linux":
    delete = "clear"
elif sistema_operativo == "Windows":
    delete = "cls"

def doing():
    option = interfaz()
    if option == 1:
        time.sleep(2)
        os.system(delete)
        show_all_players(TRACK)
    else:
        print("Option not available")
        time.sleep(2)
        os.system(delete)
        doing()




if __name__ == '__main__':
    doing()