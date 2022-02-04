import requests
import pandas

api_key = False

region_set = {'br1', 'eun1', 'euw1', 'jp1', 'kr', 'la1', 'la2', 'na1', 'oc1', 'ru', 'tr1'}


class ApiError(Exception):
    def __str__(self):
        return 'wrong api_key'


class RegionError(Exception):
    def __str__(self):
        return 'wrong region'


class TierError(Exception):
    def __str__(self):
        return 'wrong tier'


class QueueError(Exception):
    def __str__(self):
        return 'wrong queue'


def gethighleague(region, tier, queue='solo'):
    if not api_key:
        raise ApiError

    if region not in region_set:
        raise RegionError

    url = 'https://' + region + '.api.riotgames.com/lol/league/v4/'

    if tier == 'm':
        url += 'master'
    elif tier == 'gm':
        url += 'grandmaster'
    elif tier == 'c':
        url += 'challenger'
    else:
        raise TierError

    url += 'leagues/by-queue/'

    if queue == 'solo':
        url += 'RANKED_SOLO_5x5'
    elif queue == 'flex':
        url += 'RANKED_FLEX_SR'
    else:
        raise QueueError

    r = requests.get(url, headers={'X-Riot-Token': api_key})

    if r.status_code == 200:
        r = pandas.DataFrame(r.json())
        r = pandas.DataFrame(dict(r['entries']))
        r = r.transpose()
        r = r[['summonerName', 'leaguePoints', 'wins', 'losses', 'summonerId']]

        return r.sort_values(by=['leaguePoints'], ascending=False)
    else:
        pass
