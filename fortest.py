import requests
import pandas

api_key = 'RGAPI-4b9ab656-15f2-4ee6-9bc1-f07f088b7acb'


r = requests.get('https://kr.api.riotgames.com/lol/summoner/v4/summoners/by-name/깨달은 탑솔', headers={'X-Riot-Token': api_key})
print(r.text)

