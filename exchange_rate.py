import requests
from bs4 import BeautifulSoup

url = "http://finance.daum.net/exchanges"
response = requests.get(url).text

soup = BeautifulSoup(response,'html.parser')
exchange = soup.select("table")

print(exchange)
# for ex in exchange:
#     print(e.select_one("span.num"))

