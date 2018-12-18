import requests
import bs4

response = requests.get('https://finance.naver.com/marketindex/').text
soup = bs4.BeautifulSoup(response, 'html.parser')
result = soup.select_one('#exchangeList > li.on > a.head.usd > div > span.value').text

print(f'오늘의 원/달러환율은 {result} 입니다')