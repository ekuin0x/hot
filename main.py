from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium import webdriver
from time import sleep
import unicodedata
import random
import json
import re
import threading


with open("geo.json", 'r') as f :
    states = json.loads(f.read())

def proxy() :
    with open("p.txt", 'r') as f :
        data = f.readlines()
        p = random.choice(data)
        proxy = ""
    for c in p : 
        if c.isalpha() == True  : 
            break
        else : proxy += c
    return proxy[:-1]


def linkedin(state,keyword,code):
    options = Options()
    PROXY = proxy()
    options.add_argument('--proxy-server=http://{}'.format(PROXY))
    options.add_argument('--window-size=150,50')
    #options.add_argument("--headless") 
    chrome = webdriver.Chrome(options=options)
    chrome.get(f'https://google.com/search?q="{state}" AND "{keyword}" AND phone AND ("{code}-" OR "({code})") site:www.linkedin.com/in/')
    sleep(2)
    try:   
        # SCROLL DOWN
        for i in range(10):
            chrome.execute_script("window.scrollTo(0,document.body.scrollHeight)")  
            try : 
                chrome.find_element(By.CSS_SELECTOR, 'a[aria-label="Plus de résultats"]').click()
            except : pass
            sleep(1)
        links = chrome.find_elements(By.TAG_NAME, "h3")

        for i in range(len(links)-1) :
            link = chrome.find_elements(By.TAG_NAME, "h3")[i].text
            txt = chrome.find_elements(By.CSS_SELECTOR, "div[style='-webkit-line-clamp:2']")[i].text
            name = ""
            for x in link :
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
            ph = re.findall(r'[\+\(]?[1-9][0-9 .\-\(\)]{8,}[0-9]', txt)
            if len(ph) != 0 and code in ph[0] :
                print(f"phone number detected : {ph[0]} ")
                new_data = {
                    "Full Name" : fullName,
                    "Country": "United States" ,
                    "State" : state,
                    "phone" : ph[0],
                    "keyword" : keyword,
                    "source" : "https://linkedin.com/in/"
                }
                with open("phones.json","r") as f :
                    data = json.loads(f.read()) 
                    data.append(new_data)
                    with open("phones.json", "w") as w :
                        json.dump(data,w)  
            states[state].remove(code)

    except :
        pass

keywords = ["management", "lawyer", "fitness", "seo", "sales", "cybersecurity", "doctor","ecommerce", "real estate agent"]


while True :
    for keyword in keywords :
        for state in states :
            print(state + "--------" + keyword)
            max = 0
            for code in states[state] :
                if max <= 2 :
                    t = threading.Thread(target=linkedin, args=(state, keyword, code,))
                    t.start()
                    max += 1
                else : break
            sleep(60)
