import requests
from bs4 import BeautifulSoup

url  = "https://www.bithumb.com/"
res = requests.get(url).text
soup = BeautifulSoup(res,'html.parser')

coins = soup.select('tbody.coin_list tr')

print(coins)
