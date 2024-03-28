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
    print("-" * 30)
    print("| Player       |   Number    |")
    print("-" * 30)
    for player in data:
        distancia = len(f"| {player['jugador']} |  {player['jersey_number']}")
        print(f"| {player['jugador']} |  {player['jersey_number']}"+ " "*(29-distancia)+"|")
        print("-" * 30)
    

