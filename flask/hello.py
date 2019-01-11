from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route('/python')
def python():
    return 'Python is fun'


# <word>는 variable routing으로(변경될 수 있는 주소)로, 변수라고 볼 수 있음.
# <word> 앞에 <string:> 을 입력하면, 변수의 자료형에 문자열만 가능하게 됨.
# <string:word> / <int:word> / <float:word> / <path:word>
@app.route('/dictionary/<string:word>') 
def dictionary(word): #변수명을 파라미터로 받아야지 실행이 가능함
    dictionary = {
        'apple':'사과',
        'banana':'바나나',
        'pear':'배',
        'watermelon':'수박'
    }

    #dictionary의 get 메소드를 사용하여 해당 key 값에 대한 value를 반환할 수 있음.
    #[] 사용시, 예) 딕셔너리에 없는 key를 넣을 경우 에러가 발생함.
    #에러 발생 피하기 위해서 .get 메소드를 활용함.
    #key가 없는 경우는 None을 반환함.

    #get은 기본값 또한 설정할 수 있다. 
    #이를 통해, key가 없는 경우(None반환)의 결과 값을 설정 할 수 있음. 
    
    result = dictionary.get(word, '나만의 단어장에 없는 단어입니다')
    return f'{word}은(는) {result}!'