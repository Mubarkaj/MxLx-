import json
with open("data.json",'r') as f:
        data= json.load(f)
with open("json.json",'a')as jsn:
        itemlist=[i for n, i in enumerate(data) if n % 2 == 0]
        json.dump(itemlist,jsn,indent=4)