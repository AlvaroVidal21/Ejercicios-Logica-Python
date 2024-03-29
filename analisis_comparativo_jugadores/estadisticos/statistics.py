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


def most_goals(data):
    most_goals_list = []
    most_goals_players = []

    for player in data:
        most_goals_list.append(player['goals'])

    most_goals = max(most_goals_list)

    for player in data:
        if player['goals'] == most_goals:
            most_goals_players.append(player)
    
    for p in most_goals_players:
        show_player(p)


def most_passing_accuracy(data):
    most_passing_accuracy_list = []
    most_passing_accuracy_players = []

    for player in data:
        most_passing_accuracy_list.append(player['passing_accuracy'])

    most_passing_accuracy = max(most_passing_accuracy_list)

    for player in data:
        if player['passing_accuracy'] == most_passing_accuracy:
            most_passing_accuracy_players.append(player)
    
    for p in most_passing_accuracy_players:
        show_player(p)


def most_defensive_involvements(data):
    most_defensive_involvements_list = []
    most_defensive_involvements_players = []

    for player in data:
        most_defensive_involvements_list.append(player['defensive_involvements'])

    most_defensive_involvements = max(most_defensive_involvements_list)

    for player in data:
        if player['defensive_involvements'] == most_defensive_involvements:
            most_defensive_involvements_players.append(player)
    
    for p in most_defensive_involvements_players:
        show_player(p)

        