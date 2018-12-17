import requests
import bs4

response = requests.get('https://finance.naver.com/sise/').text
#print(response.text)

soup = bs4.BeautifulSoup(response,'html.parser')
result = soup.select_one('#KOSPI_now').text
print(f'시세 인정? {result} 응 인정~')

a='!'
marketindex = requests.get('https://finance.naver.com/marketindex/').text
soup = bs4.BeautifulSoup(marketindex,'html.parser')
USD = soup.select_one('#exchangeList > li.on > a.head.usd > div > span.value').text
print('지금 원/달러 환율은 {} 입니다.{}'.format(USD,a))