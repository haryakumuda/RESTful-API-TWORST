import requests

BASE = "http://127.0.0.1:5000/"

response = requests.get(BASE + "maurizka/")
print(response.json())