import time
import os
from menu.interfaz import interfaz
from estadisticos.show_all_players import show_all_players


# Path::data
TRACK = "data/jugadores.json"


def doing():
    option = interfaz()
    if option == 1:
        time.sleep(2)
        os.system("clear")
        show_all_players(TRACK)
    else:
        print("Option not available")
        time.sleep(2)
        os.system("clear")
        doing()




if __name__ == '__main__':
    doing()