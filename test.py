import requests

url = f'https://google.com/search?q="California" AND "management" AND phone AND ("213-" OR "(213)") site:www.linkedin.com/in/'

payload = { 'api_key': '33a30461da49603a36091e769f711c37', 'url': url, 'render': True, 'autoparse': True } 
r = requests.get('https://api.scraperapi.com/', params=payload)
print(r.text)
