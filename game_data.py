import requests
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import json


NHL_URL = "https://statsapi.web.nhl.com/api/v1/"
GAME = "game/"
LIVE = "feed/live/"


def get_all_teams():
    URL = 'https://statsapi.web.nhl.com/api/v1/teams'
    res = requests.get(URL)

    try:
        data = res.json()
        teams = data['teams']
    except Exception as ex:
        print ("Could not get teams")
        raise

    team_links = list()
    for team in teams:
        team_links.append(team['link'])

    print (team_links)

def get_game(game_id):
    game_id = str(game_id) + '/'
    print (NHL_URL+GAME+game_id+LIVE)

    response = requests.get(NHL_URL+GAME+game_id+LIVE)
    data = response.json()
    plays = data['liveData']['plays']['allPlays']
    shots = list()

    for play in plays:
        try:
            if play["result"]["event"] == "Shot" and play["team"]["id"] == 4:
                shots.append(play["coordinates"])

        except Exception as ex:
            pass

    sns.set_style("white")
    sns.set_color_codes()
    plt.figure(figsize=(12,11))
    for s in shots:
        plt.scatter(s['x'], s['y'])
    plt.show()

if __name__ == '__main__':
    get_all_teams()
    #get_game(2017030146)
