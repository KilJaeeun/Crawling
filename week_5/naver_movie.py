import requests
from bs4 import BeautifulSoup

raw=requests.get('https://movie.naver.com/movie/running/current.nhn',
                 headers={'User-Agent':'Mozilla/5.0'}
                 )
html=BeautifulSoup(raw.text, 'html.parser')


###
#컨테이너
#영화제목
#평점
#장르
#감독
#배우
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
    a=False
    for g in genre:
        if ("액션"in g.text):
            a=True
        else:  continue


    if((float(score.text)>=8.5)and a):
        # 구분선을 출력해줍니다.
        print("=" * 50)
        print("제목:", title.text)

        print("-" * 50)
        print("평점:", score.text)

        # 장르, 감독, 배우는 데이터가 여러개일 수 있으므로
        # 반복문을 통해 출력해줍니다.
        print("-" * 50)
        print("장르:")
        for g in genre:
            print(g.text)

        print("-" * 50)
        print("감독:")
        for d in directors:
            print(d.text)
# movies=html.select('dl.lst_dsc')
#
# for movie in movies:
#     title=movie.select_one('dt.tit>a').text
#     print('제목', title)
#     star=movie.select_one('div.star_t1>a>span.num').text
#     print('평점: ', star)
#     genres_gamdoc_actors=movie.select('span.link_txt')
#     #print(genres)
#     # print('장르: ',end ='')
#     genres=genres_gamdoc_actors[0].select('a')
#     gamdoc=genres_gamdoc_actors[1].select('a')
#     actors=genres_gamdoc_actors
#     print(type(str(actors[2]).replace(",", "")))
    # print('장르: ',end ='')
    # for gen in genres:
    #     print( gen.text , end=',')
    #
    # print('\n감독: ',end ='')
    #
    # for gen in gamdoc:
    #     print( gen.text , end=',')
    # print('\n')

    # gamdoc=movie.select_one('span.link_txt>a')[1]
    # print('감독 : '+ gamdoc)
    # actors=movie.select('span.link_txt>a')[2]
    # print('배우: ',end ='')
    # for actor in actors:
    #     print(actor.text,  end=',')
    # print('='*30)



