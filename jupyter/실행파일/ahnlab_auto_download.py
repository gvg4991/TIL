from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
import time

#안랩 접속
driver = webdriver.Chrome()
url = 'https://www.ahnlab.com/kr/site/login/loginForm.do'
driver.get(url)

#로그인
driver.find_element_by_css_selector('#userId').send_keys('csmpower')
driver.find_element_by_css_selector('#passwd').send_keys('semes12_ahnlab')
driver.find_element_by_css_selector('#passwd').send_keys(Keys.ENTER)
time.sleep(2)

#엔진파일 다운로드 창 이동
driver.get('https://www.ahnlab.com/kr/site/download/product/productEngineList.do')

#v3 통합엔진 설치
driver.find_element_by_xpath('//*[@id="form"]/div[3]/table/tbody/tr[1]/td[4]/a').click()