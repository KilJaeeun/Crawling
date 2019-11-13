import requests
from bs4 import BeautifulSoup

raw=requests.get('https://movie.naver.com/movie/running/current.nhn',
                 headers={'User-Agent':'Mozilla/5.0'}
                 )
html=BeautifulSoup(raw.text, 'html.parser')



# 컨테이너 수집하기
movie = html.select("dl.lst_dsc")

for m in movie:
    # 영화별 데이터 수집하기
    title = m.select_one("dt.tit a")
    score = m.select_one("div.star_t1 span.num")

    # nth-of-type을 활용해서 데이터를 선택합니다.
    genre = m.select("dl.info_txt1 dd:nth-of-type(1) a")
    directors = m.select("dl.info_txt1 dd:nth-of-type(2) a")
    actors = m.select("dl.info_txt1 dd:nth-of-type(3) a")

    # 평점 조건 주석처리
    # if float(score.text) < 8.5:
    #     continue

    #############################################
    # 추가

    # genre_all을 수집
    # "액션"장르가 아니면 continue
    genre_all = m.select_one("dl.info_txt1 dd:nth-of-type(1) span.link_txt")#html 전체를 받는다.
    print(genre_all)
    if "액션" not in genre_all.text:
        continue
    #############################################

    # 구분선을 출력해줍니다.
    print("=" * 50)
    print("제목:", title.text)


