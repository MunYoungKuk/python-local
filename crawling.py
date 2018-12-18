import requests
from bs4 import BeautifulSoup

url = "https://www.daum.net"
res = requests.get(url).text

soup = BeautifulSoup(res,'html.parser')
pick = soup.select("#mArticle > div.cmain_tmp > div.section_media > div.hot_issue.issue_mini.hide > div.hotissue_layer > ol > li > div > div:nth-of-type(1) > span.txt_issue > a")

for p in pick:
    print(p)
