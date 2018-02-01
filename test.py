import requests
import mysql.connector
from bs4 import BeautifulSoup

def page(pageMax):
    page,p = 1,0
    while(page<pageMax):
        yield p
        p = p+25
        page = page+1
    return 'done'

def start():
    f = open("C:/Users/wangxin69/Desktop/dou.txt","w",encoding="utf-8")
    for p in page(13):
        response = requests.get("https://www.douban.com/doulist/240962/?start="+str(p))
        soup = BeautifulSoup(response.content,"html.parser")
        movies = soup.find_all("div","doulist-item",id=True)
        for movie in movies:
            result = parse(movie)
            f.write(result)
            f.write("\r\n--------------------------------------------------------------------\r\n")

    f.close()



def parse(movie):
    result = []
    post = movie.find_all(class_="post")
    a = post[0].find("a")
    href = a.get("href")

    title = movie.find_all(class_="title")
    name = title[0].get_text()

    rating_nums = movie.find_all(class_="rating_nums")
    score = rating_nums[0].get_text()

    abstract = movie.find_all(class_="abstract")
    abs = str(abstract[0].get_text()).replace("<br>","")

    result.append(name.strip())
    result.append(href.strip())
    result.append(score.strip())
    result.append(abs.strip())
    return "\r\n".join(result)


if __name__ == '__main__':
    start()