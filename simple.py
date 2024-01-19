from bs4 import BeautifulSoup
import requests, lxml
from time import sleep
import json
import random

headers = {
    'User-agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
}

with open("geo.json", 'r') as f :
    states = json.loads(f.read())

def proxy() :
    with open("proxies.txt", 'r') as f :
        data = f.readlines()
        p = random.choice(data)
        proxy = ""
    for c in p : 
        if c.isalpha() == True  : 
            break
        else : proxy += c
    return proxy[:-1]

params = {
    'q': '"California" AND "seo" AND phone AND ("213-" OR "(213)") site:www.linkedin.com/in/',
    'gl': 'us',
    'hl': 'en',
    }

while True :
    print("Trying.....")
    p = proxy()
    proxies = {"https" : "http://" + p}
    try :
        html = requests.get('https://google.com/search',proxies=proxies,headers=headers,params=params)
        print(html)
        soup = BeautifulSoup(html.text, 'lxml')
        for result in soup.select('.tF2Cxc'):
            title = result.select_one('.DKV0Md').text
            body = result.select_one(".VwiC3b").text
            link = result.select_one('.yuRUbf a')['href']
            print(title)
            print(link + "\n ----------------------------------------------------------")
    except : 
        print("Failed...")
        pass  
    sleep(2) 
