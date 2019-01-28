# Django

[TOC]

## Introduction

### 1. What is Django?

Static Web

HTML & CSS 등으로만 구성된 정말 단순한 웹서비스

이문서를 주세요 라고 요청하면, 어떠한 변형, 연산등도 없이,  단순히 문서를 보냄(응답). 서버의 파일이 도서관의 책처럼 적재되어 있고 클라이언트의 요청을 통해서해당 파일을 마치 책을 보는 것처럼 꺼 내 올 수만 있는 웹 서비스.

Dynamic Web(Web Application program):

Static Web과 상반되는 개념. 동적으로파일을 생성하여 뿌려주는 Web.  장고는 Dynamic web이라고 하는 내부적으로 연산도 가능하고, 사용자의 인풋마다 다른 아웃풋을 보여주는 동적웹임. 



![](http://www.cellbiol.com/bioinformatics_web_development/wp-content/uploads/2017/02/static_vs_dynamic_web_pages-1-768x564.png)





웹 앱을 만드는것? 웹 서비스를 만드는 것은  카페를 만드는 것과 매우 유사하다.

카페 창업의 두가지 방법

1) A-Z 모두 직접하기: 홍보 마케팅. 대출 점포인테리어, 레시피개발... 원자재 거래처 확보  매출정산....

2) 프렌차이즈 창업



웹서비스 제작의 두가지 방법

1) URL Parsing, DB setting, ORM, Security, Content Management Template, Caching, Web Server Settting...

2) 웹 프레임 워크 사용

프렌차이즈? 기본적인 레시피나 필요한 재료는 **알아서 제공**해줄게. 넌 그냥 **좋은 카페 만드는데 집중**해!

프레임워크? 기본적인 구조나 필요한 코드들은 **알아서 제공**해줄게. 넌 그냥 **좋은 웹 서비스 만드는데 집중**해!

ex) Express JS, Ruby on Rails, Python django, JAVA Spring, PHP Laravel



**Why Django?**

이미 다 차려놓은것에서 필요한 것만 가져다 쓰면 되기 때문에 편리함.  많은 웹사이트가 웹프레임워크  - 장고를 기반으로 제작이 되어있음,  (인스타그램,  NASA, 모질라, 빗버켓)



### 2. 장고의 동작 원리(구조)

M T V : Model (데이터  관리), Template(사용자가 보는 화면), View(중간 관리자)

1) 사용자가 1번영상을 보겠다고 요청을 보냄 (URL  주소 입력)

2) View(중간관리자)는 받은 요청을 확인하고, Model (데이터 관리)에 1번강의를 찾아달라고 지시를 내림.

3) Model(데이터 관리)은 Database에서 1번 강의를 찾아서 View(중간관리자)에 전달

4) View(중간관리자)는 1번강의를 Template에 전달하여,  HTML 파일과 조합하여 화면을 사용자에게 전달

=> django는 MTV Pattern으로 구조화 되어 있음.

![](https://i.imgur.com/7wc39KX.png)

| 구조     | 데이터 관리 | 사용자가 보는 화면 | 중간 관리자 |
| :------- | ----------- | ------------------ | ----------- |
| Standard | Model       | Template           | View        |
| Django   | Model       | View               | Controller  |



**C9 에 git ignore 설정하기**

https://github.com/github/gitignore/blob/master/Python.gitignore

해당 github의 파일을 raw 로 열어서 최상위 폴더 내에 .gitignore 이라는 이름으로 파일 생성 후 내용 붙임.



## C9에서 django 다루기

### 1. 기본 설정하기

**1) 파이썬 가상환경 생성**

```bash
#intro-venv 라는 가상환경 생성
harrylee0810:~/workspace/django/intro (master) $ pyenv virtualenv 3.6.7 intro-venv

#가상환경으로 만들고자 하는 디렉토리 접속 후 명령어 입력
harrylee0810:~/workspace/django/intro (master) $ pyenv local intro-venv
(intro-venv) harrylee0810:~/workspace/django/intro (master) $ 
```



**2) 장고 설치 및 프로젝트/어플리케이션 생성**

`pip install django` : 장고 설치

`django-admin startproject intro .` : intro 라는 프로젝트를 장고 내에 생성

