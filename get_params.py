import requests
payload = {'emperor': 'KP', 'grass': 'trash'}
res = requests.get("https://httpbin.org/get", params=payload)
if res.status_code == requests.codes.ok:
    print(res.text)

res = requests.post("https://httpbin.org/post", data=payload)
print(res.text)
