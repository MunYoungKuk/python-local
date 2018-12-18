import requests
from bs4 import BeautifulSoup

url = "http://www.kita.net/exchangeRate_info/exchangeRate_info_list.jsp"
response = requests.get(url).text

soup = BeautifulSoup(response,'html.parser')
exchange = soup.select("tbody tr")

#print(exchange)
for ex in exchange:
    print(ex.select_one("th a").text.strip())
    print(ex.select_one("td").text)

