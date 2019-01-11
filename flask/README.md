# Flask

Flask? 파이썬 기반의 Web Framework로, Web을 구현할 때 사용하는 도구.

http://flask.pocoo.org/



## Flask 설치 및 기본 설정하기

#### Flask is Fun

아래의 코드를 파이썬에 입력.

(Flask 작동시, 구현되는 기본 페이지(Hello world)를 만드는 코드)

```python
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"
```



#### Easy to Setup

- `pip install Flask` : Flask를 설치하는 명령어 (Git Bash에 입력)
- `FLASK_APP=hello.py flask run` : 웹 서버 실행
- `http://127.0.0.1:5000/`를 `ctrl + Click` 하여 웹서버를 실행하면 됨.

- `http://127.0.0.1:5000/` 는 Flask의 기본 주소.


```bash
$ FLASK_APP=hello.py flask run
 * Serving Flask app "hello.py"
 * Environment: production
   WARNING: Do not use the development server in a production environment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

`ctrl + C`  : 웹 서버 종료



#### Debug 모드 적용하기

```bash
$ FLASK_DEBUG=1 FLASK_APP=hello.py flask run
 * Serving Flask app "hello.py" (lazy loading)
 * Environment: production
   WARNING: Do not use the development server in a production environment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 166-987-344
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
127.0.0.1 - - [11/Jan/2019 17:09:22] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [11/Jan/2019 17:09:59] "GET /python HTTP/1.1" 200 -
```

`FLASK_DEBUG=1 FLASK_APP=hello.py flask run`  

- 기본적으로 내용 수정이 필요 한 경우,Flask를 종료한 후에 파이썬 파일의 내용 수정 => 저장 => Flask 재 실행 과 같이 번거로운 절차가 필요하였음.
- 그러나,  Debug 모드를 사용하면,  위의 절차를 거치지 않고 간편히 업데이트가 가능하다.



## Flask 갖고 놀기

#### 페이지 생성 - 기본

```python
@app.route('/python')  
def python():
    return 'Python is fun' 
```

- `route()` : 괄호 안에는 기본 주소 이하의 추가 입력 주소 `/python`를 넣음

- `return`  이하에는 해당 주소에 들어갔을 때 뜨는 결과 값을 입력하면 됨.


#####  `http://127.0.0.1:5000/python ` 입력한 페이지 화면

![1547205918135](C:\Users\harry\AppData\Roaming\Typora\typora-user-images\1547205918135.png)



#### 페이지 생성 - 응용 1

```python
@app.route('/dictionary/<string:word>') 
def dictionary(word):
    return f'{word}을(를) 받았습니다.'
```

- `@app.route('/dictionary/<string:word>')의 <word>` 는 `variable routing` 임. (변경될 수 있는 주소; 변수)
- `word` 앞에 `string:`  (예: `<string:word` ) 을 입력 할 경우, 변수의 자료형에 문자열만 가능하게 됨.
  - 예) `<string:word>`  / `<int:word>`  / `<float:word>` / `<path:word>`
- `def dictionary(word)` : 변수명(word)을 파라미터(괄호 안 내용)로 받아야지 실행이 가능함.



#### 페이지 생성 - 응용 2

```python
@app.route('/dictionary/<string:word>') 
def dictionary(word):
    dictionary = {
        'apple':'사과',
        'banana':'바나나',
        'pear':'배',
        'watermelon':'수박'
    }
     result = dictionary.get(word,'나만의 단어장에 없는 단어입니다')
    return f'{word}은(는) {result}!'   
```

> 딕셔너리의 get 메소드를 이용하면 딕셔너리 내 key에 해당하는 value값을 반환 할 수 있음.
>
> ```python
> # 예시
> dictionary = {'apple':'사과','banana':'바나나','pear':'배', 'watermelon':'수박'}
> dictionary.get('apple')
> >>>'사과'
> ```



이를 이용하여, `http://127.0.0.1:5000/dictionar/apple` 을 주소창에 입력한다면,  

1. `word` => `apple` 로 들어가며,
2. `dictionary.get('apple')`  => `사과`  라는 결과 값이 도출 된다.
3.  따라서, `word`  = `'apple'` , `result` = `'사과'` 로  입력이 됨.

최종적으로 `return` 이하를 formatting을 이용하여 `f'{word}은(는) {result}!'`  로 작성해줄 경우,  웹페이지에는 아래와 같은 화면이 출력된다.

![1547206801622](C:\Users\harry\AppData\Roaming\Typora\typora-user-images\1547206801622.png)

#### get 메소드를 사용한 이유?

일반적으로 딕셔너리는 get 메소드를 사용하지 않고  다음과 같은 방법으로도 key값을 통해 value 값을 접근할 수도 있다. 

하지만 이 방법으로 웹페이지를 구현할 때, 딕셔너리 내에 존재하지 않는 key 값을 불러온다면 에러가 발생한다.

get 메소드의 경우, 딕셔너리 내에 존재 하지 않는 key 값을 불러올 경우 None 을 출력하기 때문에, 에러를 피할 수 있다.

```python
# 예시
dictionary = {'apple':'사과','banana':'바나나','pear':'배', 'watermelon':'수박'}
dictionary.['apple']
>>>'사과'
```

또한, get 메소드는 기본값을 적용할 수 있음. 이를 활용하여, `http://127.0.0.1:5000/dictionar/kiwi`  와 같이, 딕셔너리 내에 존재 하지 않는 키 값을 불러올 때,  기본값이 웹페이지에 출력되게 할 수 있다.

```python
result = dictionary.get(word,'나만의 단어장에 없는 단어입니다')
```

![1547207621103](C:\Users\harry\AppData\Roaming\Typora\typora-user-images\1547207621103.png)

aaa

