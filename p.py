from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.proxy import Proxy, ProxyType




def proxy() :
    with open("p.txt", 'r') as f :
        data = f.readlines()
        return random.choice(data)


with open("p.txt", 'r') as f :
    proxies = f.readlines()
    for proxy in proxies :
        options = Options()
        options.add_argument('--proxy-server=http://{}'.format(proxy))
        chrome= webdriver.Chrome()
        chrome.get("https://google.com")
        sleep(5)
        