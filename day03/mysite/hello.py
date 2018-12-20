from flask import Flask, render_template
import random
app = Flask(__name__)

@app.route("/")
def hello(): #route() 갈호안과 같을 필요 없음! 근데 같으면 좋아..
    return "Hello World!"

@app.route("/ssafy")
def ssafy():
    return "This is SSAFY:)"

@app.route("/greeting/<string:name>")
def greeting(name):
    return f'{name}~ 수고했어 오늘도!'

@app.route("/cube.<int:num>")
def cube(num):
    cube=num**3 # == num*num*num
    return str(cube)
    return f'{num}의 세제곱은 {cube}입니다.' #''자체가 스트링이기때문에 str없어도 됨

@app.route("/lunch/<int:person>")
def lunch(person):
    menu=['흰쌀밥','뜨끈한국','각종반찬']
    order=random.sample(menu,person)
    return str(order) #order가 리스트기때문에 스트링으로 바꿔줘야함!

@app.route("/html")
def html():
    multiline_string='''
    '<h1>이것은 h1입니다.</h1>
    <p>이것은 p일까요?</p>
    '''
    return multiline_string

@app.route("/html_file")
def html_file():
    return render_template('html_file.html') #html창에서 설정하겠다.

@app.route("/hi/<string:name>")
def hi(name):
    return render_template('hi.html', nnaammee=name) #hi.html과 nnaammee가 연동됨


@app.route("/fake_naver")
def fake_naver():
    return render_template('fake_naver.html')