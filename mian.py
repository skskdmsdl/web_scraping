from flask import Flask, render_template, request, redirect, send_file, jsonify
from naver import get_news as get_naver_news
from hankyung import get_news as get_hankyung_news
from graph import get_graph 
from exporter import save_to_file
import math

app = Flask("WebScrapper")   #앱 만들기 Flask("앱 이름 지정")

db = {}

@app.route("/") # @(데코레이터)는  바로 아래 있는 함수를 찾아 그 함수를 꾸며주는 역할을 함(접속 요청들어오면 바로 아래 함수 실행)
def home():

    return render_template("home.html")

@app.route("/report", methods =['POST'])
def report():
    word = request.get_json("word")
    if "num_page" in word:
        result = word.split('num_page')
        word = result[0]
        page = int(result[1])
    else:
        # 페이지 값 (디폴트값 = 1)
        page = request.args.get("page", 1, type=int)
    # 한 페이지 당 몇 개의 게시물을 출력할 것인가
    limit = 10

    # 그래프 이미지 가져오기
    graph = get_graph()

    if word:
        word = word.lower()
        existingNews = db.get(word)
        if existingNews:
            news = existingNews
            datas = news[(page - 1) * limit:limit*page]

            # 게시물의 총 개수 세기
            tot_count = len(news)
            # 마지막 페이지의 수 구하기
            last_page_num = math.ceil(tot_count / limit) # 반드시 올림을 해줘야함
            # 페이지 블럭을 5개씩 표기
            block_size = 5
            # 현재 블럭의 위치 (첫 번째 블럭이라면, block_num = 0)
            block_num = int((page - 1) / block_size)
            # 현재 블럭의 맨 처음 페이지 넘버 (첫 번째 블럭이라면, block_start = 1, 두 번째 블럭이라면, block_start = 6)
            block_start = (block_size * block_num) + 1
            # 현재 블럭의 맨 끝 페이지 넘버 (첫 번째 블럭이라면, block_end = 5)
            block_end = block_start + (block_size - 1)
        else:
            # 뉴스 기사 가져오기
            naver_news = get_naver_news(word)
            hankyung_news = get_hankyung_news(word)
            news = naver_news + hankyung_news
            db[word] = news

            datas = news[(page - 1) * limit:limit*page]
            # 게시물의 총 개수 세기
            tot_count = len(news)
            # 마지막 페이지의 수 구하기
            last_page_num = math.ceil(tot_count / limit) # 반드시 올림을 해줘야함
            # 페이지 블럭을 5개씩 표기
            block_size = 5
            # 현재 블럭의 위치 (첫 번째 블럭이라면, block_num = 0)
            block_num = int((page - 1) / block_size)
            # 현재 블럭의 맨 처음 페이지 넘버 (첫 번째 블럭이라면, block_start = 1, 두 번째 블럭이라면, block_start = 6)
            block_start = (block_size * block_num) + 1
            # 현재 블럭의 맨 끝 페이지 넘버 (첫 번째 블럭이라면, block_end = 5)
            block_end = block_start + (block_size - 1)

    else:  # 검색어를 입력하지 않은 경우 redirect시키기
        return redirect("/")  
    return jsonify(render_template(
        "report.html", 
        searchingBy=word, 
        resultNumber=len(news),
        news=news,
        datas=datas,
        limit=limit,
        page=page,
        block_start=block_start,
        block_end=block_end,
        last_page_num=last_page_num,
        graph=graph
    ))

@app.route("/export")
def export():
    try:  # try의 코드를 실행하다가 에러가 나면 except의 코드가 실행됨
        word = request.args.get("word")
        if not word:
            raise Exception()  # 만약 word가 존재하지 않으면 exception을 발생시킴
        word = word.lower()
        news = db.get(word)
        if not news:
            raise Exception()
        save_to_file(news)
        return send_file("news.csv")
    except:
        return redirect("/")


app.run(host="127.0.0.1")