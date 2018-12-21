
import requests
import os

token = os.getenv('TELEGRAM_BOT_TOKEN')
chat_id = os.getenv('CHAT_ID')
text = '반갑습니다'

# chat_id = '760097723'
# token = '766959295:AAG7uArdPfidy1JjPQaVr2A1aJMJrvuc9pU'

requests.get(f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={text}')