`python manage.py runserver $IP:$PORT` : 서버실행

```BASH
(intro-venv) harrylee0810:~/workspace/django/intro (master) $ python manage.py runserver $IP:$PORT
Performing system checks...

System check identified no issues (0 silenced).

You have 15 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
Run 'python manage.py migrate' to apply them.

January 24, 2019 - 01:35:48
Django version 2.1.5, using settings 'intro.settings'
Starting development server at http://0.0.0.0:8080/
Quit the server with CONTROL-C.

#서버에 접속하면 아래의 의 에러 창이 뜸 - setting.py 파일에 allowed host에 해당 주소를넣어라!
DisallowedHost at /
Invalid HTTP_HOST header: 'playground-harrylee0810.c9users.io:8080'. You may need to add 'playground-harrylee0810.c9users.io' to ALLOWED_HOSTS.

#Intro 폴더(프로젝트 명) 내 setting.py 내에 해당 주소를 등록 해줘야함.
ALLOWED_HOSTS = ['playground-harrylee0810.c9users.io']

#장고는 디버깅 모드가 기본으로 설정되어 있어서 저장하고 새로고침하면 소스 내용이 자동 적용됨.
```



**2-1) 프로젝트 폴더 내 파일 종류**

| 파일종류     | 내용                                                         |
| ------------ | ------------------------------------------------------------ |
| \__init__.py | Intro 라는 폴더(프로젝트로 지정한 폴더)를 하나의 패키지/모듈로 인식시킴. 이를 통해  intro.urls  intro.settings 와 같은 기능을 사용 할 수 있음. 파이썬 파일을 불러오기 위해서는 \__init\___ 파일이 필요함. |
| setting.py   | 설정들을 넣어놓는 파일                                       |
| urls.py      | 프로젝트에 접근하기 위한 첫번째 문(문지기) 라는 개념임. 어떠한 요청이 장고서버에 오면, 그요청이 도착하는 곳이 urls.py이다.  요청을 urls.py에서 분석해서 어떠한 요청이 왔는지, 어떠한 주소로 왔는지를 보고 다른곳으로 전환하는 중개기(라우터)의 역할을 함. 어떤 주소를 어디로 보내라. 어떤주소가 들어오면 어디로 보내라 등을 모아서 작성함. |
| wsgi.py      | 실제로 서비스를 하기 위해서,  완성을 해서 24시간 돌아가는 서버에다가 코드를 올려놓고 사람들이 access하고 수정을 할 수 있게 하는 파일 |
| manage.py    | 서버를 실행하기 위한 명령어 등을 저장하는 파일               |



**2-2) \__init__.py 파일의 역할**

```python
#manage.py
import os
import sys

if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'intro.settings')
```

intro.settings와 같이 `.` 으로 타고 들어갈 수 있게 해주는 파일이 \_init__.py임.  

특정 폴더 내 파일에 접근하기 위해서는,  \__init__.py라는 파일이 있어야 그 폴더(intro; 프로젝트 명)를 하나의 모듈로 보고, 그 밑으로 들어갈 수 있게됨.

 ex)`intro.settings`  : intro라는 폴더(프로젝트로 지정된 폴더) 내에 settings.py라는 파일을 불러오겠다!



**3) 어플리케이션 생성**

`python manage.py startapp 어플명`:  어플리케이션을 생성하는 명령어



**3-1) 어플리케이션 기본 설정**

어플리케이션을 생성하면,  어플리케이션을 생성했다는 것을 django 에게 알려서 등록을 해야함.  앱의 정보는 apps.py (pages 라는 어플명의 폴더 안에 위치)에 저장되어있으며, 해당 파일 안의 클래스 명인 Pages.Config를  settings.py에 등록해아함.

```python
#apps.py
from django.apps import AppConfig

class PagesConfig(AppConfig):
    name = 'pages'

#settings.py의 33rd line
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    #추가
    'pages.apps.PagesConfig',
]
```



**3-2) 추가 설정**

