import requests
url = "https://api.ipify.org"
r = requests.get(url)
print(r.text)
