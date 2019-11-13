import requests
from bs4 import BeautifulSoup

raw=requests.get('https://www.imdb.com/movies-in-theaters/?ref_=nv_mv_inths',
                 headers={'User-Agent':'Mozilla/5.0'}
                 )
html=BeautifulSoup(raw.text, 'html.parser')


###
#컨테이너
#영화제목
#평점
#감독
#배우
# 컨테이너 수집하기
movie = html.select("td.overview-top")

for m in movie:
    # 영화별 데이터 수집하기
    title = m.select_one("h4>a")
    score = m.select_one("div.rating_txt").text.replace("""



 
 

1
2
3
4
5
6
7
8
9
10

5.7/10
X
 
""","").replace("""     
        Metascore
""","")
     #print(score[0].__dir__)
    # nth-of-type을 활용해서 데이터를 선택합니다
    directors = m.select("div.txt-block>span>a")
    actors = m.select("div.txt-block>a")
    genres=m.select_one('p.cert-runtime-genre').text
    if("Action"in genres):
        print("=" * 50)
        print('액션영화')
        print("제목:", title.text)

        print("-" * 50)
        print("평점:", score)

        # 장르, 감독, 배우는 데이터가 여러개일 수 있으므로
        # 반복문을 통해 출력해줍니다.
        print("-" * 50)
     

        print("감독:")
        for d in directors:
            print(d.text)
            
        print("-" * 50)

        print("배우:")
        for d in actors:
            print(d.text)




