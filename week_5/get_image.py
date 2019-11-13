from urllib.request import urlretrieve

#############################################
# 추가
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
#############################################

urlretrieve("https://movie-phinf.pstatic.net"
            "/20161103_256/1478160313724rHuDS_JPEG/movie_image.jpg?type=m99_141_2",
            "어벤져스.png")

# 꼭 이미지가 아니더라도 데이터의 주소를 알고있다면 영상이나 프로그램, 문서 등을 모두 다운받을 수 있습니다.