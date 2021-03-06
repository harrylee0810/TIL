# C9 & Flask

## 190121 

### Introduction

Flask: 파이썬 기반의 마이크로 프레임 워크.  Web을 구현할 때 사용 하는 도구(http://flask.pocoo.org/)

Cloud9: 클라우드 기반의 통합 개발 환경(IDE)으로 서버를 빌려올 수 있음. (https://ide.c9.io/)



#### 파이썬 설치하기

**pyenv.sh 설치**

```BASH
git clone https://github.com/pyenv/pyenv.git ~/.pyenv
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
echo -e 'if command -v pyenv 1>/dev/null 2>&1; then\n  eval "$(pyenv init -)"\nfi' >> ~/.bashrc
exec "$SHELL"

git clone https://github.com/pyenv/pyenv-virtualenv.git $(pyenv root)/plugins/pyenv-virtualenv
echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.bashrc
exec "$SHELL"
```

- `pyenv install 3.6.7` : 파이썬 3.6.7 버젼 설치
- `pyenv global 3.6.7` : 설치된 파이썬을 전역(global)으로 쓰겠다!
- `python -V` : 파이썬 버젼 확인 (3.6.7이 나오면 정상적으로 작동된 것으로  확인 가능)



**가상환경 pyenv 설치**

- `pip install` 명령은 컴퓨터에 전역으로 설치하게 한다. 프로젝트마다 파이썬의 버젼, 라이브러리 버전을 나누어 사용하기 위해서는 독립적인 가상환경(venv)안에서 버젼을 설치해야 한다.

- `pyenv virtualenv 3.6.7 first-venv`  : 해당 가상환경을 `first-venv` 이라 명명한다,.

- 가상환경으로 사용하려는  폴더 내부에서 `pyenv local first-venv` 를 입력하면, 해당 폴더가 가상환경으로 지정되었음을 알 수 있다.
- `pip install -U pip` : pip 버젼을 upgrade(U) 하겠다는 명령어. 가상환경이 지정 안된 다른 디렉토리에  `pip --version` 을 입력해보면, 가상환경의 밖과 안에 다른 버전이 존재하는 것을 알 수 있음
- 프로젝트 별로, 서로 다른 라이브러리 버젼으로 인한 충돌을 막기 위해 가상환경을 주로 사용한다.
- `pip freeze` : 플라스크 등 외장 라이브러리의 버젼 정보를 확인 하는 명령어. 외부에서는 아무것도 설치되지 않는 상황이므로 해당 명령어를 실행하려해도 아무것도 뜨지 않음.

```bash
(first-venv) harrylee0810:~/workspace/mysite $ pip freeze
Click==7.0
Flask==1.0.2
itsdangerous==1.1.0
Jinja2==2.10
MarkupSafe==1.1.0
Werkzeug==0.14.1
```



#### Flask 설치하기

시작은 Flask를 기본적으로 설치했던 아래의 방법과 동일하다.  local에서는 Flask 자체가 Host였기 때문에, `FLASK_APP=app.py flask run` 로 웹서버를 실행하였으나, 이번에는 C9의 서버를 이용하기 때문에, C9에서 해당 컴퓨터에 접근하기 위해 Host와 Port를 입력해줘야 한다. 

`FLASK_APP=app.py flask run --host=$IP --port=$PORT`

(가상환경으로 지정한 디렉토리 내에 app.py 파일도 생성해주도록 하자)

> #### Flask is Fun
>
> 아래의 코드를 파이썬에 입력.
>
> (Flask 작동시, 구현되는 기본 페이지(Hello world)를 만드는 코드)
>
> ```python
> from flask import Flask
> app = Flask(__name__)
> 
> @app.route("/")
> def hello():
>     return "Hello World!"
> ```
>
> `pip install Flask` : Flask를 설치하는 명령어 



매번, 해당 명령어를 입력하는 번거로움을 줄이기 위해, 아래의 코드를 추가로 입력하도록 하자.

```python
# app.py
from flask import Flask
import os
app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello World'
    
# 밑의 구문은 항상 아래에 와야한다.
# 이 구문 밑은 실행이 안된다.
if __name__ == '__main__':
    app.run(host=os.getenv('IP'), port=os.getenv('PORT'), debug=True)
```

- 외장함수 os의 env 변수로 IP와 Port를 넘겨주고,  수정된 내용을 즉각적으로 반영하기 위해 `Debug=True`를 추가로 입력해주었음.
- `python app.py` 을 입력하면 flask를 바로 작동 시킬 수 있다.



https://flask-docs-kr.readthedocs.io/ko/latest/quickstart.html#id6

### Variable Routing

현대 웹 어플리케이션은 잘 구조화된 URL로 구성되있다. 이것으로 사람들은 URL을 쉽게 기억할 수 있고, 열악한 네트워크 연결 상황하의 기기들에서 동작하는 어플리케이션에서도 사용하기 좋다. 사용자가 인덱스 페이지를 거치지 않고 바로 원하는 페이지로 접근할 수 있다면, 사용자는 그 페이지를 좋아할 것이고 다시 방문할 가능성이 커진다.

`route()` 데코레이터는 함수와 URL을 연결해준다. 아래는 기본적인 예제들이다.

```python
@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello')
def hello():
    return 'Hello world'
```

하지만, 여기엔 더 많은것이 있다. 여러분은 URL을 동적으로 구성할 수 있고, 함수에 여러 룰을 덧붙일수있다.



#### 변수 규칙

URL의 변수 부분을 추가하기위해 여러분은 `<variable_name>`으로 URL에 특별한 영역으로 표시해야된다. 그 부분은 함수의 키워드 인수로써 넘어간다.  선택적으로, `<converter:variable_name> `으로 규칙을 표시하여 변환기를 추가할 수 있다.



```python
@app.route('/greeting/<string:name>') 
def greeting(name):
    return f'반갑습니다 ! {name}님!'

#http://flask-harrylee0810.c9users.io:8080/greeting/현수
```

- `@app.route('/greeting/<string:name>') ` 의 `name` 은 `variable routing` (변경 될 수 있는 주소; 변수)

- `name`  앞에 `string:`  (예: `<string: name>` ) 을 입력하여, 변수의 자료형에 문자열만 가능하게 지정함.

  예) `<string:name>`  / `<int:name>`  / `<float:name>` / `<path:name>`

| def   | definition                                |
| ----- | ----------------------------------------- |
| int   | accepts integers                          |
| float | like int but for floating point values    |
| path  | like the default but also accepts slashes |

- `def greeting(name):` 변수명(name)을 파라미터(괄호 안 내용)로 받아야만 실행이 가능함



```python
@app.route('/cube/<int:num>')
def cube(num):
    result = num**3
    return str(result)

#http://http://playground-harrylee0810.c9users.io:8080//cube/3
#=> 27
```

- return은 string type만 와야하기 때문에 다른 자료형(int 등)은 str로 변환해줘야 한다.



#### Render_template을 이용한 html 파일 열기

파이썬 소스코드에서 HTML을 생성하는 것은 그다지 재밌는 일은 아니다.(굉장히 번거로운 일이다) 왜냐하면 어플리케이션 보안을 위해 동적으로 변환되는 값에 대해 이스케이핑을 여러분 스스로 작성해야한다. 그런 불편함때문에 Flask는 <<http://jinja.pocoo.org/2/>>`를 템플릿엔진으로 구성하여 자동으로 HTML 이스케이핑을 한다.

템플릿을 뿌려주기 위해, 어려분은 [`render_template()`](https://flask-docs-kr.readthedocs.io/ko/latest/ko/api.html#flask.render_template) 메소드를 사용할 수 있다. 여러분이 해야하는 것은 단지 템플릿의 이름과 템플릿에 보여줄 변수를 키워드 인자로 넘겨주면 된다. 아래는 템플릿을 뿌려주는 방식의 간단한 예를 보여준다.

> 클라이언트의 요청을 받아 어떤 처리를 한 이후 서버에서 클라이언트에게 응답을 보낸다고 했다. 이때 응답은 HTML(Hyper Text Markup Language)로 보내진다. 클라이언트가 사용하고 있는 크롬이나 인터넷익스플로어와 같은 브라우저는 이 HTML을 정해진 방식으로 분석하여 지금 보는것과 같은 알맞은 화면을 생성해낸다. 이 과정을 rendering 과정이라고 한다.
>
> flask 에는 rendering 과정을 매우 쉬운 방법으로 구현할 수 있는 메서드를 제공한다.
>
> **[출처]** [[플라스크 이용하여 웹 제작해보기\] - 7. render_template 과 post방식의 로그인](https://blog.naver.com/iamsupermazinga/221364616504)|**작성자** [화수르](https://blog.naver.com/iamsupermazinga)



**html 파일은 반드시 `templates`  라는 폴더명 안에 넣어야 한다.**

예제1)

```python
from flask import render_template

@app.route('/html_file')
def html_file():
    return render_template('html_file.html')
```

```html
<!DOCTYPE html>
<!-- html_file.html -->
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>
<body>
    <h1>This is HTML file.</h1>
</body>
</html>
```

예제2)

```python
@app.route('/hi/<name>')
def hi(name):
    return render_template('hi.html', name_in_html=name)
```

```html
<!DOCTYPE html>
<!-- hi.html -->
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>
<body>
    <h1>Hi! {{ name_in_html }}</h1>
</body>
</html>
```

url 이후의 변수 `name` 을 `name_in_html` 이라는 다른 변수로 연결하여,  `name_in_html` 을 html 파일에 변수로 다시 넘겼다. 

`Flask - render_template`  메서드를 사용할 경우, 변수는 반드시 이중 중괄호 안에 넣어 줘야한다.  

예) `{{ name_in_html }}`



