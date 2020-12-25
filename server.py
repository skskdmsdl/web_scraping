from flask import Flask, render_template, request  #request안을 들여다봐서 키워드 뽑아올 수 있음(request를 임포트 하는 이유)

app = Flask("WebScrapper")   #앱 만들기 Flask("앱 이름 지정")

@app.route("/") # @(데코레이터)는  바로 아래 있는 함수를 찾아 그 함수를 꾸며주는 역할을 함(접속 요청들어오면 바로 아래 함수 실행)
def home():

    return render_template("home.html")

@app.route("/report")
def report():
    word = request.args.get("word")  #word라는 이름의 argument를 가져오기
    return render_template("report.html", searchingBy=word)

app.run(host="127.0.0.1")