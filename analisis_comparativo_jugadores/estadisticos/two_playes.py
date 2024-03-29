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



def show_two_players(data):
    choose_one  = int(input("Choose the first player: "))
    choose_two = int(input("Choose the second player: "))

    player_one = {}
    player_two = {}

    for player in data:
        if player['jersey_number'] == choose_one:
            player_one = player
        if player['jersey_number'] == choose_two:
            player_two = player

    if player_one == {} and player_two == {}:
        print("\nPlayer one and two not found")
    elif player_one == {}:
        print("\nPlayer one not found")
    elif player_two == {}:
        print("\nPlayer two not found")
    else:
        print("-" * 30)
        time.sleep(1)
        os.system(delete)
        print("-" * 30)
        print("Two players comparison")
        print("-" * 30)
        show_player(player_one)
        show_player(player_two)
