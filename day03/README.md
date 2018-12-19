# DAY03 - 오전

#### **Quiz 1.**

문자열을 입력받아 문자열의 첫 글자와 마지막 글자를 출력하는 프로그램을 작성하시오.

```PYTHON
str = input('문자를 입력하세요: ')
print(str[0]) #첫번째 글자
print(str[-1]) #마지막 글자
```

#### **Quiz 2.**

자연수 N이 주어졌을 때, 1부터 N까지 한 줄에 하나씩 출력하는 프로그램을 작성하시오.

```python
n = int(input('숫자를 입력하세요: ')) 
i = 0
while i < n:
    print(i+1)
    i += 1
```

```python
n = int(input('숫자를 입력하세요: ')) 
for i in range(n):
    print(i+1)
```

### git 활용법

----

1. git status
2. git add .  (. 은 현재폴더를 의미)
3. git commit -m "메세지명"
4. 깃헙 동기화
   * git push (커밋했던 내용을 업로드)



### VSCode 단축키

----

`ctrl+D` 동기화해서 한꺼번에 수정하기

`html:5` : 기본적인 html 구조, 템플릿을 불러와줌.



# HTML & CSS

HTML: Hypertext Markup 언어.  웹페이지를 만드는 컴퓨터 언어

CSS(Cascading Stype Sheets):  마크업 언어(HTML)이 실제 표시되는 방법을 기술하는 언어

HTML이 웹사이트의 몸체를 담당한다면,  CSS는 옷, 엑세서리와 같이 웹사이트를 꾸미는 역할을 담당한다.

