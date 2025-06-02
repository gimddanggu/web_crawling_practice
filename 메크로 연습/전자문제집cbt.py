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

try:
    # 1. 사이트 접속
    driver.get(link)
    time.sleep(2)

    # 2. 게시글의 제목에서 해당년도 기출 찾기
    list_area = driver.find_element(By.CSS_SELECTOR, ".bd_lst")
    all_post = list_area.find_elements(By.CSS_SELECTOR, ".title .hx")

    for post in all_post[:2]:
        url = post.get_attribute("href")
        url_list.append(url)
        time.sleep(2)  # 페이지 로딩 대기


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