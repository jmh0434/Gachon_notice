# /usr/bin/env python
# encoding=utf-8

import requests
from bs4 import BeautifulSoup
import telegram

bot = telegram.Bot(token='1870932706:AAGOxh07epdE-Zhbltigjx2ee-0Sfzs24SY')
channel_id = -1001275971479  # 채널 ID

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

    bot.sendMessage(-1001275971479, text)

    # 터미널 로그
    print(post_num)
    print(title)
    print(link)
