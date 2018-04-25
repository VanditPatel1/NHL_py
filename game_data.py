import requests
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import json
from database_connect import player_add


URL = 'https://statsapi.web.nhl.com/api/v1/teams'
BASE = 'https://statsapi.web.nhl.com'
NHL_URL = "https://statsapi.web.nhl.com/api/v1/"
GAME = "game/"
LIVE = "feed/live/"

def get_players(team_link, team):

    try:
        res = requests.get(BASE+team_link)
        players = res.json()['roster']
        for p in players:
            packet = list()
            packet.append(p['person']['id'])
            first, last = p['person']['fullName'].replace("'", "-").split(" ", 1)
            packet.append(first)
            packet.append(last)
            packet.append(team)
            try:
                packet.append(p['jerseyNumber'])
            except:
                packet.append(0)
            packet.append(p['position']['name'])
            print (packet)
            player_add(packet)

    except Exception as ex:
        print ("Could not get team")
        raise

def get_all_teams():

    res = requests.get(URL)

    try:
        data = res.json()
        teams = data['teams']
        for team in teams:

            if team['active']:
                get_players(team['link']+'/roster', team['name'])

    except Exception as ex:
        print ("Could not get all teams")
        raise


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
