import requests
import json

url = 'http://127.0.0.1:5005/model/parse'
myobj = {"text":"turn on yellow light"}

x = requests.post(url, json=myobj)

data=x.text
json_data=json.loads(data)
print(type(json_data["intent"]))
print(json_data["entities"])