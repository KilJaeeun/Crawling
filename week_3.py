import requests
from bs4 import BeautifulSoup

raw = requests.get('https://tv.naver.com/r')
# print(raw.text)
html_parser = BeautifulSoup(raw.text, "html.paser")# 코드에 html 의미를 붜여함.


# 사용 : 변수 이름 =BS.select('선택자')
# 선택자를 사용해 선택자에 해당하는 모든 데이터를 가져온다. 리스트 형식으로 저장됨
# select_one 릉 최초의 하나의 데이트를 가져옴

clips=html_parser.select('div.inner')
title =clips[0].select_one('dt.title')
print(title)