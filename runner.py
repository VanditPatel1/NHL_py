from game_data import get_all_teams
from database_connect import create_table, player_add


if __name__ == '__main__':

    try:
        create_table()
    except:
        print ("Table already exists")

    get_all_teams()
