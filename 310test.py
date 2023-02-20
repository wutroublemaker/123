import requests
from bs4 import BeautifulSoup

r = requests.get("https://pypi.org/project/beautifulsoup4/")
#print(r.text)


soup = BeautifulSoup(r.text,"html.parser")
#print(soup)
sel = soup.select("div split-layout p")
print(sel)
# for s in sel:
#     print(s["class"], s.text)