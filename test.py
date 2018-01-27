import requests
from bs4 import BeautifulSoup

response = requests.get("https://www.douban.com/doulist/240962/?start=0")
soup = BeautifulSoup(response.content,"html.parser")
movies = soup.find_all(class_="doulist-item")
for movie in movies:
    post = movie.find_all(class_="post")
    a = post[0].find("a")
    href = a.get("href")

    title = movie.find_all(class_="title")
    name = title[0].get_text()

    rating_nums = movie.find_all(class_="rating_nums")
    score = rating_nums[0].get_text()

    abstract = movie.find_all(class_="abstract")
    abs = str(abstract[0].get_text()).replace("<br>","")

    print(name,score,href,abs)