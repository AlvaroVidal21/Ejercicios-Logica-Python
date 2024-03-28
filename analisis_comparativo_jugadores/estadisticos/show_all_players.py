import json
import os


def show_all_players(data):
    print("-" * 30)
    print("| Player       |   Number    |")
    print("-" * 30)
    for player in data:
        distancia = len(f"| {player['jugador']} |  {player['jersey_number']}")
        print(f"| {player['jugador']} |  {player['jersey_number']}" + " " * (29-distancia) + "|")
        print("-" * 30)
