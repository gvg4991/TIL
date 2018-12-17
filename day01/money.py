import requests
import bs4

marketindex = requests.get('https://finance.naver.com/marketindex/').text
soup = bs4.BeautifulSoup(marketindex,'html.parser')
USD = soup.select_one('#exchangeList > li.on > a.head.usd > div > span.value').text
print('지금 원/달러 환율은 ' + USD + ' 입니다.')