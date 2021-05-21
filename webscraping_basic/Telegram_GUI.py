from bs4 import BeautifulSoup
import requests
import time
import telepot  # telepot 모듈 import
from telepot.loop import MessageLoop  # 봇 구동
from telepot.namedtuple import InlineKeyboardMarkup as MU  # 마크업
from telepot.namedtuple import InlineKeyboardButton as BT  # 버튼

token = '1647603576:AAFCHkO5MuXcB_0RJpLqXqROjKXFe0R6jfc'  # 봇 API 입력
mc = '1826611044'  # 텔레그램 숫자 ID 입력
bot = telepot.Bot(token)

info_message = "공지사항 크롤링 챗봇"
bot.sendMessage(mc, info_message)


def btn_show(msg):
    if msg['text'] == "소환":
        btn1 = BT(text="1. 공지사항 보기", callback_data="1")
        btn2 = BT(text="2. Bye", callback_data="2")
        mu = MU(inline_keyboard=[[btn1, btn2]])
        bot.sendMessage(mc, "선택하세요", reply_markup=mu)


def query_ans(msg):
    query_data = msg["data"]  # 콜백 데이터
    if query_data == "1":  # 콜백 데이터가 1이라면
        url = "https://www.gachon.ac.kr/community/opencampus/03.jsp?boardType_seq=358"
        res = requests.get(url)
        res.raise_for_status()
        soup = BeautifulSoup(res.text, "lxml")

        # table -> tbody -> tr -> td 순서대로 긁음
        data_rows = soup.find("table").find("tbody").find_all("tr")

        for row in data_rows:
            columns = row.find_all("td")
            # tr 태그 안에 td 가 하나 이하인 데이터는 skip
            if len(columns) <= 1:
                continue

            link = 'https://www.gachon.ac.kr/community/opencampus/'

            post_num = columns[0].get_text().strip()
            title = columns[1].get_text().strip()
            link += columns[1].find('a').attrs['href']

            # 만약 post_num 이 빈 문자열이면 뛰어넘기(image 파일)
            if(post_num == ''):
                continue

            text = '<가천대 게시글 업데이트>' + '\n'
            text += post_num + '\n'
            text += title + '\n'
            text += link
            bot.sendMessage(mc, text=text)
    elif query_data == "2":  # 콜백 데이터가 1이라면
        bot.sendMessage(mc, text="Bye")


MessageLoop(
    bot, {'chat': btn_show, 'callback_query': query_ans}).run_as_thread()

while True:
    time.sleep(5)
