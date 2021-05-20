import requests
from bs4 import BeautifulSoup
import telegram

bot = telegram.Bot(token='1870932706:AAGOxh07epdE-Zhbltigjx2ee-0Sfzs24SY')
url = "https://comic.naver.com/webtoon/weekday.nhn"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")
# 네이버 웹툰 전체 목록 가져오기
cartoons = soup.find_all("a", attrs={"class": "title"})
# a element의 class 속성이 title인 모든 "a" element 반환
for cartoons in cartoons:
    bot.sendMessage(-1001482460031, cartoons.get_text())
