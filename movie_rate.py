import requests
from bs4 import BeautifulSoup
url = 'https://www.imdb.com/chart/toptv/?ref_=nv_tvv_250'
headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:133.0) Gecko/20100101 Firefox/133.0'
}
r = requests.get(url, headers=headers)
r.encoding = 'utf-8'
sp = BeautifulSoup(r.text, 'html.parser')

title = sp.select('a h3.ipc-title__text')

rate = sp.select('.ipc-rating-star--rating')

for i in range(len(title)):
    print(f'{title[i].text} {rate[i].text}')
