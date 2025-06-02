# web_crawling_practice

[CSS Diner](https://flukeout.github.io/)
[크롤링 연습 사이트](https://startcoding.pythonanywhere.com/basic)

## 1일차
- 형제 선택자(Sibling Selector)
동일한 부모를 가진 요소들 중에 특정 요소를 선택하는데 사용
    - 인접 형제 선택자(A+B): A 바로 옆의 B 선택
    - 일반 형제 선택자(A~B): A의 형제들 중에 B인 것 선택
 CSS Diner의 12, 13 문제


- nth-of-type() 선택자
    특정 유형의 요소 중 특정 순서에 해당하는 요소를 선택할 때 사용
    
    - div.main > a:nth-of-type(3)     3번째 선택
    - div.main > a:nth-of-type(even)  짝수번째만 선택
    - div.main > a:nth-of-type(2n+3)  (n=0 부터 시작 3, 5, 7, ..)

- :not(x) 선택자
    특정 선택자와 매칭되지 않는 요소를 선택할 때 사용

    - a:not(#fancy) (id가 fancy가 아닌 것들 선택)
    - div:not(.big, .medium) div태그 중에서 클래스가 big, medium이 아닌 것들 선택

- 속성 선택자
    - 특정 속성을 기준으로 HTML 요소를 선택할 때 사용
        - 기본 속성 선택자 [attribute]
        - 특정 값이 있는 속성 선택자 [attribute="Value"]
        - 특정 값으로 시작되는 속성 선택자 [attribute^="Value"]
        - 특정 값으로 끝나는 속성 선택자 [attribute$="Value"]
        - 특정값을 포함하는 속성 선택자 [attribute*="Value"]

- 텍스트로 태그 찾기
select(), select_one() 은 선택자만 사용해서 태그를 찾을 수 있음
    - 텍스트와 똑같은 태그 **하나** 찾기: `soup.find()`
    - 텍스트와 똑같은 태그 **여러개** 찾기: `soup.find_all()`
    - 실습 [[노트북]](./정적페이지크롤링/텍스트로_태그찾는법.ipynb)

## 2일차
- 네이버 지식인 크롤링 연습: [[노트북]](./정적페이지크롤링/네이버지식인.ipynb)
- 결과: [엑셀](./정적페이지크롤링/naver_kin_crawling.xlsx) 
- 간단정리:
    - 클래스가 두 개 붙어있는 경우 선택자 지정 방법
        - `.` 으로 이어주기
        - 앞에 클래스, 뒤에 클래스 따로 사용가능
    - 특수문자가 붙은 선택자 지정 방법
        - 이스케이프 기호 사용(`\\`)

    - 크롤링 한 데이터 엑셀파일로 변환하는 방법
        - pandas 라이브러리 이용
            - df.to_excel('파일명')

## 3일차
- RISS논문 크롤링 연습 [[노트북]](./정적페이지크롤링/RISS논문크롤링.ipynb)
- 결과: [엑셀](./정적페이지크롤링/RISS_crawlling.xlsx) 
- 간단정리:
    - 파라미터가 많은 경우 → 딕셔너리로 변환
    - 서버에서 요청 거절할 경우 → 헤더 추가
    - SSL 에러 해결방법
        - request.get() 에 verify=False 옵션 추가
    - 텍스트를 이용해 크롤링 하는 법
        - find()
        - find_next_sibling()
        - find_previous_sibling()
        - find_parent()

## 4일차
- 셀레니움 기본 사용법
    - 셀레니움 라이브러리 설치
    - 드라이버 생성 및 기본 기능조작 [노트북](./셀레니움기본사용법/02.웹브라우저_기능조작방법.ipynb)
    - 태그 제어하기 [노트북](./셀레니움기본사용법/03.태그찾고_제어하기.ipynb)
     
- 셀레니움 실전 테크닉 
    - 여러 태그 동시 제어 방법 [노트북](./셀레니움실전테크닉/01.여러태그_동시제어방법.ipynb)
    - 동적 대기기법 [노트북](./셀레니움실전테크닉/02.동적대기기법.ipynb)
    - 고급 입력 컨트롤 [노트북](./셀레니움실전테크닉/03.고급%20입력%20컨트롤.ipynb)
    - 셀렉트박스 조작방법 [노트북](./셀레니움실전테크닉/04.셀렉트박스_조작방법.ipynb)
    - 여러 페이지 관리
    한 페이지 안에 서브페이지가 존재할 경우 웹드라이버는 안쪽에 있는 서브페이지 제어할 수 없음
    **한번에 하나의 페이지만 제어 가능**  

        - 페이지 안에 다른 페이지가 있는 경우(iframe)
            1. iframe 태그 찾기
            2. 선택자 만들고 드라이버로 찾아줌
            3. 드라이버 전환
            `driver.switch_to.frame(iframe)`
            4. 원래 페이지로 전환
            `driver.switch_to.default_content()`
        - 새로운 창 제어 방법
            1. 현재 드라이버가 가지고 있는 창 목록 확인
            `driver.window_handles`
            2. 새로운 창으로 전환하기
            `driver.switch_to.window(driver.window_handles[인덱스])`

        - 실습 : 네이버 메일 자동 보내기
            - [노트북](./셀레니움실전테크닉/05.네이버로그인자동화.ipynb)
            - [노트북](./셀레니움실전테크닉/06.네이버메일자동화.ipynb)