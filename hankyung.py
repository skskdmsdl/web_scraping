from urllib.parse import quote_plus
import requests
from bs4 import BeautifulSoup

# 1. 페이지 가져오기
# 2. request 만들기
# 3. news 정보 추출하기

def get_last_page(url):
    result = requests.get(url)
    soup = BeautifulSoup(result.text, "html.parser")
    pages = soup.find("span", {"class": "num"}).find_all("a")
    for page in pages:
        last_page = page.string

    return int(last_page)

def extract_news(html):
    title = html.find("em", {"class": "tit"}).text.strip()
    company = html.find("p", {"class": "info"}).find("span").string
    date = html.find("span", {"class": "date_time"}).string
    link = html.find("a")["href"]
    return {'title': title,
            'company': company,
            'date': date,
            'link': link}

def extract_hk_news(last_page, url):
    news = []
    for page in range(last_page):
        result = requests.get(f"{url}&page={page+1}")
        soup =BeautifulSoup(result.text, "html.parser")
        results = soup.find_all("div", {"class": "txt_wrap"})
        for result in results:
            hk_news = extract_news(result)
            news.append(hk_news)
    return news

def get_news(word):
    url = f"https://search.hankyung.com/apps.frm/search.news?query={word}"
    last_page = get_last_page(url)
    news = extract_hk_news(last_page, url)
    return news