기본 시간대(time zone)와 기본 언어를 settings.py 파일 내에서 설정할 수 있음. tz의 값은 표준으로 정해진 List of tz database time zones 을 기반으로함 (https://en.wikipedia.org/wiki/List_of_tz_database_time_zones)

```python
#settings.py의 107~109th line
#변경전
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'

#변경후
LANGUAGE_CODE = 'ko-kr'
TIME_ZONE = 'Asia/Seoul'
```



**3-3) 어플리케이션 폴더(예. pages) 내 파일 종류**

| 파일종류     | 내용                                                         |
| ------------ | ------------------------------------------------------------ |
| \__init__.py | 인트로라는 폴더가 하나의 패키지로 인식됨. intro.urls  intro.settings 와 같은 기능을 사용 할 수 있음. 파이썬 파일을 불러오기 위해서는 \__init\___ 파일이 필요함. |
| apps.py      | 만든 어플리케이션의 정보가 담긴 파일                         |
| models.py    | DB 관련된 코드를 작성하는 곳. 어플리케이션(예; pages)에서 사용할 DB를 정의함. 어떠한 데이터베이스 테이블을 만들건지 등을 정의하는 곳. |
| tests.py     | 작성한 코드가 잘 동작하는지? 테스트하는곳.  테스트를 해주는 코드가 또 있음.  코드를 테스트하는 코드 (코드를 테스트하는 코드가 되려 더 많아질수도있음 - 주객전도) |
| views.py     | 어떠한 요청이 들어왔을 때, 무엇을 실행할건지? 우리가 보게될 페이지를 만드는 곳?   페이지들이 모여있는 곳임. |



**4) templates 폴더 생성**

M:models.py

V: views.py (로직이 생성되는 곳)

T: ???

템플릿 관련 폴더를 만들어야함. 어플리케이션 폴더 내 templates 라는폴더를 생성하고. 사용자가 볼 html파일을 해당 폴더 안에 작성하고 저장한다. 



### 2. Django 기본 Process

**1) views.py**

```python
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')
```

어떠한 요청이 들어왔을 때, 무엇을 실행 할 것인지? 기본 로직이 생성 되는 파일임. 플라스크를 사용했던 것과 마찬가지로, 함수를 정의하며, 함수의 파라미터로 request를 받음.

render라는 함수에는 첫번째 인수로  request를 넘겨주고, 어떠한 html 파일을 보여줄건지를 설정함. 접근할 주소는  views.py가 아닌 urls.py에 작성

 return 으로 들어오는 render함수의 첫번째 인수는 위 index 함수의 파라미터와 동일한 변수값임.



**2) urls.py** 

```python
from django.contrib import admin
from django.urls import path
from pages import views

urlpatterns = [
    path('index/', views.index),
    path('admin/', admin.site.urls),
]
```

urlpatterns 라는 리스트안에 주소를 하나하나씩 쌓아 넣음.  첫번째 값에는 실제 주소 값을 입력하며, 두번째 값에는 함수를 넣어줌. 해당 함수는 pages라는 어플리케이션 폴더 내 views.py 파일에 있기 때문에, import를 해야함.

 => `from pages imort views`  입력

**=> from [어플케이션 명] import views**

추가된 내용의 의미는,  `index/` 라는 url을 입력하여 요청을 보내고, 두번째 값에 저장된 함수인 views.index를 통해 views.py 파일 내에 정의된 함수를 실행함. 이 함수를 통해 return 되는 함수 render의 두번째 값인 index 파일을 불러옴. (html 파일은 templates 폴더 내에 저장되어 있을 것임.)

=> index 주소를 호출하면 views 파일 내 index 함수를 실행함. render를 통해 html 화면을 반환해 보여줌.



**3) templates 폴더 / index. html**

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
    <h1>Index입니다!</h1>
</body>
</html>
```



**최종 정리**

- views.py에서 함수를 정의하고 해당 함수가 실행될 때 return 되는 함수(render)를 통해 html파일을 연결시킴.
- url.py에서는 url의 pattern을 정의함. 사용자가 특정 url을 요청하면(호출 하면), views.py 내에 어떠한 함수를 실행할건지? 패턴 정의
- url.py에서 정의된 패턴에 따라, 연결된 함수를  views.py로부터 불러오고,  render되는  html파일을 return함.
- render 된 html 파일을 열어서 사용자에게 보여줌.



views.py에서 함수 정의 =>  url.py에서 url 패턴 정의 =>  패턴에 따라 연결된 views.py 내 함수  실행 =>  Render 된 html파일을 열어 사용자에게 보여줌.



### 3. 템플릿 변수

템플릿으로 변수를 넘길 수 있음. 저녁 메뉴를 random으로 뽑혀서 보여주는 페이지를 생성해보자.



**1) view.py**

```python
from django.shortcuts import render
import random

