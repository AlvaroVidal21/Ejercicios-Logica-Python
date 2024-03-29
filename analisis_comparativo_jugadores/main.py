import time
import os
import platform

from menu.interfaz import interfaz
from estadisticos.show_all_players import show_all_players
from estadisticos.read_json import read_json_fn
from estadisticos.one_player import show_one_player
from estadisticos.two_playes import show_two_players
from estadisticos.statistics import fastest_player, most_assists, most_goals, most_passing_accuracy, most_defensive_involvements


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
            time.sleep(1)
            print("-" * 30)
            print("Player review")
            print("-" * 30)
            show_one_player(data)
        elif option == 3:
            time.sleep(1)
            print("-" * 30)
            print("Two players comparison")
            print("-" * 30)
            show_two_players(data) 
        elif option == 4:
            time.sleep(2)
            os.system(delete)
            print("-" * 30)
            print("Fastest player")
            print("-" * 30)
            fastest_player(data)
        elif option == 5:
            time.sleep(2)
            os.system(delete)
            print("-" * 30)
            print("Most assists")
            print("-" * 30)
            most_assists(data)
        elif option == 6:
            time.sleep(2)
            os.system(delete)
            print("-" * 30)
            print("Most goals")
            print("-" * 30)
            most_goals(data)
        elif option == 7:
            time.sleep(2)
            os.system(delete)
            print("-" * 30)
            print("Most passing accuracy")
            print("-" * 30)
            most_passing_accuracy(data)
        elif option == 8:
            time.sleep(2)
            os.system(delete)
            print("-" * 30)
            print("Most defensive involvements")
            print("-" * 30)
            most_defensive_involvements(data)
        else:
            print("Option not available")
            time.sleep(2)
            os.system(delete)
            doing()


if __name__ == '__main__':
    doing()
