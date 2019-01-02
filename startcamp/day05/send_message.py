import os
import requests

#token='784700304:AAFl1zcLZDv4JRWjaTl-mAzReT8fJl8kMuA'
#chat_id='718060199'
token = os.getenv('TELEGRAM_BOT_TOKEN')
chat_id = os.getenv('CHAT_ID')

text='yo!'
requests.get(f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={text}')