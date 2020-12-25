from naver import get_news as get_naver_news
from hankyung import get_news as get_hankyung_news
from save import save_to_file



naver_news = get_naver_news()
hankyung_news = get_hankyung_news()
news = naver_news + hankyung_news

#save_to_file(news)

