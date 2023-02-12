import os
import requests
import string
import random
import sys

if len(sys.argv) != 2:
    print("python3 getwal.py <query>")
    sys.exit(0)

def get_links(query):
    url = f"https://wallhaven.cc/api/v1/search?q={query}"
    response = requests.get(url)
    data_json = response.json()
    dllinks = []
    for line in data_json["data"]:
        dllinks.append(line["path"])

    return dllinks
def gen_id():

    return ''.join(random.choices(string.ascii_lowercase+string.digits,k=8))

def downloadWal(url):
    print(f"[+] Downloaing -----> {url}")
    wallpaper = requests.get(url)
    ext = os.path.splitext(url)[1]
    wallpaper_name = gen_id()
    save_path = f"/home/king/pix/wallpapers/{wallpaper_name}{ext}"
    open(save_path,"wb").write(wallpaper.content)


walurls = get_links(sys.argv[1])
for url in walurls:
    downloadWal(url)



