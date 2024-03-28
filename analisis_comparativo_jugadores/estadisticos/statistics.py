from .show_players import show_player


def fastest_player(data):
    most_speed_list = []
    most_speed_players = []

    for player in data:
        most_speed_list.append(player["speed"])

    most_speed = max(most_speed_list)

    for player in data:
        if player["speed"] == most_speed:
            most_speed_players.append(player)

    
    for p in most_speed_players:
        show_player(p)


def most_assists(data):
    most_assists_list = []
    most_assists_players = []

    for player in data:
        most_assists_list.append(player['assists'])

    mosts_assists = max(most_assists_list)

    for player in data:
        if player['assists'] == mosts_assists:
            most_assists_players.append(player)
    
    for p in most_assists_players:
        show_player(p)

