import requests
import argparse
import random

TEAMS = {
    'GER',
    'HUN',
    'SCO',
    'SUI',
    'ALB',
    'CRO',
    'ITA',
    'ESP',
    'DEN',
    'ENG',
    'SER',
    'SLO',
    'AUT',
    'FRA',
    'NED',
    'POL',
    'BEL',
    'ROM',
    'SVK',
    'UKR',
    'TUR',
    'CZE',
    'POR',
    'GEO'
}

parser = argparse.ArgumentParser("EURO tYEper")
parser.add_argument("team1", metavar="team1", help="Pierwszy z grajacych zespolow", choices=TEAMS)
parser.add_argument("team2", metavar="team2", help="Drugi z grajacych zespolow", choices=TEAMS)
args = parser.parse_args()

def countLetters(text, letters):
    result = 0
    textLower =  text.lower()
    lettersLower = letters.lower()
    for l in lettersLower:
        result += textLower.count(l)
    return result

quote = requests.get('https://api.kanye.rest').json()['quote']

print('Your Ye quote for today: ', quote)
firstTeamResult = random.randint(0, countLetters(quote, args.team1)) 
secondTeamResult = random.randint(0, countLetters(quote, args.team2))
print(args.team1, ' ', firstTeamResult, ':', secondTeamResult, ' ', args.team2)
