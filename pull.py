import requests
import time


while True :
    res = requests.get("https://raw.githubusercontent.com/zloi-user/hideip.me/main/http.txt").text
    with open("proxies.txt", 'w', encoding="utf-8") as f :
        f.write(res)
    print("PROXIES REFRESHED.....")
    time.sleep(240)