def dinner(request):
    menu = ["족발","햄버거","치킨","초밥"]
    pick = random.choice(menu)
    return render(request, 'dinner.html', {'dinner': pick})    
```

random을 쓰기 위해 파이썬의 외장함수인 random을 import 해야 함.  

random.choice의 결과 값을 pick이라는 변수에 저장하고, 해당 변수를 render의 3번째 인자로 넘겨줌. 

플라스크는 단순히 키워드 변수로 넘겼으나, 장고는 딕셔너리의 형태로 넘겨야함.  

- 딕셔너리의 Key: html 파일과 연동 시킬 변수명
- 딕셔너리의 value: random.choice의 결과를 나타내는 변수 pick



**2) urls.py** 

```python
from django.contrib import admin
from django.urls import path
from pages import views

urlpatterns = [
    path('dinner/', views.dinner),
    path('admin/', admin.site.urls),
]
```

페이지를 접근하는 주소를 urls.py에 생성.  

"기본주소/dinner" 이라는 url 주소를 사용자가 호출(요청;request)하면 views 폴더 내 dinner 함수가 실행됨.



**3) dinner.html**

```html
<body>
    <h1>오늘 저녁은 {{dinner}}</h1>
</body>
<-- 변수는 반드시 이중 중괄호로 감싸 줄 것! 변수는 {{key}}의 형태임 -->
```

```python
#views.py
	return render(request, 'dinner.html', {'dinner': pick})    
```

return 되는 render 함수에 따라, dinner.html 파일을 request  함.

딕셔너리의 key 값을 변수로 html 템플릿에서 사용함. 

사용자는 “기본주소/dinner” 이라는 url을 입력하면, django의 process에 따라 dinner.html의 화면을 보게 되며, dinner 이라는 변수(render 함수의 3번째 인자; 딕셔너리의 key값)의 value값이 출력된다.

**여기서, 템플릿으로 변수 값을 넘겨주는 것을 템플릿 변수 라고 한다.**



### 4. Variable routing

주소자체를 변수로 사용하는것을 의미함. 주소로 부터 받고 싶은 변수의 이름을 파라미터(인자)로 정의해야함.    변수에 따라 다른 페이지 화면을 보여줌.



**1) view.py**

```python
def hello(request, name):
    return render(request, 'hello.html', {'name': name})
```

템플릿 변수와 유사한 형태임. render의 3번째 인자로 html으로 넘겨줄 변수를 지정함. (딕셔너리 형태)

여기서 혼동하지 않고 잘 봐야하는 부분은, `{'name' : name}` 이다. 딕셔너리의 key는 html 파일과 연결해서 사용할 변수 명이며, value는 실제 주소창에 입력되는 `hello/<str:name>` 의 name이다 (hello함수의 2번째 인자)

**render 함수의 3번째 인자: { key : value}**

- key: html파일과 연동되어 html 파일에서 사용할 변수명. 이를 통해 html 파일에서 value값을 갖고 옴.
- value: 실제 주소창에 입력되는 url 뒷 부분. (이번 예제에서는 `hello/<str:name>` 의 name에 해당함). 이는 또한, hello 함수의 2번째 인자임.



**2) urls.py**

```python
urlpatterns = [
    path('hello/<str:name>/', views.hello),
    path('admin/', admin.site.urls),
]
```

페이지를 접근하는 주소를 urls.py에 생성.   “기본주소/hello/현수” 와 같은 예시처럼, 사용자가 url 주소를 호출하면 views.py 내 hello 라는 함수를 실행 시킴. 여기서 현수 라는 문자열 (`<str:name>` 에 해당되는)이  views.py 의 hello 함수의 변수(name) 로 할당됨.

-  `<str:name>` 은 자료의 형태를 string(문자열)으로 제한한다는 의미임. 
-  `hello/<str:name>`  ==  `def hello(request, name)` 

hello 함수의 변수로 할당되며, 이것이 render 함수의 템플릿 변수로 넘어가 hello.html 에서 사용할 수 있게 됨.



**3) hello.html**

```html
<body>
    <h1>안녕, {{name}}!</h1>
