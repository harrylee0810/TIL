# 190128

장고에서 데이터 베이스 다루기



Django: 모델 이라는 파이썬 객체를 통해 데이터 접속 & 관리

모델: 저장된 데이터의 구조(Schema)를 정의 ex) 필드 타입, 데이터

의 최대 크기, 기본값 등



모델은 장고 웹 어플리케이션의 `models.py` 파일에서 정의됨. 이들은 `django.db.models.Model` 를 상속받은 서브(파생) 클래스로 구현되며,  필드, 메서드, 메타데이터등을 포함 할 수 있음.



```python
from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
```



**필드(Fields)**

데이터 베이스 테이블의 열을 나타내는 추상 클래스임.  모델 클래스의 각 속성은 테이블의 필드에 해당함. 각각의필드는 DB 목록(table)에 저장하길 원하는 데이터열을 나타냄. 

```python
title = models.CharField(max_length=100)
content = models.TextField()
```

위의 예제는 `title` 이라는 하나의 필드를 갖고 있으며, `models.CharField`  필드타입임. 즉, 이 필드가 작은 문자열을 포함하고 있다는 뜻임. 

필드 타입은 특정한 클래스를 사용하여 등록되며, HTML 양식(즉, 유효값을 구성하는)에서 값을 수신할 때, 사용할 유효성 검증 기준과 함께 데이터베이스에서 데이터를 저장하는 데 사용되는 레코드의 타입을 결정함. 

필드타입은 또한 필드가 어떻게 저장되고, 사용될지 지정하는 인수를 사용할 수 있음.

- `max_length=100` : 이 필드에서 값의 최대 길이는 100자라는 것을 알림.



**Migrations**

Django에서 Model 클래스를 생성하고 난 후, 해당 모델에 상응하는 테이블을 데이터베이스에서 생성할 수 있음. Python 모델 클래스의 수정 (및 생성)을 DB에 적용하는 과정을 Migration이라고 함.

 => 모델의 변경 내역을 DB Schema(데이터베이스 데이터 구조)로 반영시키는 효율적인 방법을 제공

- `python manage.py makemigrations` : 마이그레이션 파일(초안) 생성
- `python manage.py migrate` : 해당 마이그레이션 파일을 실제 데이터 베이스에 반영(적용)



**필드 타입**

| Field Type    | 설명                                                         |
| ------------- | ------------------------------------------------------------ |
| CharField     | 제한된 문자열 필드 타입. 최대 길이를 max_length 옵션에 지정해야 한다. 문자열의 특별한 용도에 따라 CharField의 파생클래스로서, 이메일 주소를 체크를 하는 EmailField, IP 주소를 체크를 하는 GenericIPAddressField, 콤마로 정수를 분리한 CommaSeparatedIntegerField, 특정 폴더의 파일 패스를 표현하는 FilePathField, URL을 표현하는 URLField 등이 있다. |
| TextField     | 대용량 문자열을 갖는 필드                                    |
| IntegerField  | 32 비트 정수형 필드. 정수 사이즈에 따라 BigIntegerField, SmallIntegerField 을 사용할 수도 있다. |
| BooleanField  | true/false 필드. Null 을 허용하기 위해서는 NullBooleanField를 사용한다. |
| DateTimeField | 날짜와 시간을 갖는 필드. 날짜만 가질 경우는 DateField, 시간만 가질 경우는 TimeField를 사용한다. |
| DecimalField  | 소숫점을 갖는 decimal 필드                                   |
| BinaryField   | 바이너리 데이타를 저장하는 필드                              |
| FileField     | 파일 업로드 필드                                             |
| ImageField    | FileField의 파생클래스로서 이미지 파일인지 체크한다.         |
| UUIDField     | GUID (UUID)를 저장하는 필드                                  |



## CRUD

`python manage.py shell` : 장고 전용 파이썬 쉘 
(Django 에서 동작하는 모든 명령을 대화식 Python 쉘에서 사용 할  수 있게 함)

`from [어플리케이션명].models import [클래스명]` :  파이썬 쉘 내 사용을 위한 클래스 호출



**Create**

```python
>>> post = Post(title='몇번째?', content='인가요?')
>>> post
Post: Post object (None)>
>>> post.save()
>>> post.title
'몇번째?'
>>> post.content
'인가요?'
```

