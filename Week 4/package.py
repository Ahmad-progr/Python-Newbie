import requests
import sys

if len(sys.argv) != 2:
    sys.exit()

response = requests.get(
    "https://itunes.apple.com/search?entity=song&limit=20&term=" + sys.argv[1]
)

o = response.json()

for request in o["results"]:
    print(request["trackName"])
