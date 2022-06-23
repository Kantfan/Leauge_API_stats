import json
import os

path = r'E:\Python_LeagueAPI\matches'
file_list = os.listdir(path)

f = open("PUUID.txt","r")
PUUID = f.read()
f.close()

for file_name in (file_list):
    if file_name.endswith(".json"):
        f = open(f'{path}\{file_name}', encoding = "utf8")
        match_info = json.loads(f.read())
        for i in range(10):
            if match_info["info"]["participants"][i]["puuid"] == PUUID:
                print(match_info["info"]["participants"][i]["championName"])
                break