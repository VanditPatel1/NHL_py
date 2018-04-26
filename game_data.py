import requests
#import matplotlib.pyplot as plt
#import pandas as pd
#import seaborn as sns
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

def add_player(number):
    print ("ADDING PLAYER")
    db = db_connect()
    data = get_json('https://statsapi.web.nhl.com/api/v1/people/'+str(number))
    packet = dict()
    packet['id'] = data['people'][0]['id']
    packet['first_name'] = data['people'][0]['firstName']
    packet['last_name'] = data['people'][0]['lastName']

    try:
        packet['number'] = data['people'][0]['primaryNumber']
        packet['position'] = data['people'][0]['primaryPosition']['name']
        packet['team'] = data['people'][0]['currentTeam']['name']
    except:
        print ("Not on a team probably")

    db.add_row(packet, 'player_meta')


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
        game_id = game['gameData']['game']['pk']

    except:
        print ("Could not get meta...")
        raise

    else:
        meta['game'] = away + ' @ ' + home
        meta['date'] = time
        meta['game_id'] = game_id
        return meta



def get_all_shots(link, db):

    data = get_json(link)


    live_data = data['liveData']['plays']['allPlays']

    for play in live_data:
        packet = game_meta(data)
        type = play['result']['event']

        """ Period 5 is shootout, 1-4 are regulation and overtime """
        if type in ['Goal', 'Shot'] and play['about']['period'] < 5:

            """ Get Shooter, Goalie and Assist Player ID's """
            for p in play['players']:

                if p['playerType'] in ["Shooter", "Scorer"]:
                    packet['player_id'] = p['player']['id']

                elif p['playerType'] == "Goalie":
                    packet['goalie_id'] = p['player']['id']

                elif p['playerType'] == "Assist":
                    if 'assist_1' in packet:
                        packet['assist_2'] = p['player']['id']
                    else:
                        packet['assist_1'] = p['player']['id']
                else:
                    pass

            try:
                packet['x_coord'] = play['coordinates']['x']
                packet['y_coord'] = play['coordinates']['y']

            except:
                print ("Could not get coordinates")


            try:
                packet['period'] = play['about']['period']
                packet['time'] = play['about']['periodTime']
            except:
                print ("Could not shot timings")

            try:
                packet['shot_type'] = play['result']['secondaryType']

            except:
                print ("Could not get shot type")

            packet['goal'] = False
            packet['strength'] = None

            if 'assist_1' not in packet:
                packet['assist_1'] = None
            if 'assist_2' not in packet:
                packet['assist_2'] = None

            packet['game_winning'] = None
            packet['empty_net'] = None


            if type == 'Goal':
                packet['goal'] = True
                packet['strength'] = play['result']['strength']['name']
                packet['game_winning'] = play['result']['gameWinningGoal']
                packet['empty_net'] = play['result']['emptyNet']


            try:
                db.add_row(packet, 'shots')

            except Exception as ex:
                print ("####### " + str(packet['player_id']) + " #######")
                print ("Player probably did not exists")
                add_player(packet['player_id'])
                db.add_row(packet, 'shots')


def get_all_game_links():
    data = get_json(NHL_URL+ALL_GAMES_2017_2018)
    dates = data['dates']

    for date in dates:
        games = date['games']
        db = db_connect()

        for game in games:
            link = game['link']
            get_all_shots(BASE+link, db)


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
