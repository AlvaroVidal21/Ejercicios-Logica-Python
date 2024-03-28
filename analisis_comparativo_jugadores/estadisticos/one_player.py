import platform
import time
import os
from .show_players import show_player


# Operative System
sistema_operativo = platform.system()
if sistema_operativo == "Linux":
    delete = "clear"
elif sistema_operativo == "Windows":
    delete = "cls"


def show_one_player(data):
    choose_one = int(input("Choose the player: "))

    player_one = {}

    for player in data:
        if player['jersey_number'] == choose_one:
            player_one = player
    
    if player_one == {}:
        print("\nPlayer not found")
    else:
        print("-" * 30)
        time.sleep(1)
        os.system(delete)
        print("-" * 30)
        print("Player review")
        print("-" * 30)
        show_player(player_one)