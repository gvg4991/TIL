from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
import time
import logging


logger = logging.getLogger(__name__)
formatter = logging.Formatter('[%(asctime)s] %(message)s' )
streamhandler = logging.StreamHandler()
filehandler = logging.FileHandler('C:\\Users/ahnlab_auto_download.log')
streamhandler.setFormatter(formatter)
filehandler.setFormatter(formatter)
logger.addHandler(streamhandler)
logger.addHandler(filehandler)

options = webdriver.ChromeOptions()

# Headless (창숨김) 모드
# options.add_argument('headless')
# options.add_argument("--disable-gpu")
# options.add_argument("lang=ko_KR")
# options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36")

#파일 다운로드 위치 설정
options.add_experimental_option("prefs", {
  "download.default_directory": "C:\\Users",
  "download.prompt_for_download": False,
  "download.directory_upgrade": True,
  "safebrowsing.enabled": False
})
logger.error('SETTING')

#안랩 접속
driver = webdriver.Chrome(chrome_options=options)
driver.implicitly_wait(20)
logger.error('CHROME')
url = 'https://www.ahnlab.com/kr/site/login/loginForm.do'
driver.get(url)
driver.implicitly_wait(20)
time.sleep(1)
logger.error('AHNLAB')

#로그인
driver.find_element_by_css_selector('#userId').send_keys('csmpower')
driver.find_element_by_css_selector('#passwd').send_keys('semes12_ahnlab')
driver.find_element_by_css_selector('#passwd').send_keys(Keys.ENTER)
driver.implicitly_wait(2)
logger.error('LOGIN')

#엔진파일 다운로드 페이지 이동
driver.get('https://www.ahnlab.com/kr/site/download/product/productEngineList.do')

#v3 통합엔진 설치
driver.find_element_by_xpath('//*[@id="form"]/div[3]/table/tbody/tr[1]/td[4]/a').click()
logger.error('V3 DOWNLOAD')
time.sleep(2)