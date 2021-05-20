import requests
url = "http://nadocoding.tistory.com"
headers = {"User.Agent": ""}
res = requests.get(url, headers=headers)
res.raise_for_status()

with open("nadocoding.html", "w", encoding="utf-8") as f:
    f.write(res.text)
