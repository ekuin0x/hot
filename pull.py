import requests
import time


while True :
    res = requests.get("https://github.com/zloi-user/hideip.me/blob/main/https.txt").text
    with open("p.txt", 'w') as f :
        f.write(res)
    print("PROXIES REFRESHED.....")
    time.sleep(240)
