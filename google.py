import requests
from bs4 import BeautifulSoup

#주소 변경하기 google로 https://www.youtube.com/watch?v=3b_VMk3WlNY
URL = "https://search.daum.net/search?w=news&sort=recency&q=%EC%82%BC%EC%84%B1%EC%A0%84%EC%9E%90&cluster=n&DA=PGD&dc=STC&pg=1&r=1&p=1&rc=1&at=more&sd=20200623030151&ed=20201223030151&period=6m"

def get_last_page():
    result = requests.get(URL)

    soup = BeautifulSoup(result.text, "html.parser")
    pages = soup.find("div", {"class": "inner_article"}).text
    
    print(pages)
    # for page in pages:
    #     link = page.text
    #     print(link)

def get_news():
    last_page = get_last_page()
    return []




# 1. 페이지 가져오기
# 2. request 만들기
# 3. news 정보 추출하기