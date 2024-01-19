import requests
import time


while True :
    res = requests.get("https://raw.githubusercontent.com/zloi-user/hideip.me/main/http.txt").text
    with open("p.txt", 'w', encoding="utf-8") as f :
        f.write(res)
    print("PROXIES REFRESHED.....")
    time.sleep(240)
