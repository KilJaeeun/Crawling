# 네이버 지도 데이터 수집하기
# 네이버 지도 데이터 수집하기
from selenium import webdriver

##################################################
# 파이썬 내부 라이브러리 time을 사용합니다.
# time: 시간과 관련된 여러가지 기능을 포함합니다.
import time
##################################################

driver = webdriver.Chrome("./chromedriver")
# 구버전 네이버지도 접속
driver.get("https://v4.map.naver.com")
# !!!추가//네이버 지도 업데이트 후 안내메시지 끄기##########
# 무시하고 진행해주세요.
driver.find_elements_by_css_selector("button.btn_close")[1].click()
##################################################

#3. 검색창에 검색어 입력하기 // 검색창: input#search-input
search_box = driver.find_element_by_css_selector("input#search-input")
search_box.send_keys("치킨")
#4. 검색버튼 누르기 // 검색버튼: button.spm
search_button = driver.find_element_by_css_selector("button.spm")
search_button.click()

##################################################
# 1초의 지연시간을 줍니다.
time.sleep(1)
##################################################

# 컨테이너(가게 정보) 수
stores = driver.find_elements_by_css_selector("div.lsnx")
for store in stores:
    # 세부 데이터 수집
    name = store.find_element_by_css_selector("dt > a").text
    addr = store.find_element_by_css_selector("dd.addr").text
    phone = store.find_element_by_css_selector("dd.tel").text

    print(name, addr, phone)
driver.close()