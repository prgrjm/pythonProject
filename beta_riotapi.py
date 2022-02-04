import requests


# 사전에 gethighleague 추가됨
def gethighleague(region, queue='solo'):
    if region in ('br1', 'eun1', 'euw1', 'jp1', 'kr', 'la1', 'la2', 'na1', 'oc1', 'ru', 'tr1'):
        url1 = 'https://' + region + '.api.riotgames.com/lol/league/v4/'
    else:
        return 1

    if queue == 'solo':
        url2 = 'leagues/by-queue/RANKED_SOLO_5x5'
    elif queue == 'flex':
        url2 = 'leagues/by-queue/RANKED_FLEX_SR'
    else:
        return 1

    for tier in ('challenger', 'grandmaster', 'master'):
        url = url1 + tier + url2
        print(url)


gethighleague('kr')


