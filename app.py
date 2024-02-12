from bs4 import BeautifulSoup
import requests, lxml
from time import sleep
import unicodedata
import threading
import random
import string
import json
import re

new_data = []
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

headers = {
    'User-agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
    }

def linkedin(keyword) :
    PROXY = proxy()
    variation = (random.choice(string.ascii_letters) + random.choice(string.ascii_letters) + random.choice(string.ascii_letters)).lower()
    q = f'intitle:"{keyword}" "@gmail.com" AND {variation} site:linkedin.com/in'
    params = {'q' : q}
    proxies = {'https' : "http://" + PROXY}
    try :   
        html = requests.get('https://www.google.com/search',headers=headers,proxies=proxies, params=params,timeout=5)
        soup = BeautifulSoup(html.text, 'lxml')
        
        for result in soup.select('.tF2Cxc'):
            title = result.select_one('.DKV0Md').text
            body = result.select_one(".VwiC3b").text
            li = result.select_one('.yuRUbf a')['href']
            name = ""
            for x in title :
                if x in ["–", ",","-", "  "] :
                    break
                else : name += x
        
            fullName = unicodedata.normalize('NFKD', name).encode('ascii', 'ignore').decode('utf-8')
            tit = unicodedata.normalize('NFKD', title).encode('ascii', 'ignore').decode('utf-8')
            link = unicodedata.normalize('NFKD', li).encode('ascii', 'ignore').decode('utf-8')
            key = unicodedata.normalize('NFKD', keyword).encode('ascii', 'ignore').decode('utf-8')
            #results = re.findall(r'[\+\(]?[1-9][0-9 .\-\(\)]{8,}[0-9]', body)
            results = re.findall(r'[\w.+-]+@[\w-]+\.[\w.-]+', body)
            if len(results) > 0  :
                if len(results[0]) >= 10 :
                    new_record = {
                        "Full Name" : fullName,
                        "title" : tit,
                        "email" : results[0],
                        "keyword" : key,
                        "source" : link
                    }
                    new_data.append(new_record)
    except : 
        pass

while True : 

    keyword = "business owner"
    for i in range(299) :
        t = threading.Thread(target=linkedin, args=(keyword,))
        t.start()
    sleep(5)

    with open("giveaway.json", 'r') as f :
        local = json.loads(f.read())
        for new in new_data :
            if new not in local :
                local.append(new)
                print(new["email"])
        with open("giveaway.json", 'w') as w :
            json.dump(local, w)
    new_data = []
