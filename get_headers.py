import requests
url = 'https://irs.thsrc.com.tw/IMINT/'
headers = {
    'user-agent':'Mozilla/5.0 (X11; Linux x86_64; rv:133.0) Gecko/20100101 Firefox/133.0'
}
r = requests.get(url, headers=headers)
r.encoding = "utf-8"
print(r.text)
