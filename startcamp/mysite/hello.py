import os
import random
import requests
from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route('/ping')
def ping():
    return render_template('ping.html')

@app.route('/pong')
def pong():
    name = request.args['name']
    result = random.choice(['yo','wow','OMG'])
    return render_template('pong.html', name_in_html=name, result=result) #왼쪽에 있는 볼은 html에서 이용할 수 있도록 지정해준 값

@app.route('/lotto/<int:num>')
def lotto(num): #입력받은 값(num) 넣어주기
    url = f'https://dhlottery.co.kr/common.do?method=getLottoNumber&drwNo={num}' #입력받은 값(num) 들어가는 자리
    response = requests.get(url)
    lotto = response.json()

    winner = []
    for i in range(1,7):
        winner.append(lotto[f'drwtNo{i}']) #30

    bonus = lotto['bnusNo'] #6

    return render_template('lotto.html',w=winner, b=bonus, n=num)

@app.route('/write')
def write():
    return render_template('write.html')

@app.route('/send')
def send():
    token = os.getenv('TELEGRAM_BOT_TOKEN')
    chat_id = os.getenv('CHAT_ID')

    text=request.args['message']
    requests.get(f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={text}')
    return render_template('send.html')