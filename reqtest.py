import requests
import json
a={}
url = 'http://127.0.0.1:5005/model/parse'
myobj = {"text":"turn on  fan into 5  "}

x = requests.post(url, json=myobj)

data=x.text
json_data=json.loads(data)
entities=json_data["entities"]
intents=json_data["intent"]
acc=intents["confidence"]
if acc >=.9:
    device=intents["name"]
    a["device"]=device
    for entity in entities:
        # print((entitie))
        if entity["entity"]=="action":
            a["action"]=entity["value"]
            # print(entitie["value"])
        if entity["entity"]=="value":
            a["value"]=entity["value"]

json_a = json.dumps(a)
print(a)
