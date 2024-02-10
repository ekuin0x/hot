from bs4 import BeautifulSoup
import requests, lxml
import unicodedata
import threading
import random
import string
import json
import re

headers = {
    'User-agent'
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



def linkedin(keyword,country,new_data) : 
    headers = {
    'User-agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
    }
    PROXY = proxy()
    #variation = ""
    #for i in range(2) :
    #    variation += random.choice(string.ascii_letters).lower()
    if country in ["", "us","usa"] :
        q = f'site:linkedin.com/in/ intitle:{keyword} AND "@gmail.com" AND {variation} '
    else : 
         q = f'site:{country}.linkedin.com/in {keyword} AND "@gmail.com"'
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
            link = unicodedata.normalize('NFKD', li).encode('ascii', 'ignore').decode('utf-8')
            key = unicodedata.normalize('NFKD', keyword).encode('ascii', 'ignore').decode('utf-8')
            #results = re.findall(r'[\+\(]?[1-9][0-9 .\-\(\)]{8,}[0-9]', body)
            results = re.findall(r'[\w.+-]+@[\w-]+\.[\w.-]+', body)
            if len(results) > 0  :
                if len(results[0]) >= 10 :
    
                    new_record = {
                        "Full Name" : fullName,
                        "email" : results[0],
                        "keyword" : key,
                        "source" : link
                    }
                    new_data.append(new_record)

    except : 
        pass



