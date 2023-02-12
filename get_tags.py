import requests
import json
taglist = []
id_list = []
for id in range(1,101):
    try:
        response = requests.get(f"https://wallhaven.cc/api/v1/tag/{id}")
        print(response.json()["data"]["name"])
        taglist.append(response.json()["data"]["name"])
        id_list.append(response.json()["data"]["id"])
    except:
        pass

file = open("taglist.txt","a")
for (id,tag) in zip(id_list,taglist):
    file.write(str(id) + "-----> " + tag + "\n")



