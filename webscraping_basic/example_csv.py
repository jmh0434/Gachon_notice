import csv
import requests
from bs4 import BeautifulSoup

url = "https://www.gachon.ac.kr/community/opencampus/03.jsp?boardType_seq=358"

filename = "gachon(1page).csv"
f = open(filename, "w", encoding="utf-8-sig", newline="")
writer = csv.writer(f)

title = "번호   제목    첨부파일    조회수".split("\t")
# ["N", "종목�?", "?��?���?", ...]
print(type(title))
writer.writerow(title)

res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")

data_rows = soup.find("div", attrs={"class": "boardlist"}).find(
    "tbody").find_all("tr")
for row in data_rows:
    columns = row.find_all("td")
    if len(columns) <= 1:  # ?���? ?��?�� ?��?��?��?�� skip
        continue
    data = [column.get_text().strip() for column in columns]
    print(data)
    # writer.writerow(data)
