import riotgames
import pandas

api_key = 'RGAPI-4b9ab656-15f2-4ee6-9bc1-f07f088b7acb'

var1 = 1
if var1:
    pandas.set_option('display.max_colwidth', None)
    pandas.set_option('display.max_columns', None)
    pandas.set_option('display.max_rows', None)
    pandas.set_option('display.width', None)

var2 = 0
if var2:
    c = riotgames.gethighleague('kr', 'c', 'solo', api_key)
    gm = riotgames.gethighleague('kr', 'gm', 'solo', api_key)
    m = riotgames.gethighleague('kr', 'm', 'solo', api_key)
    pandas.concat([c, gm, m], ignore_index=True).to_csv('highleague.csv', index=False)

var3 = 0
if var3:
    data1 = pandas.read_csv('highleague.csv')
    data2 = pandas.read_csv('summonerid.csv')
    data3 = pandas.concat([data1, data2], axis=1)
    data3 = data3.drop(['id', 'name', 'Unnamed: 0'], axis=1)
    print(data3)

var4 = 0
if var4:
    crab4 = riotgames.getsummoner('kr', 'T4EdIIx3ticsQTXelAW9pKDRYXiQemAijIVvmoasSRSY-UM', api_key)
    hob = riotgames.getsummoner('kr', 'axwm8N5-mQ6uxZttPgqLR8al8AXujBhxZVyfanhroYJR6kz6', api_key)
    print(pandas.concat([crab4, hob], axis=1))

var5 = 0
if var5:
    data = pandas.read_csv('highleague.csv')
    for si in data['summonerId']:
        s1 = riotgames.getsummoner('kr', si, api_key)
        try:
            df1 = pandas.concat([df1, s1], axis=1)
        except NameError:
            df1 = s1
        print(s1)
        print()

    df1 = df1.transpose()
    df1.to_csv('summonerid.csv')

while True:
    c = riotgames.gethighleague('kr', 'c', 'solo', api_key)
    print(c)
    print(c['Retry-After'])
    break
