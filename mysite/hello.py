from flask import Flask, render_template, request
import random
import requests

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/ssafy")
def ssafy():
    return "This is SSAFY!"

@app.route("/greeting/<string:name>")
def greeting(name):
    return f'반갑습니다! {name}님'

@app.route("/cube/<int:num>")
def cube(num):
    cube = num**3   #int형이므로 str형태로 바꿔야함
    return f'{num}의 세제곱은 {cube}  입니다.'

@app.route("/lunch/<int:person>")
def lunch(person):
    menu = ['햄버거','곱창','짜장면','볶음밥','짬뽕','통닭','피자','삼겹살']
    order = random.sample(menu, person)
    return str(order)

@app.route("/html")
def html():
    multiline_string = '''
        <h1> 이것은 h1 입니다! </h1>
        <p>  여기는 p 입니다 </p>

    '''
    return multiline_string

@app.route("/html_file")
def html_file():
    return render_template('html_file.html')

@app.route("/hi/<string:name>")
def hi(name):
    return render_template('hi.html', name_in_html=name)

@app.route("/fake_naver")
def fake_naver():
    return render_template('fake_naver.html')

@app.route("/ping")
def ping():
    return render_template('ping.html')

@app.route("/pong")
def pong():
    name = request.args['name']

    result = random.choice(['bada.jpg','bada.jpg','bada.jpg'])
    
    return render_template('pong.html', name_in_html=name, result=result)

@app.route('/lotto/<int:num>')
def lotto(num):
    url = f'https://dhlottery.co.kr/common.do?method=getLottoNumber&drwNo={num}'
    response = requests.get(url)
    lotto = response.json()
    
    winner = []
    for i in range(1,7):
        winner.append(lotto[f'drwtNo{i}'])

    bonus = lotto['bnusNo']

    #winner & bonus 리스트를 lotto.html 에 넘겨줘야함.

    return render_template('lotto.html', w=winner, b=bonus, n=num)