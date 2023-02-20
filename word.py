import jieba
import jieba.analyse
import pymongo


articles = []

def loadNewWordToJeiba():
    lines = []
    with open('word.txt', encoding="utf-8") as f:
        lines = f.readlines()

    n = 0
    while n < len(lines) :
        lines[n] = lines[n].replace("\n", "")
        n += 1

    
    for line in lines :
        jieba.add_word(line)

def cut():
    for a in articles :
        seg_list = jieba.cut(a["content"], cut_all=False)
        #print("Default Mode: " + "/ ".join(seg_list))

        tfidf_list = jieba.analyse.extract_tags(a["content"], topK=20, withWeight=True, allowPOS=())

        #print(tfidf_list)


def getFromDB() :
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")

    mydb = myclient["ptt"]

    mycol = mydb["mobel"]

    for x in mycol.find():
        articles.append(x)

def main() :
    loadNewWordToJeiba()
    getFromDB()
    cut()
    #saveToDB()
    
if __name__ == '__main__':
    main()