* Bootstrap:  트위터를 만든 회사에서 만든 CSS Framework를 제공하는 사이트

  (http://bootstrapk.com/)

* CSS Framework를 활용하면, HTML의 스타일을 직접 하지 않고, 적절한 디자인을 적용할 수 있음.

  (HTML Style을 도와주는 서비스 혹은 라이브러리의 개념

특정 태그들을 골라내는 역할? 선택자? 셀렉터


## 1. HTML의 기본 구성

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
    </body>
</html>
```

## 2. 태그

### 구역 구분 태그

1. `<title> </title>` : 웹브라우져 Tab에 나타나는 HTML문서의 제목 (제목정보 담는 태그)

2. `<p> </p>` : 구문/단락 구분하는 태그

3. `<br>`  : Line breaking;  줄을 나누는 태그. 닫는 태그는 필요 없음. 뒤에 입력 
   * `<ul> </ul>`  + `<li> </li>` 
   * `<ol> </ol>` +  `<li> </li>` 

4. `<div> </div> & <span> </span>`  : 콘텐츠의 영역이나 그룹화를 할 때 사용(내용 블럭 잡기)
   * `div` 는 배경색이 레이아웃 가로 모두에 적용
   * `span`은 다른텍스트와 구별하기 위해 사용. 배경색은 글자가 있는 곳만 적용

###  텍스트 스타일 수정 태그

1. `<b> </b>`  : 텍스트 강조 (Bold)

2. `<i> </i>` : 텍스트 기울임 (Italic)

3. `<u> </u>` : 텍스트 밑줄 (Underline)



## 3. CSS 속성

### CSS 기본 구성

`<head>`   안에서 태그명을 입력하여 CSS를 작성할 수 있음.

(위의 예시는 `<style>` 태그를 사용 / h1,h2,h3 tag의 색깔을 지정)

```html
<!DOCTYPE html>
<html lang="en">
    <head>
		<style>
            h1 {color: red;}
            h2 {color: blue;}
            h3 {color: red;}
            #green {color: green;}
            .yellow {color: yellow;}
        </style>
    </head>
    
    <body>
        <h1 style="color: pink;">이것은 h1 태그입니다.</h1>
        <h2>이것은 h2 태그입니다.</h2>
        <h3>이것은 h3 태그입니다.</h3>
        <h4 id="green"> 이것은 h4 태그입니다.</h4>
        <h5 class="yellow">이것은 h5 태그입니다.</h5>
        <h6 class="yellow">이것은 h6 태그입니다.</h6>
    </body>
```

### 같은 속성을 구분하지 않고, 한꺼번에 수정하기

속성이 같은 경우, 태그명을 ,(콤마) 로 열거하여 한꺼번에 적용가능

```html
        <style>
            h1,h3 {color: red;}
            h2 {color: blue;}
        </style>
```

### id와 class를 활용하여 CSS 적용하기 (CSS의 선택자들)

#id: 전체 문서에서 딱 하나만 입력 가능한, 태그의 고유한 id 값 (태그의 주민등록번호)

.class: 태그가 어떠한 반에 속해 있는지?  공통된 속성을 적용하고 싶을 때 사용

```html
        <style>
            #green {color: green;}
            .yellow {color: yellow;}
        </style>

<h4 id="green"> 이것은 h4 태그입니다.</h4>
<h5 class="yellow">이것은 h5 태그입니다.</h5>
<h6 class="yellow">이것은 h6 태그입니다.</h6>
```

### inline style

해당하는 태그 내에서 직접 입력도 가능

인라인 스타일로 들어간 것이 가장 우선순위 둠.

```html
    <body>
        <h1 style="color: pink;">이것은 h1 태그입니다.</h1>
    </body>
```

CSS 적용 우선순위? inline style > id > class

`ctrl + /`  : 주석 입력하기



# DAY03 - 오후

#### **Quiz 4.** 

표준 입력으로 국어, 영어, 수학, 과학 점수가 입력됩니다.

국어는 90점 이상,

영어는 80점 초과,

수학은 85점 초과, 

과학은 80점 이상일 때 합격이라고 정했습니다.(한 과목이라도 조건에 만족하지 않으면 불합격)

다음 코드를 완성하여 합격이면 True, 불합격이면 False가 출력되도록 작성하시오. 

```python
a = int(input('국어: '))
b = int(input('영어: '))
c = int(input('수학: '))
d = int(input('과학: '))

if a >= 90 and b > 80 and c > 85 and d >= 80:
    print('True')
else:
    print('False')
```

​	 input으로 추출되는 값은 문자열(string) 이므로, 숫자를 입력할때는 int로 다시 감싸줘야한다.

#### **Quiz 5.**

표준 입력으로 물품 가격 여러 개가 문자열 한 줄로 입력되고, 각 가격은 ;(세미콜론)으로 구분되어 있습니다.

입력된 가격을 높은 가격순으로 출력하는 프로그램을 만드세요.

\# 입력 예시: 300000;20000;10000

```python
prices = list(map(int, input('물품 가격을 입력하세요: ').split(';')))
prices.sort(reverse=True)

for i in prices:
    print(i)
```

map(함수, 자료형):  내장함수 map 사용하면, map이라는 또다른 형태의 class(데이터 타입)으로 변경됨. 이 경우는 출력이 불가능함. 따라서 list()로 또다시 묶어줘야함.

```python
prices = input('물품 가격을 입력하시오: ')
prices = prices.split(';')

int_prices =[]
for i in prices:
    int_prices.append(int(i))
    
int_prices.sort(reverse=True)
print(int_prices)
```



# Flask를 활용한 어플리케이션 구축

## 1. Flask 모듈 설치

`pip install flask`  : Flask  모듈 설치

`FLASK_APP=hello.py flask run`  : Flask 모듈 실행

`Ctrl + C` : 플라스크 모듈 종료



## 2. Flask를 활용한 예시

### 1. (주소에) 이름(예. 현수) 입력 후, 반갑습니다 현수님 출력하기

```python
from flask import Flask
app = Flask(__name__)

@app.route("/greeting/<string:name>")
def greeting(name): 
    return f'반갑습니다! {name}님'
```

` <string:name>` : <자료형: 변수이름> 은 대표적인 이름 방식. 

이경우,  string이라는 자료형에 name이라는 변수명을 명명하였다.

`/greeting/<string:name>` : variable routing이라고 함.

`def greeting(name):` ()안에는 변수명 입력

### 2. 숫자(예. 3) 입력 후, 3의 세제곱 값 출력

````PYTHON
from flask import Flask
app = Flask(__name__)

@app.route("/cube/<int:num>")
def cube(num):
    cube = num**3
    return f'{num}의 세제곱은 {cube} 입니다.'
````

formatting을 사용할 경우, 자료형이 기본적으로 문자열(string)으로 변하기때문에,  따로 str()을 사용하지 않아도 괜찮음.

### 3. 사람 수(예. 5) 입력 후, 수 만큼 메뉴를 랜덤으로 출력

````python
from flask import Flask
import random
app = Flask(__name__)

@app.route("/lunch/<int:person>")
def lunch(person):
    menu = ['햄버거','곱창','짜장면','볶음밥','짬뽕','통닭','피자','삼겹살']
    order = random.sample(menu,person)
    return str(order)
````

`import random`  :  외장함수인 `random` 을 `import` 해야함을 유의하자.

Flask에서는 두가지  자료형만 사용 가능(문자열;string & response 객체)

따라서, list 나 숫자와 같은 자료형은 str()으로 type을 변경 해줘야함.

`random.sample(menu, person)`  menu: 리스트, person: 추출하고자 하는 갯 수

### 4. HTML 태그를 활용하여 페이지 출력

```python
from flask import Flask
app = Flask(__name__)

@app.route("/html")
def html():
    multiline_string = '''
        <h1> 이것은 h1 입니다! </h1>
        <p>  여기는 p 입니다 </p>

    '''
    return multiline_string
```

이 경우, python 언어와 html 언어가 뒤섞이고 가독성이 떨어지는 코드임을 알 수 있음.

### 5. render_template을 활용 - Python과 HTML을 각각 분리하여 다른 페이지에서 입력하기

```python
from flask import Flask
app = Flask(__name__)

@app.route("/html_file")
def html_file():
    return render_template('html_file.html')
```

```html
<h1>여기는 h1! h1!</h1>
<p>여기는 p! p!</p>
```

render_template: 메소드.  플라스크가 구현하는 함수 ( import render_template 입력 요)

이후, html 파일을 import하여 별개의 파일을 연동시켜서 작성 할 수 있음.

(html 태그 및 코딩은 html 파일에서 작성하면 됨. 가독성 Up!)

<u>**반드시 폴더명을 templates로 넣어야 작동함을 유의하자**</u>

<u>**(html_file.html은 templates 폴더 안에 넣기)**</u>

### 6. render_template을 활용2 -  HTML 파일을 이용한 Variable routing

```python
from flask import Flask
app = Flask(__name__)

@app.route("/hi/<string:name>")
def hi(name):
    return render_template('hi.html', name_in_html=name)
```

```html
<style>
    h1 {color: red;}
</style>
<h1>만나서 반갑습니다! {{name_in_html}}님 </h1>
```

파이썬 코드를 입력하는 파일이 아니라, render_template 메소드로 연동된 HTML 파일에 입력하여도 Variable routing이 적용 가능하다.

flask에서 지원하는 html파일을 이용하여 name을 입력할때는 중괄호를 두개 써야함.

### 7.  Fake 주소를 활용하여 네이버 검색결과 사이트 열기

```python
from flask import Flask
app = Flask(__name__)

@app.route("/fake_naver")
def fake_naver():
    return render_template('fake_naver.html')
```

```html
<form action="https://search.naver.com/search.naver">
    <input type="text" name="query">
    <input type="submit">
</form>
```

`<form action=" ">` :  `input` 으로 입력되는 데이터를 어디로 요청을 보낼것이냐? 

(입력된 데이터를 전달 버튼 눌렀을 때, 어떤 페이지로 데이터를 전달할지 입력하는 부분)

1. `<form> </form>` : 태그
2. `<action>`  : 태그의 속성 (type은 대표적인 필수 속성)
3. `text` : 속성의 Value(값)
4.  `	submit` : 서버로 데이터를 전송해주라는 속성 값
