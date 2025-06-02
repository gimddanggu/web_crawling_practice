from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os

link = r"https://www.comcbt.com/xe/r2";
url_list = []
# chrome 설정
options = webdriver.ChromeOptions()
options.add_experimental_option("prefs", {
    "download.default_directory": os.path.abspath("downloads"),
    "plugins.always_open_pdf_externally": True
})
driver = webdriver.Chrome(options=options)

print("다운받을 연도 범위를 입력하세요 (예: 2021 2023)")
start, end = map(int, input("→ ").split())


# 탐색 종료 조건
## 다음 항목 가져왔을 때 가져오는 범위 벗어남 or 
## 마지막 항목일 경우 다음 페이지까지 확인하기
## 마지막 페이지일 경우 



try:
    # 1. 사이트 접속
    driver.get(link)
    time.sleep(2)

    # 2. 게시글의 제목에서 해당년도 기출 찾기
    list_area = driver.find_element(By.CSS_SELECTOR, ".bd_lst") # 전체 덩어리
    all_post = list_area.find_elements(By.CSS_SELECTOR, ".title .hx") # 덩어리 중 하나


    for post in all_post[:2]:
        url = post.get_attribute("href")
        url_list.append(url)
        time.sleep(2)  # 페이지 로딩 대기

    text = all_post[-1].text
    for t in text.split():
        if "년" in t:
            year = int(t.replace("년", ""))

    if year <= end:
        # 다음페이지로 이동
        next_btn = driver.find_element("a.direction")
        next_btn.click()
        
    # 가져온 url 에 접속해 pdf 파일 다운로드
    for ur in url_list:
        driver.get(ur)
        a_tags = driver.find_elements(By.CSS_SELECTOR, "table.bd_tb ul li a")

        for a in a_tags:
            text = a.text.strip()
            href = a.get_attribute("href")

            if "교사용" in text and text.endswith(".pdf"):
                print(text)
                driver.get(href)


        time.sleep(2)

    print("파일 모두 다운로드 완료!")
except Exception as e:
    print("오류 발생:", e)

finally:
    driver.quit()