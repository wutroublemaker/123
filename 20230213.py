import requests
from bs4 import BeautifulSoup
import sys
import pymongo

article = []
last_page_link = ""
# time = 0
time = 3                                            #抓的頁數所執行的次數
# if int(sys.argv[1]) > 5000 :
#     time = 5000
# else :
#     time = int(sys.argv[1])

def capData() :
    r = requests.get("https://www.ptt.cc/bbs/MobileComm/index.html")         #丟網址進來
    
    global time
    while time > 0:
        
        soup = BeautifulSoup(r.text,"html.parser")
        index_soup = soup.select("div.title a")       #選擇網頁的關鍵字

        last_page_soup = soup.select("a.btn")


        for l in last_page_soup:
            if "‹ 上頁" == l.text  :
                last_page_link = l["href"]        #執行上一頁迴圈動作
                

        for i in index_soup:
            r = requests.get("https://www.ptt.cc"+i["href"]) #抓取你執行"上一頁"後 裡面內容的東西
            
            soup = BeautifulSoup(r.text,"html.parser")
            #print(soup)
            article_soup = soup.select("div#main-content")

            article.append({ "html" : str(article_soup), "link" : i["href"] }) #將你抓到的東西塞進一個很像矩陣的地方收集起來
            #print(article_soup)


        r = requests.get("https://www.ptt.cc"+last_page_link)
        time -= 1
        print(time)
        #print(len(article_link))

def saveToDB() :
    myclient = pymongo.MongoClient("mongodb+srv://jasonyaya:jasonyaya@cluster0.rjbp5vy.mongodb.net") #把東西塞進一個DB

    mydb = myclient["just looking"] #資料夾名稱

    mycol = mydb["mobel"] #資料夾名稱的子目錄
    
    mycol.insert_many(article)

def main() :
    capData()
    saveToDB()
    print("Total article : " + str(len(article)))
    
if __name__ == '__main__':
    main()