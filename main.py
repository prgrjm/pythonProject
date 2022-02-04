import requests
import pandas
import riotapi

api_key = 'RGAPI-121b4abf-bd36-47d7-84de-d06dc073df70'


def get_master_league():
    url = 'https://kr.api.riotgames.com/lol/league/v4/masterleagues/by-queue/RANKED_SOLO_5x5'
    req = requests.get(url, headers={'X-Riot-Token': api_key})
    if req.status_code == 200:
        print(req.text)
        return req


riotapi.api_key = api_key

alpha = riotapi.gethighleague('kr', 'm', 'solo')
beta = riotapi.gethighleague('kr', 'gm', 'solo')
gamma = riotapi.gethighleague('kr', 'c', 'solo')

print(gamma.reset_index(drop=True))


def get_high_league(tier):
    tier_dict = {'m': 'master', 'gm': 'grandmaster', 'c': 'challenger'}
    url = 'https://kr.api.riotgames.com/lol/league/v4/' + tier_dict[tier] + 'leagues/by-queue/RANKED_SOLO_5x5'
    r = requests.get(url, headers={'X-Riot-Token': api_key})
    return r
