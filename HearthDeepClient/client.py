import kivy
kivy.require('1.0.9')


import json
import requests


headers = {
    'Content-Type': 'application/json'
        }

res = requests.post('http://127.0.0.1:8000/api/hearthlog/', data=json.dumps({"brutLog": "Exemple!!!!!"}), headers={"Content-Type":"application/json"})

print(res.status_code)
assert res.status_code == 201