#### jinja templates 

jinja templates를 이용하면 반복문 등을 실행 할 수 있다.

```python
@app.route('/fruits')
def fruits():
    fruits = ['qpple', 'banan', 'mango', 'melon']
    return render_template('fruits.html', fruits=fruits)
```

```html
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>
<body>
    {% for f in fruits %}
    <li> {{ f }} </li>
    {% endfor %}
</body>
</html>
```
- `{% for f in fruits %}`: 중괄호 안에 앞뒤로 %를 써주면 안에 있는 내용이 출력이 안되고, jinja 템플릿이 적용됨

- `{{ fruits }}` 로 쓴다면 글자 그대로 출력이 됨
- list로 for 문을 순회하는 요소값 f 출력
- `{% endfor %}` : for 문 끝!



## 190122

#### 파일 조작1 : 요청을 보낼 HTML 파일 생성

```python
@app.route('/send')
def send():
    
    return render_template('send.html')
```

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>
<body>
    <form action="/receive" method="get">
        <input type="text" name="who"/>
        <input type="text" name="message"/>
        <input type="submit" value="submit"/>
    </form>
</body>
</html>
```

요청을 보내기 위해 send.html 이라 지정한 파일 내에 form 과 input 태그를 사용한다.

`input` : 사용자로부터 입력을 받을 수 있는 내용을 작성하는 태그.  `input` 은  입력만 받고, 화면을 보여주는 역할만 가능하므로 `form` 태그를 추가로 사용해야 함. (대표적인 속성: `name`)

-  `name` : `input` 태그 내에 작성된 내용(메세지) 의 이름을 지어줌. 플라스크는 input의 내용을 딕셔너리의 형태로 가공하여, `form`  태그를 통해 전달함. 따라서, `name` 속성으로 지정된 내용이 딕셔너리의 key가 되며, `input` 태그를 통해 작성되는 내용이 딕셔너리의 value가 됨.

`form` : `input` 으로 작성된 내용을 보내는데 사용하는 태그 (대표적인 속성: `action` , `method`)

- action: 폼태그에서 어디로 보낼지를 설정하는 속성
- method: 어떠한 방식으로 보낼 것인가? (POST / GET 방식)



`http://playground-harrylee0810.c9users.io:8080/receive?who=MJ+&message=gobowling%3F`



