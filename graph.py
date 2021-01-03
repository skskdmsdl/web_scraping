import requests
from bs4 import BeautifulSoup

def extact_graph(url):
    result = requests.get(url)

    soup = BeautifulSoup(result.text, "html.parser")

    kospi = soup.find("img", {"alt": "코스피지수 상세보기"})["src"] # 코스피지수 그래프
    kosdaq = soup.find("img", {"alt": "코스닥지수 상세보기"})["src"] # 코스닥지수 그래프
    kpi200 = soup.find("img", {"alt": "코스피200지수 상세보기"})["src"] # 코스피200지수 그래프

    return {
        'kospi' : kospi,
        'kosdaq' : kosdaq,
        'kpi200' : kpi200
    } 

def extact_naver_graph(url):
    graph = []
    graph_info = extact_graph(url)
    graph.append(graph_info)

    return graph

def get_graph():
    url = f"https://finance.naver.com"
    graph = extact_naver_graph(url)
    return graph