import threading
import requests

res = requests.get("https://api.proxyscrape.com/v3/free-proxy-list/get?request=displayproxies").text.splitlines()

with open("prx.txt", 'a') as f :
    for line in res :
        f.write(line+"\n")


