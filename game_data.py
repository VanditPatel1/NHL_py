import requests
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import json
from database_connect import db_connect


BASE = 'https://statsapi.web.nhl.com'
NHL_URL = "https://statsapi.web.nhl.com/api/v1/"
TEAMS = '/teams'
GAME = "game/"
LIVE = "feed/live/"
ALL_GAMES_2017_2018 = "schedule?startDate=2017-10-04&endDate=2018-04-07"

def get_json(link):
    try:
        res = requests.get(link)
        data = res.json()

    except Exception as ex:
        print (ex)
        print ("Could not get JSON data from URL {}".format(link))
        raise

    else:
        return data

def get_all_players():

    data = get_json(NHL_URL+TEAMS)

    try:
        teams = data['teams']
        for team in teams:
            if team['active']:

                team_link = team['link']+'/roster'
                data = get_json(BASE+team_link)

                players = data['roster']
                for p in players:
                    """ Build row to insert into DB """
                    packet = list()
                    packet.append(p['person']['id'])
                    first, last = p['person']['fullName'].replace("'", "-").split(" ", 1)
                    packet.append(first)
                    packet.append(last)
                    packet.append(team['name'])
                    try:
                        packet.append(p['jerseyNumber'])
                    except:
                        packet.append(0)
                    packet.append(p['position']['name'])
                    player_add(packet)


    except Exception as ex:
        print ("Could not get all teams")
        raise

def game_meta(game):
    meta = dict()

    try:
        away = game['gameData']['teams']['away']['abbreviation']
        home = game['gameData']['teams']['home']['abbreviation']
        time = game['gameData']['datetime']['dateTime']

    except:
        print ("Could not get meta...")
        raise

    else:
        meta['game'] = away + ' @ ' + home
        meta['datetime'] = time
        return meta

def get_all_shots(link):

    data = get_json(link)
    game_data = game_meta(data)
    print (game_data)



def get_all_game_links():
    data = get_json(NHL_URL+ALL_GAMES_2017_2018)
    dates = data['dates']

    for date in dates:
        games = date['games']

        for game in games:
            link = game['link']
            get_all_shots(BASE+link)


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
    #get_all_teams()
    #get_game(2017030146)
    get_all_game_links()
