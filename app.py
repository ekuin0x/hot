from bs4 import BeautifulSoup
from flask import Flask
import requests, lxml
from time import sleep
import unicodedata
import threading
import random
import json
import re

app = Flask(__name__)

# GET A RANDOM PROXY FROM PROXIES.TXT AND CLEA

with open("geo.json", 'r') as f :
    states = json.loads(f.read())


def proxy() :
    res = requests.get("https://raw.githubusercontent.com/zloi-user/hideip.me/main/http.txt").text
    proxies = res.splitlines()
    p = random.choice(proxies)
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

def linkedin(state, keyword,code) :
    PROXY = proxy()
    params = {
        'q': f'"{state}" AND "{keyword}" AND phone AND ("{code}-" OR "({code})") site:www.linkedin.com/in/',
        'gl': 'us',
        'hl': 'en',
    }
    proxies = {'https' : "http://" + PROXY}
    try :
        html = requests.get('https://www.google.com/search',headers=headers,proxies=proxies, params=params)
        soup = BeautifulSoup(html.text, 'lxml')
        for result in soup.select('.tF2Cxc'):
            title = result.select_one('.DKV0Md').text
            body = result.select_one(".VwiC3b").text
            link = result.select_one('.yuRUbf a')['href']
            name = ""
            for x in title :
                if x in ["–", ",","-", "  "] :
                    break
                else : name += x
            exist = 0
            '''
            with open("phones.json", 'r') as f :
                data = json.loads(f.read())
                for record in data :
                    if record["Full Name"] == name :
                        exist = 1
                        break;
            '''
            if exist == 1 : break
            fullName = unicodedata.normalize('NFKD', name).encode('ascii', 'ignore').decode('utf-8')
            ph = re.findall(r'[\+\(]?[1-9][0-9 .\-\(\)]{8,}[0-9]', body)
            if len(ph) != 0 and code in ph[0] :
                print(f"phone number detected : {ph[0]} ")
                new_data = {
                    "Full Name" : fullName,
                    "Country": "United States" ,
                    "State" : state,
                    "phone" : ph[0],
                    "keyword" : keyword,
                    "source" : link
                }
                '''
                with open("phones.json","r") as f :
                    data = json.loads(f.read()) 
                    data.append(new_data)
                    with open("phones.json", "w") as w :
                        json.dump(data,w)  
                '''
    except : 
        print("proxy failed")
        pass


keywords = ["Administrative assistant", "Customer service","Retail","Finance","Graphic designer","Healthcare","Insurance", "management", "lawyer", "fitness", "seo", "sales", "doctor","ecommerce", "real estate agent"] 

@app.route("/alive")
def alive():
    keyword = random.choice(keywords)
    state = random.choice(list(states))
    for i in range(4):
        print("started")
        code = random.choice(list(states[state]))
        t = threading.Thread(target=linkedin, args=(state, keyword, code,))
        t.start()
    sleep(1)
    return "hello World"
    

if __name__ == '__main__' :
    app.run(port = 5000, debug=False)