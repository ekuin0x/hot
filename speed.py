import json
import time

while True :
    with open("phones.json" ,'r') as f :
        start = len(json.loads(f.read()))

    time.sleep(1800)
    
    with open("phones.json" ,'r') as f :
        finish = len(json.loads(f.read()))
        
    diff = finish - start
    print("Collected records in last 30 minutes : " + str(diff))

