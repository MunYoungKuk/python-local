import requests
from bs4 import BeautifulSoup

url = "http://finance.daum.net/exchanges"
res = requests.get(url).text

soup = BeautifulSoup(res,'html.parser')
ex = soup.select("tbody tr")

print(ex)
for e in ex:
    print(e.select_one("span.num"))