post라는 Post의 인스턴스를 생성. 이는 post 라는 변수임.


`post.title`  또는 `post.content` 로 접근하면, 파이썬 내에서만 인스턴스의 변수를 호출하는 것임. 따라서, ` post.save()` 를 써야, 데이터 베이스에 저장이 됨.



**Read**

```python
#Read all
>>> Post.objects.all()
<QuerySet [<Post: Post object (2)>, <Post: Post object (3)>]>

#Get one
>>> Post.objects.get(pk=3)
<Post: Post object (3)>
```

데이터베이스로 부터 어떠한 값을 갖고 올 때, 여러개의 결과를 갖고 올지, 하나의 결과를 갖고 올지를 보고, 적절한 방법을 사용하자. 

Django의 경우, id값이 아니라 pk(primary key)로 접근을 함.



```python
#filter (WHERE)
>>> posts = Post.objects.filter(title='Hello').all()
>>> posts
<QuerySet [<Post: Post object (1)>]> 
#all()로 filter를 쓰면 복수 형으로 결과가 리스트의 형태로 뜸.

>>> posts = Post.objects.filter(title='Hello').first()
>>> posts
<Post: Post object (1)>
    
#like 
>>> posts = Post.objects.filter(title__contains='He').all()
>>> posts
<QuerySet [<Post: Post object (1)>]>

#order by
#title이라는 필드로 오름차순
>>> posts = Post.objects.order_by('title').all()
>>> posts
<QuerySet [<Post: Post object (1)>]>

#내림차순 (필드명 앞에 -붙임)
>>> posts = Post.objects.order_by('-title').all()
>>> posts
<QuerySet [<Post: Post object (1)>]>

#limit & offset
>>> Post.objects.all()[:1]
<QuerySet [<Post: Post object (1)>]>

>>> Post.objects.all()[1:2]
<QuerySet [<Post: Post object (2)>]>
```



**Delete**

django에서는 SQL과 다르게 id 값이 아닌 pk (primary key)로 고유값에 접근함.

```python
>>> post = Post.objects.get(pk=1)
>>> post.delete()
(1, {'posts.Post': 1})
```



**Update**

파이썬 내 Post라는 클래스의 인스턴스가 수정된 것이므로 save를 반드시 해줘야 Database에도 수정이 적용된다.

```python
>>> post = Post.objects.get(pk=2)
>>> post.title
'1번째'
>>> post.title = '2번째로변경'
>>> post.title
'2번째로변경'

>>> post.save()
>>> post = Post.objects.get(pk=2)
>>> post.title
'2번째로변경'
```



**Model을 활용하여 웹페이지 생성하기(New / Create)**

```python
#views.py
from django.shortcuts import render
from .models import Post

def new(request):
    return render(request, 'new.html')


def create(request):
    title = request.GET.get('title')
    content = request.GET.get('content')
    
    post = Post(title=title, content=content)
    post.save()
    
    return render(request, 'create.html')


#urls.py
from posts import views

urlpatterns = [
    path('create/', views.create),
    path('new/', views.new),
]
```

```html
<-- new.html -->
<body>
    <form action="/posts/create/", method="get">
        <input type="text" name="title"/>
        <input type="text" name="content"/>
        <input type="submit" value="Submit"/>
    </form>

</body>
    
<-- create.html -->
<body>
   <h1> 성공적으로 Post를 생성 했습니다! </h1>
</body>
```



`views.py` 에서 `render`  함수로 `new.html` 을 호출함. 
input 태그를 통해 들어오는 값은 총 2가지로, 각각 `title` 과 `content`라는 `name`의 속성으로 정의 되어 있다. 
여기서 `Dict`의 구조를 띔. {title: 사용자 입력 값, content: 사용자 입력값} 

`views.py` 안 `create`  함수에서 `Dict`에서 저장된 value값을 가져와 각각 `title` 과 `content` 라는 변수에 저장.

```python
title = request.GET.get('title')
content = request.GET.get('content')
```



데이터베이스에 내용을 저장하는 작성함. 아래의 경우, Post 클래스를 사용하기 위해 `models.py`에 작성된 Post 클래스를  `import`를 해와야함.

