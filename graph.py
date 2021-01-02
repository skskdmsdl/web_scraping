import requests
from bs4 import BeautifulSoup

def naver_graph(url):
    result = requests.get(url)

    soup = BeautifulSoup(result.text, "html.parser")

    graph = soup.find("img", {"alt": "코스피지수 상세보기"})["src"] # 그래프 이미지
    return graph 

def get_graph():
    url = f"https://finance.naver.com"
    graph = naver_graph(url)
    return graph