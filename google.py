from urllib.parse import quote_plus
import requests
from bs4 import BeautifulSoup
#from selenium import webdriver

base_url = "https://www.google.com/search?q="
keyword_url = input("무엇을 검색할까요? : ")
url = base_url + quote_plus(keyword_url) + "&tbm=nws&start=0"

def get_last_page():
    result = requests.get(url)

    soup = BeautifulSoup(result.text, "html.parser")
    pages = soup.find('div')
    for page in pages:
        print(page)

    # for page in pages:
    #     link = page.text
    #     print(link)

def get_news():
    last_page = get_last_page()
    return []




# 1. 페이지 가져오기
# 2. request 만들기
# 3. news 정보 추출하기