#### **파일 조작 2-1: 응답을 받을 HTML 파일 생성**

send.html 에서 입력된 내용이 담길 receive.html 생성 및 내용 설정을 해보도록 하자.

```python
from flask import Flask, render_template, request

@app.route('/receive')
def receive():
    name = request.args.get('who') # request.args['name']
    message = request.args.get('message')
    
    return render_template('receive.html', name_in_html=name, message_in_html=message)
```

URL로 넘겨진 파라메터 (`?who=MJ` 소위 말하는 질의 문자열)에 접근하려면, `args` 속성을 사용 할 수 있음.

`request.args` 는 딕셔너리의 형태로 자료를 요청하므로,  `request.args.get[]`  혹은 `request.args[]` 을 사용 할 수 있음. request라는 외장 라이브러리를 사용하기 위해 import 하는 것을 잊지 말자.

ex) requests.gets

​	{‘who’: ‘민재님’. ‘message’: ‘볼링 치러가실래요?’}

```python
    name = request.args.get('who')
    message = request.args.get('message')
```

위의 코드에서 get 이하의  `who` 와 `message` 는 send.html > input > name 속성에서 지정한 변수명(key)이다. `requests.args.get(‘who’)` 를 통해 ‘민재님’ 이라는 value값을 불러오도록 요청(request)하고, 그 값을 name이라는 변수에 저장하였음. 마찬가지로, ‘볼링 치러 가실래요?’ 라는 value값을 message 라는 변수에 저장함.

> ```python
> <body>
>     <form action="/receive" method="get">
>         <input type="text" name="who"/>
>         <input type="text" name="message"/>
>         <input type="submit" value="submit"/>
>     </form>
> </body>
> ```



```python
    return render_template('receive.html', name_in_html=name, message_in_html=message)
```

HTML 문서 작성을 위해 render_template 메서드를 사용하고, 위의 코드를 입력한다. 이때, `name` 과 `meesage` 라는 변수명에는 상위 코드에서 입력한  ‘민재님‘ 과  ‘볼링치러 가실래요?’가 저장되어있고, 그 값을 다시, html에서 불러올 수 있도록  ` name_in_html`  과 `message_in_html` 이라는 변수로 다시 저장한다.

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>
<body>
    <h1>from {{name_in_html}}:</h1>
    <p>{{ message_in_html }}</p>
