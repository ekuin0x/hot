# pip install zenrows
from zenrows import ZenRowsClient

client = ZenRowsClient("1a0b5a90d9a65a28eb7da2982827cc0df131c56a")
url = 'https://google.com/search?q="California" AND "marketing" AND phone AND ("213-" OR "(213)") site:www.linkedin.com/in/'
params = {"js_render":"true","autoparse":"true","premium_proxy":"true"}

response = client.get(url,params=params)
print(type(response.text))
