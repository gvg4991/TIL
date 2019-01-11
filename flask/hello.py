from flask import Flask
app = Flask(__name__)

@app.route("/") #데코레이터 아래의 함수를 ()와 함께 넘김
def hello(): #함수
    return "Yo! Wor~~ld~~~~~!" #반환값

@app.route('/python') #항상 /로 시작(주소 뒤에 붙일 입력값)
def python():
    return 'yo! python'

@app.route('/dictionary/<string:word>') #<>를 이용하여 다른 여러값을 받음
def dictionary(word):
    dictionary={
        'apple':'사과',
        'banana':'바나나',
        'melon':'멜론',
        'peach':'복숭아'
    }
    result=dictionary.get(word,'나만의 단어장에 없는 단어입니다.') #없으면 기본값 '' 반환
    #dict['apple']로 불러올순 있지만 없으면 Error뜸
    return f'{word}은(는) {result}!'