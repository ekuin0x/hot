from bs4 import BeautifulSoup
import requests, lxml
from time import sleep
import threading
import random


headers = {
    'User-agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
}

def proxy() :
    with open("prx.txt", 'r') as f :
        data = f.readlines()
        p = random.choice(data)
        proxy = ""
    for c in p : 
        if c.isalpha() == True  : 
            break
        else : proxy += c
    return proxy[:-1]

def linkedin() :
    p = proxy()
    proxies = {
        "https" : "http://" + p 
    }
    html = requests.get('https://www.linkedin.com/in/stephen-hall-98a61815b',headers=headers,proxies=proxies)
    soup = BeautifulSoup(html.text, 'lxml')
    print(soup)

for i in range(150) : 
    t = threading.Thread(target=linkedin)
    t.start()