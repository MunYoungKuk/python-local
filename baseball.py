import requests
from bs4 import BeautifulSoup

url = "https://search.daum.net/search?w=tot&DA=YZR&t__nil_searchbox=btn&sug=&sugo=&q=%ED%94%84%EB%A1%9C%EC%95%BC%EA%B5%AC+%EC%88%9C%EC%9C%84"
res = requests.get(url).text

soup = BeautifulSoup(res,'html.parser')
ranks = soup.select("#abtColl > div.coll_cont > div > div.tab_body > div:nth-of-type(1) > div > table > tbody")

for rank in ranks:
    print(rank.select_one("td:nth-of-type(1)").text)
    for r in range(2,11):
        print(rank.select_one("tr:nth-of-type("+str(r)+") > td:nth-of-type(1)").text)
