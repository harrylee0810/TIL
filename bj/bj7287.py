import requests
import bs4

response = requests.get('https://www.acmicpc.net/user/hsgoood11').text
soup = bs4.BeautifulSoup(response, 'html.parser')
result1 = soup.select_one('#statics > tbody > tr.for-chart > td > a').text
result2 = soup.select_one('body > div.wrapper > div.container.content > div.row > div > div > h1').text

print(result1)
print(result2)