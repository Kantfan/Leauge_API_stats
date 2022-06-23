# import requests module
import requests
import json
from time import sleep

# Making a get request
headers = {"X-Riot-Token": ""}
summoner_info = requests.get('https://euw1.api.riotgames.com/lol/summoner/v4/summoners/by-name/DeIeteZhonyas', headers=headers)
puuid = summoner_info.json()['puuid']

response = requests.get('https://europe.api.riotgames.com/lol/match/v5/matches/by-puuid/'+puuid+'/ids?type=ranked&start=0&count=100', headers = headers)
matchIDs = response.json()
last_matchID = matchIDs[-1]
counter = 0

while len(matchIDs) == 100:
    sleep(1.2)
    response = requests.get('https://europe.api.riotgames.com/lol/match/v5/matches/'+last_matchID, headers = headers)
    last_match_info = response.json()["info"]["gameEndTimestamp"]
    sleep(1.2)
    response = requests.get(f'https://europe.api.riotgames.com/lol/match/v5/matches/by-puuid/{puuid}/ids?endTime={(last_match_info//1000) -1}&type=ranked&start=0&count=100', headers = headers)
    sleep(1.2)
    matchIDs = response.json()
    last_matchID = matchIDs[-1]

    for i, matchID in enumerate(matchIDs):
        sleep(1.2)
        match_data = requests.get(f'https://europe.api.riotgames.com/lol/match/v5/matches/{matchID}', headers = headers)
        match_data = match_data.json()
        with open(f'matchID{counter}_{i}.json', 'w', encoding='utf-8') as f:
            json.dump(match_data, f, ensure_ascii=False, indent=4)

    counter += 1





# with open('matchIDs.json', 'w', encoding='utf-8') as f:
#     json.dump(matchid100, f, ensure_ascii=False, indent=4)
#    #json.dump(response2, f, ensure_ascii=False, indent=4)

# print response
print(summoner_info)

# print json content