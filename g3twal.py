import os
import requests
import string
import random
import sys

usage = "python3 g3twal.py <query> <pg-no>"
if len(sys.argv) != 3:
    print(usage)
    sys.exit(0)
query = sys.argv[1]
page_num = int(sys.argv[2])

def get_links(query):
    dl_links = []
    for page in range(1,page_num+1):
        print(f"[+] Scraping page : {page}")
        url = f"https://wallhaven.cc/api/v1/search?q={query}&page={page}&atleast=1920x1080&sorting=random&order=dec&seed"
        response = requests.get(url)
        json_data = response.json()
        for line in json_data["data"]:
            dl_links.append(line["path"])
    return dl_links

def gen_id():

    return ''.join(random.choices(string.ascii_lowercase+string.digits,k=8))

def downloadWal(url):
    print(f"[+] Downloading -----> {url}")
    wallpaper = requests.get(url)
    ext = os.path.splitext(url)[1]
    wallpaper_name = gen_id()
    save_path = f"/home/king/pix/wallpapers/{wallpaper_name}{ext}"
    open(save_path,"wb").write(wallpaper.content)

walurls = get_links(str(sys.argv[1]))
for url in walurls:
    downloadWal(url)







