import json
import os
from collections import OrderedDict


def dictToFile(dict, path):
    with open(path, 'w') as f:
        f.write('{\n')
        c = 0
        for i, j in dict.items():
            if c==len(dict)-1:
                f.write(f'\t"{i}": {j}\n')
            else:
                f.write(f'\t"{i}": {j},\n')
            c += 1
        f.write('}')
path = r'E:\Python_LeagueAPI\matches'
file_list = os.listdir(path)

path = r'E:\Python_LeagueAPI\code'

f = open(f'{path}\PUUID.txt',"r")
PUUID = f.read()
f.close()

path = r'E:\Python_LeagueAPI\matches'


champion_dict = {}

for file_name in (file_list):
    if file_name.endswith(".json"):
        f = open(f'{path}\{file_name}', encoding = "utf8")
        match_info = json.loads(f.read())
        for i in range(10):
            if match_info["info"]["participants"][i]["puuid"] == PUUID:
                offset = 0
                if (i <= 4):
                    offset = 5 
                for j in range(5):
                    champ_name = match_info["info"]["participants"][offset+j]["championName"]
                    if (champ_name not in champion_dict):
                        champion_dict[champ_name] = [0,0]
                    champion_dict[champ_name][1] += 1
                    champion_dict[champ_name][0] += match_info["info"]["participants"][i]["win"]
                break


for champion in champion_dict:
    champion_dict[champion].append(100*champion_dict[champion][0]/champion_dict[champion][1])



path = r'E:\Python_LeagueAPI\code'
dictToFile(OrderedDict(sorted(champion_dict.items(), key=lambda t: t[1][2])), f"{path}\output.json")
# with open(f"{path}\output.json", "w") as outfile:
#     json.dump(champion_dict, outfile, indent=4)

# with open(f'{path}test_output.json', 'w', encoding='utf-8') as f:
#             json.dump(output, f, ensure_ascii=False, indent=4)
