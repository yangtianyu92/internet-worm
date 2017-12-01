import requests
from bs4 import BeautifulSoup
import pprint
import lxml
def get_movie_EnglishName():
    movie_list=[]
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 \
                (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36',
               'Host': 'movie.douban.com'}
    for i in range(10):
        link = "https://movie.douban.com/top250?start=" + str(i * 25)
        r = requests.get(link, headers=headers)
        print(str(i+1),"页响应状态码： ",r.status_code)
        soup=BeautifulSoup(r.text,"lxml")
        for tag in soup.find_all(attrs={"class":"item"}):
            title=tag.find_all(attrs={"class":"title"})
            i=0
            for each in title :
                text=each.get_text()
                text=text.replace('/','')
                text=text.lstrip()
                if i==1:
                    movie_list.append(text)
                i+=1
    return movie_list

pprint.pprint(get_movie_EnglishName())