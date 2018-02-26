import pandas as pd
import requests
import json
import pprint

ID = 8447375 #temp player ID (need to get CSV with all)
PEOPLE = 'people/' #(End point to find certian player, works with ID)
BASE_URL = 'https://statsapi.web.nhl.com/api/v1/'
TEAMS = 'teams/' #need ID at end


def get_teams():
	team_list = []
	for x in range(1, 55):
		res = requests.get(BASE_URL+TEAMS+str(x))
		team = json.dumps((json.loads(res.text)), indent=4)
		my_dict = json.loads(team)
		team_clean = clean_team(my_dict)
		team_list.append(team_clean)
	return (team_list)

def clean_team(data):
	clean = {}
	data = data['teams'][0]
	if data['active']:
		clean['full_name'] = data['name']
		clean['city'] = data['venue']['city']
		clean['location_name'] = data['locationName']
		clean['abbreviation'] = data['abbreviation']
		clean['franchise_id'] = data['franchise']['franchiseId']
		clean['short_name'] = data['shortName']
		clean['division'] = data['division']['name']
		clean['conference'] = data['conference']['name']

		return clean


team_list = get_teams()

FH = open('teams_clean.txt', 'w')
for t in team_list:
	if t:
		print t
		t = json.dumps(t, indent=4)
		FH.write(t)
