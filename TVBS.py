import requests
from bs4 import BeautifulSoup

r = requests.get("https://news.tvbs.com.tw/entertainment/2039953")
#print(r.text)
if r.status_code == 200:
    print(r.status_code)
else:
    print(r.status_code)


soup = BeautifulSoup(r.text,"html.parser")
#print(soup)
sel = soup.select("div.list a")
print(sel)
for s in sel:
     print(s["href"], s.text)




#0213

Skip to content
Search or jump to…
Pull requests
Issues
Codespaces
Marketplace
Explore
 
@wutroublemaker 
Jason9071
/
CLUT-Python-Class-2
Public
Fork your own copy of Jason9071/CLUT-Python-Class-2
Code
Issues
Pull requests
Actions
Projects
Security
Insights
CLUT-Python-Class-2/web.py /
@Jason9071
Jason9071 init
Latest commit f26d3a6 11 hours ago
 History
 1 contributor
64 lines (43 sloc)  1.39 KB

import requests
from bs4 import BeautifulSoup
import sys
import pymongo

article = []
last_page_link = ""
time = 0

if int(sys.argv[1]) > 5000 :
    time = 5000
else :
    time = int(sys.argv[1])

def capData() :
    r = requests.get("https://www.ptt.cc/bbs/MobileComm/index.html")
    
    global time
    while time > 0:
        
        soup = BeautifulSoup(r.text,"html.parser")
        index_soup = soup.select("div.title a")

        last_page_soup = soup.select("a.btn")


        for l in last_page_soup:
            if "‹ 上頁" == l.text  :
                last_page_link = l["href"]
                

        for i in index_soup:
            r = requests.get("https://www.ptt.cc"+i["href"])
            
            soup = BeautifulSoup(r.text,"html.parser")
            #print(soup)
            article_soup = soup.select("div#main-content")

            article.append({ "html" : str(article_soup), "link" : i["href"] })
            #print(article_soup)


        r = requests.get("https://www.ptt.cc"+last_page_link)
        time -= 1
        print(time)
        #print(len(article_link))

def saveToDB() :
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")

    mydb = myclient["ptt"]

    mycol = mydb["mobel"]
    
    mycol.insert_many(article)

def main() :
    capData()
    saveToDB()
    print("Total article : " + str(len(article)))
    
if __name__ == '__main__':
    main()
    
Footer
© 2023 GitHub, Inc.
Footer navigation
Terms
Privacy
Security
Status
Docs
Contact GitHub
Pricing
API
Training
Blog
About
