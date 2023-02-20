import requests
from bs4 import BeautifulSoup

r = requests.get("https://www.ptt.cc/bbs/MobileComm/index.html")
#print(r.text)


soup = BeautifulSoup(r.text,"html.parser")
sel = soup.select("div.nrec span")

for s in sel:
    print(s["class"], s.text)