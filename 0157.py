import requests
from bs4 import BeautifulSoup

r = requests.get("https://www.tvbs.com.tw/")
#print(r.text)


soup = BeautifulSoup(r.text,"html.parser")
# print(soup)
sel = soup.select("div sub_card_text h3")

for s in sel:
    print(s["h3"], s.text)