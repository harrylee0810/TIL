# Flask

Flask? 파이썬 기반의 Web Framework로, Web을 구현할 때 사용하는 도구.

http://flask.pocoo.org/



## Flask 설치 및 기본 설정하기

### Flask is Fun

아래의 코드를 파이썬에 입력.

(Flask 작동시, 구현되는 기본 페이지(Hello world)를 만드는 코드)

```python
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"
```



### Easy to Setup

아래 명령어를 Git Bash에 입력하여 Flask를 설치함.

`pip install Flask` : Flask를 설치하는 명령어 (Git Bash에 입력)

`FLASK_APP=hello.py flask run` : 웹 서버 실행



`http://127.0.0.1:5000/`를 `ctrl + Click` 하여 웹서버를 실행하면 됨.

`http://127.0.0.1:5000/` 는 Flask의 기본 주소.

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



### Debug 모드 적용하기

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

기본적으로 내용 수정이 필요 한 경우,Flask를 종료한 후에 

수정 => 저장 => Flask 재 실행이 필요하나,  위 Debug 모드를 사용하면,  위의 절차를 거치지 않고 간편히 업데이트가 가능하다.



## Flask 갖고 놀기

```python
@app.route('/python')  
def python():
    return 'Python is fun' 
```

`route()` : 괄호 안에는 기본 주소 이하의 추가 입력 주소 `/python`를 넣음

`return`  이하에는 해당 주소에 들어갔을 때 뜨는 결과 값을 입력하면 됨. 



```python
@app.route('/dictionary/<string:word>') 
def dictionary(word):
    return f'{word}을(를) 받았습니다.'
```

`<word>` 는 `variable routing` 임. (변경될 수 있는 주소; 변수)

`word` 앞에 `string:`  (예: `<string:word` ) 을 입력 할 경우, 변수의 자료형에 문자열만 가능하게 됨.

예) `<string:word>`  / `<int:word>`  / `<float:word>` / `<path:word>`

`def dictionary(word)` :또한 변수명(word)을 파라미터(괄호안 내용)로 받아야지 실행이 가능하다.



