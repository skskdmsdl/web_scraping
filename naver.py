import requests
from bs4 import BeautifulSoup

def get_last_page(url):
    result = requests.get(url)

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
    company = html.find("a", {"class": "info press"}).text # 신문사 정보
    date = html.find("div", {"class": "info_group"}).find_all("span")[-1].string # date
    link = html.find("a")["href"]  # 링크 주소
    return {
        'title': title, 
        'company': company,
        'date': date,
        'link': link} #dictionary 생성

def extract_naver_news(last_page, url):
    news = []
    for page in range(last_page):
        result = requests.get(f"{url}&start={page*10}") # 뉴스 기사 정보
        soup = BeautifulSoup(result.text, "html.parser")
        results = soup.find_all("div", {"class":"news_wrap api_ani_send"})
    for result in results:  #results는 html list이고, soup을 사용했으니까 soup의 list이기도 함
        news_info = extract_news(result)
        news.append(news_info) # news_info를 news배열에 담기
    return news

def get_news(word):
    url = f"https://search.naver.com/search.naver?&where=news&query={word}"
    last_page = get_last_page(url)
    news = extract_naver_news(last_page, url)
    return news
