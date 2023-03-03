def clean_player_data(players):
    clean_players = []
    for player in players:
        player["height"] = convert_height(player["height"])
        player["experience"] = convert_exp(player["experience"])
        player["guardians"] = convert_guardians(player["guardians"])
        clean_players.append(player)


def convert_height(string):
    new_string = string.replace(" inches", "")
    return int(new_string)


def convert_exp(string):
    if string == "YES":
        new_bool = True
    elif string == "NO":
        new_bool = False
    return new_bool


def convert_guardians(string):
    return string.split(' and ')
