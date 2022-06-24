# import requests module
import requests
import json
from time import sleep

#get API_KEY from text file
f = open("API_KEY.txt","r")
API_KEY = f.read()
f.close()

summoner_name = input("Enter your Sumonner Name: ").replace(" ","%20")

headers = {"X-Riot-Token": API_KEY}
summoner_info = requests.get(f'https://euw1.api.riotgames.com/lol/summoner/v4/summoners/by-name/{summoner_name}', headers=headers)
PUUID = summoner_info.json()['puuid']

f = open("PUUID.txt", "w")
f.write(PUUID)
f.close()

response = requests.get('https://europe.api.riotgames.com/lol/match/v5/matches/by-puuid/'+PUUID+'/ids?type=ranked&start=0&count=100', headers = headers)
matchIDs = response.json()
last_matchID = matchIDs[-1]
counter = 6

for i, matchID in enumerate(matchIDs):
        sleep(1.2)
        match_data = requests.get(f'https://europe.api.riotgames.com/lol/match/v5/matches/{matchID}', headers = headers)
        match_data = match_data.json()
        with open(f'E:\Python_LeagueAPI\matches\matchID{counter}_{i}.json', 'w', encoding='utf-8') as f:
            json.dump(match_data, f, ensure_ascii=False, indent=4)

counter += 1

while len(matchIDs) == 100:
    sleep(1.2)
    response = requests.get('https://europe.api.riotgames.com/lol/match/v5/matches/'+last_matchID, headers = headers)
    last_match_info = response.json()["info"]["gameEndTimestamp"]
    sleep(1.2)
    response = requests.get(f'https://europe.api.riotgames.com/lol/match/v5/matches/by-puuid/{PUUID}/ids?endTime={(last_match_info//1000) -1}&type=ranked&start=0&count=100', headers = headers)
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



