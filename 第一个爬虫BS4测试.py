import requests
from bs4 import BeautifulSoup
link="http://www.santostang.com/"
headers={'User-Agent':'Mozilla/5.0(Windows;U;Windows NT 6.1;en-US;rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}
r=requests.get(link,headers=headers)
soup=BeautifulSoup(r.text,"html5lib") #"lxml"经过搜索将其变为html5lib就可以读取了，书上的源代码会报错。
title=soup.find("h1",class_="post-title").a.text.strip()
print(title)
'''
书上UTF-8编码方式不对，会出现乱码PYTHON2的写法不应该带入PYTHON3内。
'''
with open('title.txt',"a+") as f:
    f.write(title)
    f.close
