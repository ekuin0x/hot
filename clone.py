from zenrows import ZenRowsClient
from time import sleep
import unicodedata
import threading
import requests
import random
import json
import re

client = ZenRowsClient("53b78420862b3631011daf85ae7acbb17843ed92")



def linkedin(state,keyword,code):
    url = f'https://google.com/search?q="{state}" AND "{keyword}" AND phone AND ("{code}-" OR "({code})") site:www.linkedin.com/in/'
    payload = { 'api_key': '33a30461da49603a36091e769f711c37', 'url': url, 'render': True, 'autoparse': True } 
    response = requests.get('https://api.scraperapi.com/', params=payload).text
    results = json.loads(response)
    for result in results["organic_results"] :
        description = result["snippet"]
        source = result["link"]
        name = ""
        for x in result["title"] :
            if x in ["–", ",","-", "  "] :
                break
            else : name += x    
        exist = 0
        with open("phones.json", 'r') as f :
            data = json.loads(f.read())
            for record in data :
                if record["Full Name"] == name :
                    exist = 1
                    break;
        if exist == 1 : break
        fullName = unicodedata.normalize('NFKD', name).encode('ascii', 'ignore').decode('utf-8')
        #emails = re.search(r'[\w.+-]+@[\w-]+\.[\w.-]+', txt) 
        ph = re.findall(r'[\+\(]?[1-9][0-9 .\-\(\)]{8,}[0-9]', description)
        if len(ph) != 0 and code in ph[0] :
            print(f"phone number detected : {ph[0]} ")
            new_data = {
                "Full Name" : fullName,
                "Country": "United States" ,
                "State" : state,
                "phone" : ph[0],
                "keyword" : keyword,
                "source" : source
            }
            with open("phones.json","r") as f :
                data = json.loads(f.read()) 
                data.append(new_data)
                with open("phones.json", "w") as w :
                    json.dump(data,w)  

keywords = ["management", "lawyer", "fitness", "seo", "sales", "cybersecurity", "doctor","ecommerce", "real estate agent"]
with open("geo.json", 'r') as f :
    states = json.loads(f.read())
    while True :
        keyword = random.choice(keywords)
        state = random.choice(list(states))
        for code in states[state] :
            t1 = threading.Thread(target=linkedin, args=(state, keyword, code,))
            t1.start()
            sleep(1)
        sleep(15)
