import requests

BASE = "http://127.0.0.1:5000/"
#response = requests.put(BASE + "tworst/1", {"id":"1","tweet_kotor":"kotor","tweet_clean":"bersih"})
response = requests.get(BASE + "video")

print(response.json())