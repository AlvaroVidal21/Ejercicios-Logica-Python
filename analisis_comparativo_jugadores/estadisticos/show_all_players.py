import json
import os

def read_json(track):
    if not os.path.isfile(track):
        return "404 - File not found"
    else:
        with open(track, "r") as file:
            data  = json.load(file)
        return data


def show_all_players(track):
    data = read_json(track)

    for player in data:
        print(f"{player['jugador']} - Number : {player['jersey_number']}")
    

