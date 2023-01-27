# 0127 이미지 크롤링 및 다운로드 실습

# pip install selenium을 통해 셀레니움 설치먼저 해야함.

# 크롤링하기 위한 라이브러리 실행
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import urllib
import time

# driver실행
driver = webdriver.Chrome()

# 이미지 사이트 한번에 이동
driver.get("https://www.google.co.kr/imghp?hl=ko&ogbl")

# html에서 input name이 q인 요소 찾아낸다.
elem = driver.find_element(By.NAME, 'q')

# 검색어 입력
elem.send_keys('검색어 입력')

# 엔터키 입력
elem.send_keys(Keys.RETURN)

# 이미지 검색후 무한 스크롤 내리기
SCROLL_PAUSE_TIME = 2.9

# 스크롤의 높이 가져옴
last_height = driver.execute_script('return document.body.scrollHeight')

while True:
    # 끝까지 스크롤 다운
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # 1초 대기
    time.sleep(SCROLL_PAUSE_TIME)

    # 스크롤 다운 후 스크롤 높이 다시 가져옴.
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        # 'my4qd'라는 클래스명 선택해서(찾아서) 클릭
        try : 
            driver.find_element(By.CSS_SELECTOR, '.mye4qd').click()
        except:
            break
    # last_height를  new_height로 갱신
    last_height = new_height

# 검색해서 나온 큰 그림의 CSS_Selector 전체 가져오기
imgs = drive.find_elements(By.CSS_SELECTOR, '.rg_i_Q4Luwd')

# cnt값 1로 선언하고
cnt = 1 

# 반복문으로 이미지 요소 배열들 돌며 작업
for img in imgs :
    try:
        # 이미지 클릭
        img.click()

        # 기다리는 시간(로딩시간) 설정
        time.sleep(3.1)

        # 미리보기 이미지 클릭해서 큰 이미지 띄우고, 선택해서 src 속성 가져오기
        src = driver.find_element(By.CSS_SELECTOR, '.n3VNCb').get_attribute('src')

        # 이미지 다운로드
        urllib.request.urlretrieve(src, str(cnt)+'.png')
        cnt += 1

    except:
        pass

driver.close()

