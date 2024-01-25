from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium import webdriver
from time import sleep
import unicodedata
import threading
import random
import json
import re


chrome = webdriver.Chrome()
chrome.get("https://www.linkedin.com/search/results/people/?geoUrn=%5B%22102095887%22%5D&keywords=real%20estate&origin=FACETED_SEARCH&sid=ej9&talksAbout=%5B%22realestate%22%2C%22commercialrealestate%22%5D")
sleep(8000)


