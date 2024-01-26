from bs4 import BeautifulSoup
import requests, lxml
from time import sleep
import unicodedata
import threading
import random
import string
import json
import re

headers = {
    'User-agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
}

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

new_data = []

def linkedin(state,keyword,category,code) : 
    PROXY = proxy()
    variation = (random.choice(string.ascii_letters) + random.choice(string.ascii_letters)).lower()
    params = {
        'q': f'"{state}" AND "{keyword}" AND {variation} AND phone AND ("{code}-" OR "({code})") site:www.linkedin.com/in/',
        #'q' : f'"{state}" AND "{city}" AND "{keyword}" AND "@gmail.com" site:www.linkedin.com/in/',
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
            exist = 0
            with open("data.json", 'r') as f :
                data = json.loads(f.read())
                for record in data :
                    if record["Full Name"] == name :
                        exist = 1
                        break;
            if exist == 1 : 
                break
            fullName = unicodedata.normalize('NFKD', name).encode('ascii', 'ignore').decode('utf-8')
            link = unicodedata.normalize('NFKD', li).encode('ascii', 'ignore').decode('utf-8')
            results = re.findall(r'[\+\(]?[1-9][0-9 .\-\(\)]{8,}[0-9]', body)
            #results = re.findall(r'[\w.+-]+@[\w-]+\.[\w.-]+', body)
            if len(results) > 0  :
                if len(results[0]) > 11 and len(results[0]) < 18 :
                    print("new number")
                    new_record = {
                        "Full Name" : fullName,
                        "Country": "United States" ,
                        "State" : state,
                        "phone" : results[0],
                        "keyword" : keyword,
                        "category" : category,
                        "source" : link
                    }
                    new_data.append(new_record)

    except : 
        pass

while True :
    job = random.choice(list(jobs))
    #category = job["category"]
    #try : keyword = random.choice(job["keywords"])[0]
    #except : keyword = category
    '''
    for state in list(states) :
        print("------state----" + state)
        for code in list(states[state]) :
    '''
    category = "real estate"
    keyword = "real estate agent"
    #state = "California"
    for state in list(states) :
        print(f"------------------- {state} -------------------")
        for code in list(states[state]):
            for i in range(449) :
                t = threading.Thread(target=linkedin, args=(state, keyword,category, code,))
                t.start()
            sleep(5)

        with open("data.json","r") as f :
            data = json.loads(f.read()) 
            for new in new_data : 
                data.append(new)
            with open("data.json", "w") as w :
                json.dump(data,w) 

        

