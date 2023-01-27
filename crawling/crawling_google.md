# 0127 이미지 크롤링 및 다운로드 실습

1. 크롬 웹드라이버 설치
2. jupyter notebook 실행
3. 코드 입력
   - 크롤링을 하려면 selenium을 설치해야함
   - `pip install selenium`


### 1. 라이브러리 실행
`from selenium import webdriver`

`from selenium.webdriver.common.keys import Keys`

`from selenium.webdriver.common.by import By`

`import urllib`

`import time`

---

### 2. 드라이버 실행
`driver = webdriver.Chrome()`

---

### 3. 구글 이미지 사이트로 바로 이동
`driver.get("https://www.google.co.kr/imghp?hl=ko&ogbl")`

---

### 4. html에서 q라는 이름을 가진 요소를 찾아낸다.
`elem = driver.find_element(By.NAME, 'q')`

---

### 5. 검색어 입력
`elem.send_keys('검색어')`

---

### 6. 엔터키 입력
`elem.send_keys(Keys.RETURN)`

---

### 7. 이미지 검색후 무한 스크롤 내리기
`SCROLL_PAUSE_TIME = 3.1`

---

### 8. 
`last_height = 



