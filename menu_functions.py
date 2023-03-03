import time


def menu_start(teams):
    print('''
    \n*** BASKETBALL STATS TOOL ***
    \nA) Display Teams
    \nB) Quit
    ''')
    while True:
        selection = input("\nSelect an option: ")
        try:
            if selection.lower() == "a":
                display_teams_list(teams)
                break
            elif selection.lower() == "b":
                print("\nThanks for stopping by!")
                quit()
            else:
                raise Exception("\nPlease enter an (A) or a (B)")
        except Exception as e:
            print(e)
            continue


def display_teams_list(teams):
    index_list = []
    print("\n*** SELECT A TEAM FOR STATS ***\n")

    for index, team in enumerate(teams):
        print(f"\n{index + 1}) {team['team_name']}")
        index_list.append(index + 1)
    print(f"\n{len(index_list) + 1}) Quit")

    while True:
        selection = input("\nSelect an option: ")
        try:
            selection_int = int(selection)
            if selection_int == len(index_list) + 1:
                print("\nThanks for stopping by!")
                quit()
            elif selection_int in index_list:
                display_team_stats(teams[selection_int - 1], teams)
                break
            else:
                raise Exception("\nPlease enter a number in the selection")
        except ValueError:
            print("\nPlease enter a number in the selection")
            continue
        except Exception as e:
            print(e)
            continue


def display_team_stats(team, all_teams):
    players_list = create_player_list(
        team["exp_players"], team["no_exp_players"])
    guardians_list = create_guardian_list(
        team["exp_players"], team["no_exp_players"])

    print(f"""
    \n______________________________________________________
    \n*** Team: {team['team_name']} ***
    \nTotal Players: {team['total_players']}
    \nExperienced Players: {len(team['exp_players'])}
    \nInexperienced Players: {len(team['no_exp_players'])}
    \nAverage Height: {team['avg_height']}
    \nPlayers: {', '.join(players_list)}
    \nGuardians: {', '.join(guardians_list)}
    \n______________________________________________________
    \nGoing back to team selection...
    """)
    time.sleep(5)
    display_teams_list(all_teams)


def create_player_list(list1, list2):
    total_list = list1 + list2
    list_of_strings = []
    # SORT BY HEIGHT
    sort_players(total_list)

    for player in total_list:
        name_string = f"{player['name']} - Height: {player['height']}in"
        list_of_strings.append(name_string)
    return list_of_strings


def sort_players(players):
    players.sort(reverse=True, key=get_height)


def get_height(player):
    return player["height"]


def create_guardian_list(list1, list2):
    total_list = list1 + list2
    guardian_list = []
    for player in total_list:
        if len(player["guardians"]) > 1:
            new_string = " & ".join(player["guardians"])
            guardian_list.append(new_string)
        else:
            new_string = "".join(player["guardians"])
            guardian_list.append(new_string)
    return guardian_list
