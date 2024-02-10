from scraper import linkedin
from bs4 import BeautifulSoup
import requests, lxml
from time import sleep
import unicodedata
import threading
import random
import string
import json
import re

def api(keyword, country) :
    new_data = []
    while len(new_data) <= 10 :
        for i in range(99) :
            t = threading.Thread(target=linkedin, args=(keyword,country,new_data))
            t.start()
        sleep(5)
    return(new_data)

while True : 
    country = random.choice(["de", "ca"])

    if country == "ca" : 
        keywords = [
            "Property management sale",
            "Real estate management selling",
            "Property manager contact",
            "Management selling properties",
            "Commercial property management sale",
            "Property management sales listings",
            "Real estate manager for sale",
            "Selling managed properties",
            "Property management sell services",
            "Ready to sell property management"
        ]
    else :
        keywords = [
            "Immobilienverwaltung Verkauf",
            "Hausverwaltung Immobilienverkauf",
            "Verkauf durch Verwalter",
            "Immobilienverwalter Kontakt",
            "Immobilienverwaltung Portfolio Verkauf"
            "Gewerbeimmobilien Verwaltung Verkauf",
            "Verwaltung von Verkaufsimmobilien",
            "Immobilienverwaltung Verkaufsangebote",
            "Immobilienverwalter Verkaufsservice",
            "Verkaufsbereite Immobilienverwaltung",
        ]

    keyword = random.choice(keywords)

    data = api(keyword, country)
    with open("estate.json", 'r') as f :
        local = json.loads(f.read())
        for new in data :
            if new not in local :
                local.append(new)
        with open("data.json", 'w') as w :
            json.dump(local, w)