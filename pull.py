import requests
import time


while True :
    res = requests.get("https://raw.githubusercontent.com/prxchk/proxy-list/main/all.txt").text
    with open("p.txt", 'w') as f :
        f.write(res)
    print("PROXIES REFRESHED.....")
    time.sleep(240)
