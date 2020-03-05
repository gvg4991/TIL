'''
# 환경 준비
1. 셀레니움 설치
pip install selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys 

2. 크롬 드라이버 설치
chromdriver검색
download chromdriver
chromdriver 78.0.3904...(크롬 버전 확인 후 다운)
자기 운영체제에 맞는 파일 다운로드
실행하는 파이썬 파일이 있는 폴더에 넣어주기


# 브라우저
1. 크롬 브라우저 열기
driver = webdriver.Chrome() #()안에는 파일 경로 작성, 같은 폴더면 공란
url = 'https://google.com'
driver.get(url)
- 큰 창으로 키우기(최대화)
driver.maximize_window()

2. 주소 이동
driver.get('url주소')


#액션
1. 작업 대상 찾기
UI에서 우클릭 후 검사를 통해 elements의 selector명이나 xpath 찾기(아이디:#, 클래스: .)
ex) login_class = '.inputTxt inpBig'

2. 액션 정의
- 클래스명이 하나일때
driver.find_element_by_css_selector('#아이디명').send_keys('파이썬')
- 클래스명이 복수 개 일때
driver.find_elements_by_css_selector('.클래스명')[2].send_keys('파이썬')
- 엔터 입력
from selenium.webdriver.common.keys import Keys #문장이 길어서 Keys로 호출되도록 함, 키보드 입력을 정의
driver.find_elements_by_css_selector('변수명')[1] .send_keys(Keys.ENTER)
- 탭 입력
driver.find_elements_by_css_selector('변수명')[1] .send_keys(Keys.TAB)
- 시프트 누르고 있기
driver.find_elements_by_css_selector('변수명')[1] .key_down(Keys.SHIFT).send_keys('python').key_up(Keys.SHIFT)
- 클릭: .click()
driver.find_element_by_xpath('xpath 경로').click()
- 바로 입력 가능한 화면일 경우
from selenium.webdriver.common.action_chains import ActionChains
action = ActionChains(driver) #변수를 사용해서 드라이브 제어
action.send_keys('파이썬').perform()
action.reset_actions() #액션 초기화 시켜주기

3. 포인터 이동(like 마우스 이동)
move_to_element('변수명')

4. 대기
pause(2)

5. 시간 끌기
import time
time.sleep(2)

6. 창 숨김 모드
options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument("--disable-gpu")
options.add_argument("lang=ko_KR")
options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36")
driver = webdriver.Chrome(chrome_options=options) #크롬드라이버 실행 시, 옵션 넣어주기

7. 파일 다운로드 위치 설정
options.add_experimental_option("prefs", {
  "download.default_directory": "설치 경로",
  "download.prompt_for_download": False,
  "download.directory_upgrade": True,
  "safebrowsing.enabled": False
})
driver = webdriver.Chrome(chrome_options=options) #크롬드라이버 실행 시, 옵션 넣어주기
'''

from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.action_chains import ActionChains
import time

# Headless (창숨김) 모드
options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument("--disable-gpu")
options.add_argument("lang=ko_KR")
options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36")

#파일 다운로드 위치 설정
options.add_experimental_option("prefs", {
  "download.default_directory": "C:\\Users",
  "download.prompt_for_download": False,
  "download.directory_upgrade": True,
  "safebrowsing.enabled": False
})
print('SETTING')

#안랩 접속
driver = webdriver.Chrome(chrome_options=options)
driver.implicitly_wait(20)
print('CHROME')
url = 'https://www.ahnlab.com/kr/site/login/loginForm.do'
driver.get(url)
driver.implicitly_wait(20)
print('AHNLAB')

#로그인
driver.find_element_by_css_selector('#userId').send_keys('csmpower')
driver.find_element_by_css_selector('#passwd').send_keys('semes12_ahnlab')
driver.find_element_by_css_selector('#passwd').send_keys(Keys.ENTER)
driver.implicitly_wait(2)
print('LOGIN')

#엔진파일 다운로드 페이지 이동
driver.get('https://www.ahnlab.com/kr/site/download/product/productEngineList.do')

#v3 통합엔진 설치
driver.find_element_by_xpath('//*[@id="form"]/div[3]/table/tbody/tr[1]/td[4]/a').click()
print('V3 DOWNLOAD')
time.sleep(2)

# #다운로드 관리 페이지
# driver.get('chrome://downloads/')
# time.sleep(2)
# driver.find_element_by_css_selector('#dangerous > div:nth-child(2)').click()