import requests
from bs4 import BeautifulSoup

def nhlWeb(url):
    source_code = requests.get(url)
    plain_text = source_code.content
    soup = BeautifulSoup(plain_text, "html.parser")
    n = soup.findAll('h3', 'player-jumbotron-vitals__name-num' )
    for name in n:
        print name.string.strip()




nhlWeb('https://www.nhl.com/player')