</body>
</html>
```

{{ }}를 사용하여  `name_in_html`  과 `message_in_html` 라는 변수를 갖고옴.



#### 파일 조작 2-2: 내용 저장하기

지금까지, 클라이언트(웹 사용자)가 요청을 처리하고(input을 통해 내용 입력), 적절한 응답을 보내는것(입력된 내용을 화면에 출력)까지 구성해보았다. 여기까지의 과정은 내용을 입력하고 화면에 출력하는 것에 불과하며, 입력된 내용이 어디에도 저장되지 않는다. 입력된 내용을 저장하는 방법에 대해 살펴보자.

요청을 받아서, 응답을 보내줄 때가 내용을 저장하기 위한 가장 적절한 타이밍이다.  저장할 파일을 만들기 위해 guestbook.csv라는 파일을 디렉토리 내에 생성하고, who와 message라는필드명을 지정해보자. (반드시 Enter를 쳐서, line2로 넘어가고, 필드명은 붙여서 써야함.)

ex) 1. who, message (O)  

​      2. who, message (X) <=== 필드명 사이에 공백이 존재

```python
import os, csv

@app.route('/receive')
def receive():
    name = request.args.get('who')
    message = request.args.get('message')
    
    with open('guestbook.csv','a', encoding='utf8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['who','message'])
        writer.writerow({
            'who': name,
            'message':message
        })

return render_template('receive.html', name_in_html=name, message_in_html=message)
```

외장 라이브러리인 `csv`를 import 하고,  파일을 조작하기 위해 `with open() as 변수명`  함수를 사용한다. 새로운 내용을 덮어쓰는 것이 아니라, 미리 설정한 필드명(who, message)를 기반으로 내용을 추가해야하므로, `open` 함수의 속성으로 `w` 가 아니라 `a(append)` 를 사용한다.

writerow라는 메서드에 파라미터(인자)를 넘겨주는데, 이 인자가 딕셔너리가되어야함. 따라서 () 안에 {}으로 정리가 필요함(필드명 `who`의 value값으로  `name = request.args.get('who')` 을 갖고오고, 필드명 `message`의 value값으로 `message = request.args.get('message')` 를 갖고옴)



#### 파일 조작 3: 저장된 페이지 보기

내용을 입력하고 저장하는데,  내용이 저장된 페이지를 보는 곳이 없음? 또만들어보자!

=> `DictReader` 메서드를 통해  CSV 파일을 읽어와야함. (따라서, `open` 함수의 `r` 속성 사용).  한줄씩 읽어와야하므로, 반복을 돌리고, 각 줄에 있는 내용을 result라는 리스트에 append함. 이를 통해, result라는 변수에는 파일에는 csv 파일의 내용들이 각각 불러와져서 저장될 것임.(딕셔너리로, who와 message라는 키와 value로)

마지막으로, render_template를 이용해서 result_in_html = result 으로 넘겨서 html파일에서 볼수 있게 해야함.

```PYTHON
@app.route('/guestbook')
def guestbook():
    result = []
    with open('guestbook.csv','r', encoding='utf8', newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            result.append(row)
        
    return render_template('guestbook.html', result_in_html = result)
```



```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>
<body>
    <h1>여기는 방명록 페이지 입니다. </h1>
    <ul>
        {% for m in result_in_html %}
            <li>{{m.name}} - {{m.message}} </li>
        {% endfor %}
    </ul>
    
</body>
</html>
```

jinja templates 을 이용하여 csv파일의 내용이 담긴 리스트의 내용을 하나씩 불러오는 반복문을 사용한다.

m은 리스트안에 저장된 각각의 딕셔너리를 의미함. 예) {‘who’: ‘민재님, ‘message’ : ‘볼링치러 가실래요?’}

플라스크에서는 `m.name`  과 `m.message` 라는 기능을 통해 value값에 바로 접근을 할 수 있다.

(`m.name` 의 `name` 과 `m.message`의 `message` 는 아래의 내용을 의미함;딕셔너리의 value에 대한 변수) 

```python
name = request.args.get('who')
message = request.args.get('message')
```


지금까지, C9에서 제공하는 웹서버를 기반으로, 파이썬 기반의 웹프레임워크인 플라스크를 활용하여, 요청과 응답을 보내고,  파일을 조작하는 것까지 살펴보았다. 

그런데 만약, 홍길동이라는 데이터를 만날 경우, 이 데이터는 제외하고 guestbook.html이라는 웹페이지에 화면이 출력하게 하고 싶은경우, 추가적인 조건문과 open함수 등을 사용해야하므로 코드가 복잡해지고, 가독성이 떨어질 것이다. 따라서, 우리는 **데이터베이스** 라는 것을 활용해야 하는 결론에 최종적으로 도달하게된다.