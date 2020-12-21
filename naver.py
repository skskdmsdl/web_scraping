import requests
from bs4 import BeautifulSoup

URL = "https://search.naver.com/search.naver?&where=news&query=%EC%82%BC%EC%84%B1%EC%A0%84%EC%9E%90&sm=tab_pge&sort=1&photo=0&field=0&reporter_article=&pd=6&ds=2020.06.23&de=2020.12.20&docid=&nso=so:dd,p:6m,a:all&mynews=0"

def extract_naver_pages():
    result = requests.get(URL)

    soup = BeautifulSoup(result.text, "html.parser")

    # find로 찾은 결과를 sc_page_inner 변수에 넣고 리스트를 만들어 pages 변수에 넣어주기
    sc_page_inner = soup.find("div", {"class": "sc_page_inner"})  #페이징이 있는 클래스 찾기

    links = sc_page_inner.find_all('a')  #페이지를 알기 위해 모든 a태그 찾기 (여기서 pages는 list임)
    pages = []

    for link in links:
        pages.append(int(link.string))

    max_page = pages[-1]
    return max_page

def extract_naver_news(last_page):
    news = []
    for page in range(last_page):
        result = requests.get(f"{URL}&start={page*10}&refresh_start=0")
        print(result.status_code)
    return news

# 페이지 정보 추출까지 성공!
# 이후 뉴스 정보 추출하기