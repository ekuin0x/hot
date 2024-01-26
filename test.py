import json

with open("data.json", 'r') as f :
    data = json.loads(f.read())
    unique = { each['Full Name'] : each for each in data }.values()
    with open("data.json", "w") as f :
        json.dump(unique, f)