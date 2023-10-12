import requests
import json

URI = "https://www.dnd5eapi.co/api/classes"

response = requests.get(URI)

#print(f"GET: {response.text}")

response_json = json.loads(response.text)

print(f"{response_json['results'][2]['name']}")

"""
contador = 0
for resultado in response_json['results']:
    contador = contador + 1
    print(contador,".",resultado['name'])
"""