from flask import Flask, render_template, request, redirect, send_file
from naver import get_news
from exporter import save_to_file

app = Flask("WebScrapper")   #앱 만들기 Flask("앱 이름 지정")

db = {}

@app.route("/") # @(데코레이터)는  바로 아래 있는 함수를 찾아 그 함수를 꾸며주는 역할을 함(접속 요청들어오면 바로 아래 함수 실행)
def home():

    return render_template("home.html")

@app.route("/report")
def report():
    word = request.args.get("word")  #word라는 이름의 argument를 가져오기
    if word:
        word = word.lower()
        existingNews = db.get(word)
        if existingNews:
            news = existingNews
        else:
            news = get_news(word)
            db[word] = news
    else:  # 검색어를 입력하지 않은 경우 redirect시키기
        return redirect("/")  
    return render_template(
        "report.html", 
        searchingBy=word, 
        resultNumber=len(news),
        news=news
    )

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