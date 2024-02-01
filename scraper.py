from bs4 import BeautifulSoup
import requests, lxml
from time import sleep
import unicodedata
import threading
import random
import string
import json
import sys
import re

headers = {
    'User-agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
}
new_data = []
# GET ALL US STATES AREA CODES FOR PHONE NUMBERS FILTERING
with open("geo.json", 'r', encoding = 'utf-8') as f :
    states = json.loads(f.read())

with open("jobs.json", 'r') as f :
    jobs = json.loads(f.read())

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



def linkedin(state,keyword,category,code) : 
    PROXY = proxy()
    variation = (random.choice(string.ascii_letters) + random.choice(string.ascii_letters)).lower()
    countries = ["sa","ae" "kw", "qa", "il"]
    iso = random.choice(countries)
    params = {
        #'q': f'"{state}" AND "{keyword}" AND {variation} AND phone AND ("{code}-" OR "({code})") site:www.linkedin.com/in/',
        #'q' : f'"{state}" AND "{keyword}" AND {variation} AND email and "@gmail.com" site:www.linkedin.com/in/',
        'q' : f'"{keyword}" AND "@gmail.com" site:{iso}.linkedin.com/in/',
        'gl': 'us',
        'hl': 'en',
    }
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
            link = unicodedata.normalize('NFKD', li).encode('ascii', 'ignore').decode('utf-8')
            #results = re.findall(r'[\+\(]?[1-9][0-9 .\-\(\)]{8,}[0-9]', body)
            results = re.findall(r'[\w.+-]+@[\w-]+\.[\w.-]+', body)
            if len(results) > 0  :
                if len(results[0]) > 8 :
                    new_record = {
                        "Full Name" : fullName,
                        "Country": iso ,
                        "email" : results[0],
                        "keyword" : keyword,
                        "category" : category,
                        "source" : link
                    }
                    new_data.append(new_record)

    except : 
        pass

while True :
    #keyword = sys.argv[1]
    keyword = "investor"
    state = ""
    code = ""
    category = ""
    for i in range(299) :
        t = threading.Thread(target=linkedin, args=(state, keyword,category, code,))
        t.start()
    

    with open("estate.json","r") as f :
        data = json.loads(f.read()) 
        for new in new_data :
            if new not in data :
                print(new["email"])
                data.append(new)
        with open("estate.json", "w") as w :
            json.dump(data,w)

    sleep(5)
        

