import riotgames_error
import requests
import pandas
import time

region_list = ('br1', 'eun1', 'euw1', 'jp1', 'kr', 'la1', 'la2', 'na1', 'oc1', 'ru', 'tr1')
tier_list = {'c': 'challenger', 'gm': 'grandmaster', 'm': 'master', 'd': 'diamond', 'p': 'platinum', 'g': 'gold',
             's': 'silver', 'b': 'bronze', 'i': 'iron'}


def gethighleague(region, tier, queue, api_key):
    if region not in region_list:
        raise riotgames_error.RegionError

    if tier not in ('c', 'gm', 'm'):
        raise riotgames_error.TierError
    else:
        tier = tier_list[tier]

    if queue == 'solo':
        queue = 'RANKED_SOLO_5x5'
    elif queue == 'flex':
        queue = 'RANKED_FLEX_SR'
    else:
        raise riotgames_error.QueueError

    url = 'https://' + region + '.api.riotgames.com/lol/league/v4/' + tier + 'leagues/by-queue/' + queue
    while True:
        req = requests.get(url, headers={'X-Riot-Token': api_key})
        return req.headers

    df1 = pandas.DataFrame(req.json())
    df2 = pandas.DataFrame(dict(df1['entries']))
    df2 = df2.transpose()
    df3 = pandas.concat([df1, df2], axis=1)
    df3 = df3.drop(['entries'], axis=1)

    return df3


def getsummoner(region, summoner_id, api_key):
    if region not in region_list:
        raise riotgames_error.RegionError

    url = 'https://' + region + '.api.riotgames.com/lol/summoner/v4/summoners/' + summoner_id
    while True:
        req = requests.get(url, headers={'X-Riot-Token': api_key})
        if req.status_code == 429 or req.status_code == 503:
            print(req)
            time.sleep(60)
        else:
            break

    s1 = pandas.Series(req.json())

    return s1


def getmatches():
    pass


# SUMMONER-V4

def getsummoner_encryptedsummonerid(encryptedsummonerid, region, api_key):
    if region not in ('br1', 'eun1', 'euw1', 'jp1', 'kr', 'la1', 'la2', 'na1', 'oc1', 'ru', 'tr1'):
        pass


    url = 'https://' + region + '.api.riotgames.com/lol/summoner/v4/summoners/' + encryptedsummonerid
