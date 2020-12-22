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

def extract_news(html):
    title = html.find("a", {"class": "news_tit"})["title"] # 뉴스 title 정보 
    company = html.find("a", {"class": "info press"}).text
    return {'title': title, 'company': company} #dictionary 생성

def extract_naver_news(last_page):
    news = []
    #for page in range(last_page):
    result = requests.get(f"{URL}&start={0*10}&refresh_start=0") # 뉴스 기사 정보
    soup = BeautifulSoup(result.text, "html.parser")
    results = soup.find_all("div", {"class":"news_wrap api_ani_send"})
    #print(results)
    for result in results:  #results는 html list이고, soup을 사용했으니까 soup의 list이기도 함
        news_info = extract_news(result)
        news.append(news_info) # news_info를 news배열에 담기
    return news
