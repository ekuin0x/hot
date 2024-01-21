import requests
import time

headers = {
    'User-agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
}

sources = [
    "https://raw.githubusercontent.com/zloi-user/hideip.me/main/http.txt",
    "https://raw.githubusercontent.com/Zaeem20/FREE_PROXIES_LIST/master/http.txt"
    #"https://api.proxyscrape.com/v3/free-proxy-list/get?request=displayproxies"
]
proxies = ""
while True :
    for source in sources :
        http = requests.get(source, headers = headers).text
        proxies += http
        time.sleep(1)

    with open('proxies.txt') as reader, open('proxies.txt', 'r+') as writer:
        for line in proxies:
            if line.strip():
                writer.write(line)
        writer.truncate()
        writer.write(proxies)

    print("PROXIES REFRESHED.....")
    time.sleep(240)