```python
from .models import Post

post = Post(title=title, content=content)
post.save()
```



최종적으로, `new.html` 에서 사용자가 내용을 입력하면,  `form`  태그 `action` 속성으로 연결된 `create.html` 으로 이동되어,  `views.py` 에 정의된 `create`  함수가 실행된다. 해당 함수에 정의된 변수명에 따라, 데이터베이스에 내용이 저장되며,  사용자는 `create.html` 에 따라, "성공적으로 Post되었습니다" 라는 결과를 화면을 보게 된다.



**URL구조 변경**

지금까지 우리는 프로젝트 폴더 내에 존재하는 urls.py (어플리케이션 폴더의 상위디렉토리)에 모든 url을 저장해왔다. 그런데 만약, 한 프로젝트 내에 무수히 많은 어플리케이션을 생성하고, 관련 url을 urls.py에 작성한다면, traceability 적인 측면 뿐만 아니라 직관적으로 각 어플리케이션에 해당하는 url을 구분하기 힘들 것이다. 

따라서, urls.py를 각 어플리케이션 내에 새로 생성하여, 손쉽게 urls.py를 관리 할 수 있도록 해보자.

1) 어플리케이션 내에 urls.py 작성

```python
from django.urls import path
from . import views
#현재 디렉토리 내에 views.py를 불러오므로 from 에는 현재 디렉토리를 의미하는 . 을 써줌.

urlpatterns = [
    path('create/', views.create),
    path('new/', views.new),
]
#일반적인 작성방법대로, urlpatterns을 작성한다. 
```

2) 상위 디렉토리(프로젝트 폴더) 내 urls.py 수정

```python
from django.urls import path, include

urlpatterns = [
    path('posts/', include('posts.urls')),
    path('admin/', admin.site.urls),
]
```

`path`의 첫 번째 인수로, `'posts/'` 값을 줌에 따라,  posts(어플리케이션)에 적용되는 모든 url을 직관적으로 이해할 수있음. 또한 두번째 인수로,  `include('posts.urls')` 을 주어, posts(어플리케이션) 내 urls.py와 연결을 시켰음. 이 때, 외장 함수인 include를 import 하였음.



**데이터 베이스 내용 조회**

New / Create 예제를 통해, 데이터베이스를 저장하는 것 까지 살펴보았음. 이제 데이터베이스에 저장된 내용을 조회하는 과정을 살펴보자. 장고에서는 데이터베이스의 내용을 간편히 볼 수 있는 관리자 페이지가 내장되어있음.

```python
#admin.py
from django.contrib import admin
from .models import Post
#Model.py에서 정의된 데이터의 구조에 따라 Post 클래스를 import 해옴.

admin.site.register(Post)
#관리자 페이지에서 만든 모델을 보기 위해 모델 등록
```



`기본주소/admin` 접속하여 관리자 페이지에 들어가기 위해 계정 생성을 해야함.

```bash
(crudvenv) harrylee0810:~/workspace/django/crud (master) $ python manage.py createsuperuser
Username (leave blank to use 'ubuntu'): admin
Email address: admin@admin.com
Password: 
Password (again): 
This password is too short. It must contain at least 8 characters.
This password is too common.
This password is entirely numeric.
Bypass password validation and create user anyway? [y/N]: y
Superuser created successfully.
```



객체의 내용도 보일 수 있게 admin 페이지를 커스터마이징 할 필요가 있음. 
`admin.ModelAdmin` 상속을 통해 커스터마이징이 가능함.

```python
from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('title','content',)

admin.site.register(Post, PostAdmin)
```



**데이터베이스에 저장된 레코드 보는 페이지 작성**

```python
#views.py
def index(request):
    #데이터 베이스에 저장된 모든 값을 불러옴.
    posts = Post.objects.all()
    return render(request, 'index.html', {'posts':posts})

#urls.py
urlpatterns = [
    path('', views.index),
]
```

```html
<body>
    <h1>Post Index</h1>
    <ul>
    <-- 반복문을 돌리기 위해 jinja 템플릿 사용 -->
    {% for post in posts %}
        <li>{{ post.title }} - {{ post.content }}</li>    
    {% endfor %}
    </ul>
</body>
```



