import requests
from bs4 import BeautifulSoup

naver_result = requests.get("https://search.naver.com/search.naver?where=news&query=삼성전자&sm=tab_opt&sort=1&photo=0&field=0&reporter_article=&pd=6&ds=&de=&docid=&nso=so%3Add%2Cp%3A6m%2Ca%3Aall&mynews=0&refresh_start=0&related=0")

naver_soup = BeautifulSoup(naver_result.text, "html.parser")

# find로 찾은 결과를 sc_page_inner 변수에 넣고 리스트를 만들어 pages 변수에 넣어주기
sc_page_inner = naver_soup.find("div", {"class": "sc_page_inner"})  #페이징이 있는 클래스 찾기

pages = sc_page_inner.find_all('a')  #페이지를 알기 위해 모든 a태그 찾기 (여기서 pages는 list임)



print(pages)

