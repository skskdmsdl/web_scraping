import csv

# csv 파일 저장
# csv 파일 생성
def save_to_file(news):
    file = open("news.csv", mode="w", newline="", encoding="utf-8") # 파일 열기(한줄 띄어쓰기 제거 &한글 깨질 수 있으니 encoding 추가!)
    writer = csv.writer(file)  # 쓰기할 파일 지정하기
    writer.writerow(["title", "company", "date", "link"])  # 리스트로 파일 작성(첫 줄 추가)
    for news_info in news:
        writer.writerow(list(news_info.values()))  # dictionary에서 값만 가져와 list로 만들기(파일에 추가)
    return