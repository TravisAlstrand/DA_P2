from constants import PLAYERS, TEAMS
import player_functions
import team_functions
import copy


def create_copy(list):
    new_list = copy.deepcopy(list)
    return new_list


if __name__ == "__main__":
    # MAKE COPIES OF IMPORTED LISTS
    new_players = create_copy(PLAYERS)
    new_teams = create_copy(TEAMS)
    # CLEAN PLAYERS DATA
    player_functions.clean_player_data(new_players)
    # BALANCE TEAMS
    balanced_teams = team_functions.balance_teams(new_teams, new_players)
    print(balanced_teams)