</body>
```



### 5. django 내 정보 주고 받기

Throw와 Catch라는 함수를 통해 django 내에서 정보를 주고 받는 process를 살펴 보자



**1-1) view.py**

```python
def throw(request):
    return render(request,'throw.html')
```

input 을 보낼 페이지에 연결하는 함수 throw를 view.py에 작성함.



**1-2) urls.py**

```python
urlpatterns = [
    path('throw/',views.throw),
]
```

사용자가 "기본주소/throw" 라는 주소를 호출하면 views.py 내 throw 라는 함수를 실행시키는 url 패턴을 작성



**1-3) throw.html**

```html
<body>
    <form action="/catch", method="get">
        <input type="text" name="message"/>
        <input type="submit" value="Submit"/>
    </form>
</body>
```

플라스크에서 작성했던 "요청을 보낼 HTML 생성"과 동일한 HTML 구성을 띔.  데이터를 넘겨주기 위해 (요청을 보내기 위해), form 태그를 사용함.  (넘겨줄  url 주소를 form 태그의 action 속성의 값으로 입력)

input 태그 내에 작성된 내용이 message 라는 변수에 저장됨.  딕셔너리의 형태를 띔. 

**예) {"message" : "input 내용"}**

추후, 응답을 받을 html 파일에 대해 view.py에 내용 작성 시, 해당 변수가 사용됨. method는 GET 방식이 사용됨.



> 요청을 보내기 위해 send.html 이라 지정한 파일 내에 form 과 input 태그를 사용한다.
>
> `input` : 사용자로부터 입력을 받을 수 있는 내용을 작성하는 태그.  `input` 은  입력만 받고, 화면을 보여주는 역할만 가능하므로 `form` 태그를 추가로 사용해야 함. (대표적인 속성: `name`)
>
> - `name` : `input` 태그 내에 작성된 내용(메세지) 의 이름을 지어줌. 플라스크는 input의 내용을 딕셔너리의 형태로 가공하여, `form`  태그를 통해 전달함. 따라서, `name` 속성으로 지정된 내용이 딕셔너리의 key가 되며, `input` 태그를 통해 작성되는 내용이 딕셔너리의 value가 됨.
>
> `form` : `input` 으로 작성된 내용을 보내는데 사용하는 태그 (대표적인 속성: `action` , `method`)
>
> - action: 폼태그에서 어디로 보낼지를 설정하는 속성
> - method: 어떠한 방식으로 보낼 것인가? (POST / GET 방식)



**2-1) view.py**

```PYTHON
def throw(request):
    return render(request,'throw.html')

def catch(request):
    message = request.GET.get('message')
    return render(request, 'catch.html', {'message': message})
```

1-3) throw.html에 따라, input으로 들어가는 내용이 message라는 변수에 저장되고, 우리는 catch라는 함수를 view.py에 작성하여 그 내용을 갖고올 예정임.

- request: 정보/데이터를 요청함.

- GET: throw.html - form 태그 - method 속성의  "get"을 의미함 (어떠한 방식으로 요청을 보낼건지?)

- get('message') : dict의  value값을 갖고오는 메서드.  message로 정의된 이름 속성의 내용(value)를 갖고옴.  <u>여기서 value는 throw.html에서 사용자가 입력하는 input 내용임!</u>  

  ```python
          <input type="text" name="message"/>
  ```

*=> Get 방식으로 응답/요청을 주고 받는 throw.html에서 사용자가 입력한 내용을 받아, message라는 변수에 저장한다는 의미*

최종적으로 render 함수의 템플릿 변수(html과 연동할 변수)를 'message'라 정의하고,  딕셔너리의 key 값으로 윗 줄에서 정의한 message를 넣는다. (템플릿 변수는 항상 Dict의 형태임을 잊지말자!)



**2-2) urls.py**

```python
urlpatterns = [
    path('catch/',views.catch),
]
```

url 패턴을 정의하는 부분. 반복되는 내용이므로 자세한 설명은 생략한다.



**2-3) catch.html**

```html
<body>
    <h1>Catch! {{message}}</h1>
