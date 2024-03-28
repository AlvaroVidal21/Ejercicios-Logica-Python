def show_player(player):
    print(f"Name: {player['jugador']}")
    print(f"Jersey Number: {player['jersey_number']}")
    print(f"Goals: {player["goals"]}")
    print(f"Assists: {player["assists"]}")
    print(f"Passing accuracy: {player["passing_accuracy"]}")
    print(f"Defensive involvments: {player["defensive_involvements"]}")
    print("-" * 30)



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
        print("\Player one and two not found")
    elif player_one == {}:
        print("\nPlayer one not found")
    elif player_two == {}:
        print("\nPlayer two not found")
    else:
        print("-" * 30)
        show_player(player_one)
        show_player(player_two)
