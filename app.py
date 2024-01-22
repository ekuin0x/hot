import json
cities = 0
with open("us.json", 'r') as f :
    data = json.loads(f.read())
    for state in data : 
        for city in data[state] :
            cities += 1

print(cities) 