</body>
```

views.py에서 넘긴 템플릿 변수를 catch.html에 입력한다. `{{ 변수명}}` 의 형태를 띄는 것을 다시한번 주의하자.

템플릿 변수 message 의 결과값으로 throw.html에서 사용자가 입력한 input 내용이 들어온다.



### 6. 외부 웹으로 요청 주고 받기

내부에 요청을 보내고 응답하는것이 아니라, django 외부에 요청을 보내는 것을 해보자.



**1) views.py**

```python
def naver(request):
    return render(request, 'naver.html')
```

naver 함수 정의. 요청(request)가 들어오면 render 함수를 통해 naver.html 파일을 호출한다.



**2) urls.py**

```python
urlpatterns = [
    path('naver/',views.naver),
]
```

'naver/' 주소가 들어오면 views.py 내 naver 함수를 호출함.



**3) naver.html**

```python
<body>
    <form action="https://search.naver.com/search.naver", method="get">
        <input type="text" name="query"/>
        <input type="submit" value="Submit"/>
    </form>
</body>
```

네이버에서 어떤 단어를 검색하면 주소창은 아래의 구조를 띄는데, 내부에서 요청을 보내고 응답을 했을 때와 매우 유사한 형태를 띄고 있는 것을 알 수 있다.

> ```python
> #네이버 검색 결과 url
> https://search.naver.com/search.naver?query=python
> #내부 요청 응답 결과 url    
> http://playground-harrylee0810.c9users.io:8080/catch/?message=안녕
> ```



내부에서 요청을 보내고 응답할 때는 `<form action=""/catch">` 처럼  form 태그의 action 속성에 기본주소 + 넘길 주소 url을 입력하면 되었으나,  외부을 보낼 때에는 전체 주소를 넣어야 한다.  따라서, 이번에는 네이버 결과 주소창의 기본 구조에 따라 `https://search.naver.com/search.naver` 를  action 속성에 입력한다.

input 태그의 name 속성에는 네이버에서 요구하는 이름인 `query`를 입력하자.  치종적으로,  사용자가 naver.html에  내용을 입력하면, `https://search.naver.com/search.naver?query=입력내용` 이 넘겨지게되고, naver.html은 fake naver 와 같은 기능을 하게 된다.



### 7. Bootstrap 사용

CSS Framework인 Bootstrap을 사용하는 데 특별한 부분은 전혀 없다. 동일한 process를 적용하자.

```python
#views.py
def bootstrap(request):
    return render(request, 'bootstrap.html')

#urls.py
urlpatterns = [
    path('bootstrap/', views.bootstrap),
```

```html
<--bootstrap.html -->
 <head>
<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.2.1/css/bootstrap.min.css" integrity="sha384-GJzZqFGwb1QTTN6wy59ffF1BuGJpLSa9DkKMp0DgiMDm4iYMj70gZWKYbI706tWS" crossorigin="anonymous">
</head>
<body>
    <h1>Bootstrap!</h1>
    
    <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.6/umd/popper.min.js" integrity="sha384-wHAiFfRlMFy6i5SRaxvfOCifBUQy1xHdJ/yoi7FRNXMRBu5WHdZYu1hA6ZOblgut" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.2.1/js/bootstrap.min.js" integrity="sha384-B0UglyR+jN6CkvvICOB2joaf5I4l3gm9GU6Hc1og6Ls7i6U/mkkaduKaBhlAXv9k" crossorigin="anonymous"></script>
</body>
```





## Appendix A : 명령어 정리

| 명령어                                     | 정의              |
| ------------------------------------------ | ----------------- |
| pyenv virtualenv 3.6.7 [가상환경 명]       | 가상환경 생성     |
| pyenv local [가상환경 명]                  | 가상환경으로 설정 |
| pip install django                         | 장고 설치         |
| django-admin startproject [프로젝트이름] . | 프로젝트 생성     |
| python manage.py startapp [앱이름]         | 어플리케이션 생성 |
| python manage.py runserver $IP:$PORT       | 서버 실행         |

 


