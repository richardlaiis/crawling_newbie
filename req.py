import requests
from bs4 import BeautifulSoup
res = requests.get("https://quotes.toscrape.com/tag/humor/page/1/")
res.encoding = "utf-8"

soup = BeautifulSoup(res.text, "lxml")
elements = soup.find_all("span", class_ = "text")
# hi
for i in elements:
    print(i.text)
