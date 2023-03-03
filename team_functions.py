import statistics


def balance_teams(teams, players):

    exp_players = []
    no_exp_players = []

    # MAKE TEAMS A LIST OF TEAM OBJECTS
    new_teams = create_new_teams(teams)

    # SPLIT PLAYERS BY EXP
    for player in players:
        if player["experience"] == True:
            exp_players.append(player)
        else:
            no_exp_players.append(player)

    # EVENLY SPREAD PLAYERS TO TEAMS
    disperse_players(new_teams, exp_players, True)
    disperse_players(new_teams, no_exp_players, False)

    # SORT PLAYERS BY HEIGHT
    sort_players(new_teams)

    # GET TOTAL PLAYER COUNTS
    get_total_players(new_teams)

    # GET AVG HEIGHTS
    get_avg_heights(new_teams)
    return new_teams


def create_new_teams(teams):
    new_teams = []
    for team in teams:
        new_team = {}
        new_team.update({"team_name": f"{team}", "total_players": 0, "exp_players": [
        ], "no_exp_players": [], "avg_height": 0})
        new_teams.append(new_team)
    return new_teams


def disperse_players(teams, player_list, exp_bool):
    while player_list:
        for team in teams:
            popped_player = player_list.pop(0)
            if exp_bool:
                team["exp_players"].append(popped_player)
            else:
                team["no_exp_players"].append(popped_player)


def sort_players(teams):
    for team in teams:
        team["exp_players"].sort(reverse=True, key=get_height)
        team["no_exp_players"].sort(reverse=True, key=get_height)


# RESOURCE - https://www.w3schools.com/python/ref_list_sort.asp
def get_height(player):
    return player["height"]


def get_total_players(teams):
    for team in teams:
        team["total_players"] = (
            len(team["exp_players"]) + len(team["no_exp_players"]))


def get_avg_heights(teams):
    for team in teams:
        height_list = []
        for player in team["exp_players"]:
            height_list.append(player["height"])
        for player in team["no_exp_players"]:
            height_list.append(player["height"])
        avg = statistics.mean(height_list)
        team["avg_height"] = round(avg, 1)
