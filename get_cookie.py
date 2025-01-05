import requests
url = "https://www.ptt.cc/bbs/sex/index.html"
cookies = {'over18': '1'}
r = requests.get(url, cookies=cookies)
r.encoding = "utf-8"
print(r.text)
