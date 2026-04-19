import requests
from bs4 import BeautifulSoup
urls=[
    f"https://www.cnblogs.com/#p{page}"
    for page in range(1,50+1)
]
#生产者
def craw(url):
    r=requests.get(url)
    #print(url,len(r.text))
    return r.text

def parse(html):
    #class="post-item-title"
    soup=BeautifulSoup(html,'html.parser')
    links=soup.find_all('a',class_='post-item-title')
    return [(link["href"],link.get_text()) for link in links]


if __name__=="__main__":
    #用for循环遍历解析结果里的每一个(href, title)，每次循环把结果赋值给result变量
    for result in parse(craw(urls[2])):
        print(result)
