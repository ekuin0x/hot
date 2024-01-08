from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
from time import sleep
import unicodedata
import random
import json
import re

def getProxy() :
    with open("proxies.txt") as f :
        proxies = f.readlines()
        proxy = proxies[random.randint(0,len(proxies))]
    px = ""
    for x in proxy :
        if x.isalpha() == False :
            px += x
        else : break
    proxy = px[:-1]
    return proxy

def linkedin(country, city, job):
    options = Options()
    options.add_argument("--headless")
    chrome = webdriver.Chrome(options=options)
    chrome.get(f'https://www.google.com/search?q={city} AND {job} -inurl: dir/ email "@gmail.com" site:{country}.linkedin.com/in/ OR site:{country}.linkedin.com/pub/')
    sleep(2)
    for i in range(8):
        chrome.execute_script("window.scrollTo(0,document.body.scrollHeight)")  
        sleep(1)

    links = chrome.find_elements(By.TAG_NAME, "h3")
    try :
        for i in range(len(links)-1) :
            link = chrome.find_elements(By.TAG_NAME, "h3")[i].text
            txt = chrome.find_elements(By.CSS_SELECTOR, "div[style='-webkit-line-clamp:2']")[i].text
            name = ""
            for x in link :
                if x in ["–", ",","-"] :
                    break
                else : name += x
            
            exist = 0
            with open("data.json", 'r') as f :
                data = json.loads(f.read())
                for record in data :
                    if record["Full Name"] == name :
                        exist = 1
                        break;
            if exist == 1 : break

            fullName = unicodedata.normalize('NFKD', name).encode('ascii', 'ignore').decode('utf-8')
            emails = re.search(r'[\w.+-]+@[\w-]+\.[\w.-]+', txt) 
            if emails != None and bool(re.search(r'\d', fullName)) == False :
                new_data = {
                    "Full Name" : fullName,
                    "Country": country ,
                    "City" : city,
                    "email" : emails[0],
                    "keyword" : job,
                    "source" : "linkedin.com"
                }
                with open("data.json","r") as f :
                    data = json.loads(f.read()) 
                    data.append(new_data)
                    with open("data.json", "w") as w :
                        json.dump(data,w)  
    except : pass

jobs = ["affiliate","management" ,"web development", "seo", "finance", "accounting","programming","insurance", "crypto", "marketing"]
countries = ["UK","IT","ES","CA","SE","DE","FR","BZ","CZ", "MX", "FI", "PL", "NO", "PT", "RO"]

while True :
    job = random.choice(jobs)
    country = random.choice(countries)
    cities = []
    with open("geo.json", 'r',encoding="utf-8") as f :
        data = json.loads(f.read())
        for c in data :
            if country in c["code"] :
                cities.append(c["name"])
    city = random.choice(cities)
    linkedin(country, city, job)
    sleep(random.randint(40,55))
        