import json
import time

total = 0
while True :
    try :
        with open("phones.json" ,'r') as f :
            start = len(json.loads(f.read()))

        time.sleep(1800)
        
        with open("phones.json" ,'r') as f :
            finish = len(json.loads(f.read()))
            
        diff = finish - start
        total += diff
        print("Collected records in the last 10 minutes : " + str(diff))
        print(f"Total Collected Data : {total}")
    except : pass
