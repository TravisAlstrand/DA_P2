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
            else:
                raise Exception("\nPlease enter a number in the selection")
        except ValueError:
            print("\nPlease enter a number in the selection")
            continue
        except Exception as e:
            print(e)
            continue


def display_team_stats(team, all_teams):
    print(team)
