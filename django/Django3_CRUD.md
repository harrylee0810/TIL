# 190129



**게시글의 세부 정보가 담긴 페이지 작성하기**

우리가 작성한 `index.html` 은 데이터베이스에 입력한 레코드 전체에 대한 정보를 보여줬음.
이제,  게시판 안의 글의 내용을 보는 것과 같이, 클릭하여 들어가서 세부 내용을 보여주는 페이지를 생성해보자.

레코드에 대한 세부 정보를 보여주기 위해서는, 각 레코드가 갖고 있는 고유값(id; pk)로 접근을 해야 함. 
이를 위해 id값을 파라미터로 갖고오는 Variable routing을 설정 해야 함.

예) 기본주소/posts/1 

```python
#views.py
def detail(request, post_id):
    post = Post.objects.get(pk=post_id)
    return render(request, 'detail.html', {'post':post})

#urls.py
urlpatterns = [
    path('<int:post_id>/', views.detail),
]
```

```html
<-- detail.html -->
<body>
    <h1>Post Detail</h1>
    <h2>Title : {{post.title}}</h2>
    <p> Content : {{post.content}}</p>
    <a href="/posts/">List</a>
 
</body>
```



`detail` 함수의 두번째 파라미터인 `post_id` 는 레코드의 고유키를 의미하는 variable routing임. 이는 `urls.py` 내 `path` 함수의 첫번째 인자와 반드시 일치 시켜줘야함. (Variable routing이 주소자체를 변수로 사용하는 거니까..)

`post = Post.objects.get(pk=post_id) ` : `Post`라는 모델 클래스를 통해 저장된 1번(pk=1) 레코드를 `post` 라는 변수로 저장함.  이때 `post` 는 `Post`  클래스의 인스턴스라고 볼 수 있음.



`‘post’` 를 템플릿 변수로 지정하였으며, 사용자의 편의상, Dict의 key값와 value값을 `post`로 일치시켰음. 
따라서,  `detail.html` 에서 템플릿 변수 `post` 를 입력하면,  `Post`의 인스턴스이자, 템플릿 변수의 key값인  `post`가 호출 됨. 
이때,  `Post`의 인스턴스인 `post` 는 클래스에서 정의된 멤버 변수(예, `post.title` / `post.content` )를 불러올 수 있음. 



추가로, 레코드 전체에 대한 정보가 담겨 있는  `기본주소/posts/ 또는 (index.html)`  으로 돌아가기 버튼을 만들기 위해, a 태그를  사용 하였음.

```python
<a href="/posts/">List</a>
```





**인덱스 페이지(전체 게시글 리스트)와 detail 페이지(레코드 상세 정보) 연결하기**

```python
#views.py
def index(request):
    posts = Post.objects.all()
    return render(request, 'index.html', {'posts':posts})
```

`views.py` - `index` 함수의 코드를 살펴보면, 모델 클래스인 `Post` 으로 작성된 레코드 전체를 갖고 오는 `Post.objects.all()` 메서드를 사용하여 `posts` 변수에 저장한 것을 알 수 있음.

`posts` 를 파이썬 쉘에서 불러오면, 다음과 같은 예시 결과가 뜬다. 여기서 우리는  `posts` 라는 변수에는 `Post` 의 인스턴스들이 리스트에 저장 되어 있다는 것을 알 수 있다.  이를 활용하여, 반복문을 통해 `posts` 내 각각의 객체 불러오는 작업을 `index.html`에서 할 수 있다.

> ```python
> >>> posts = Post.objects.all()
> >>> posts
> <QuerySet [<Post: 2번째로변경>, <Post: 추가번째>, <Post: 몇번째?>, <Post: 왜 나는  수업시간만되면>, <Post: 민재야>, <Post: [개념글]>, <Post: [뻘글]>, <Post: [정보]>, <Post: [to harry]>, <Post: 66666>, <Post: [to harry]>, <Post: 1번째>, <Post: 배가왜이리>, <Post: 123123>]>
> ```



```html
<-- index.html -->
<body>
    <a href="/posts/new/">New - 새로운 글쓰기</a>
    <ul>
    {% for post in posts %}
        <li><a href="/posts/{{post.pk}}/">{{ post.title }}</a></li>    
    {% endfor %}
    </ul>
</body>
```

`index.html` 내 진자 템플릿을 이용하여 반복문을 사용하였으며, 리스트 내 클래스 객체를 불러오는 변수명을 `post`로 정의하였음. 반복문이 돌면서 리스트 내 객체가 하나씩 호출되는 과정은 아래와 같음.

1번째 반복: post = <Post: 2번째로변경> => 기본주소/students/1
2번째 반복: post = <Post: 추가번째>
3번째 반복: post = <Post: 몇번째?>
...

각 객체는 `post`라는 `Post` 클래스의 인스턴스에 저장되어, `post.pk` 나 `post.title` 와 같이 클래스의 멤버변수를 호출하여 저장된 값을 불러올 수 있다. 

이를 활용하여, `post.pk` 를  a태그 내 링크 주소로 입력하면 variable routing 으로 반복문이 돌면서 각각의 인스턴스는  `detail` 함수(세부정보가 담긴 페이지를 호출하는 함수)를 불러오는 url patterns와 연결이 된다.

```python
#urls.py
urlpatterns = [
    path('<int:post_id>/', views.detail),
]
```





**new.html 에서 새글 작성 후, 글 세부 내용보는 페이지로 넘기기**

앞서 우리가 작성한 코드에서, `new.html`에 내용을 작성하면, `create.html`으로 연결되어 해당 웹페이지에 작성된 내용인 “성공적으로 Post되었습니다” 라는 화면을 사용자가 볼 수 있었음. 이부분을 수정하여,  `new.html`에서 내용을 작성하면, 작성한 내용을 보는 페이지로 넘어가게 해보자.



이에 앞서, 클라이언트(웹 브라우저)에서 서버를 요청(request)을 보내는 방식을 Get에서 Post로 변경을 해보자.

Get: 가져오는것 (html 문서를 보여달라!) 
Post: 수행하는 것

데이터베이스를 저장해줘 의미상 맞지않음.
post는 어떠한 데이터를 실어서 요청을 보내므로 주소창에 뜨지 않음.

```html
<-- new.html -->
<form action="/posts/create/", method="post">
{% csrf_token %}
```

> CSRF: 사이트 간 요청 위조(Cross-site Request Forgery)
>
> 웹 애플리케이션 취약점 중 하나로 사용자가 자신의 의지와 무관하게 공격자가 의도한 행동을 하여 특정 웹페이지를 보안에 취약하게 한다거나 수정, 삭제 등의 작업을 하게 만드는 공격 방법



CSRF 토큰이란 CSRF 공격에 대응을 하기 위한 방어 기법 중 하나임. 보통 CSRF공격은 특정액션시 넘어가는 파라미터를 가지고 그 행위를 특정액션 이외에 자동으로 넘어가게 하는 기법인데 이것을 넘어가는 값 중에 랜덤으로 발행되는 키값을 넘기고 받게 해서 이 값이 일치하지 않으면 그 액션을 수행하지 않는 것이다.

CSRF token은 보안상의 목적으로 사용. token을 넣어줘야 token과 함께 `create` 페이지에 요청을 보냄. 장고에서  csrf token을 가지고,  피하식별 하듯이, 우리 사이트에서 보낸 요청이라는 것을 확실히 알 수 있게 됨.

Post 메소드를 쓸 때는 반드시 `csrf_token`이 있어야함.



```python
from django.shortcuts import render, redirect

def create(request):
    title = request.POST.get('title')
    content = request.POST.get('content')
    
    post = Post(title=title, content=content)
    post.save()
    return redirect(f'/posts/{post.pk}')
```

`views.py`에서  메소드 방식을 `GET` => `POST`로 변경.

`POST`는 html 문서를 돌려주지 않음(반환 X).  그 대신 특정 페이지로 `redirect `하게 지정 할 수 있음.
`redirect`는 외장 함수 이므로 `import` 해줘야함.



**정리**

1) `new.html`에서 사용자가 내용을 입력하면,  `form 태그`에 입력된 `action` 과 `method` 속성에 따라, `기본주소/posts/create/`  url을 서버세 요청함.  

2) create 함수에서 정의된 내용에 따라, 입력된 내용이 각각 `title` & `content` 변수에 저장

3) 데이터베이스에 내용을 저장하기 위해 `Model 클래스` 인 `Post` 를 호출하여, 각각의 내용을 테이블의 구조에 맞게 저장한다.`post = Post(title=title, content=content)`  이때, `post.save()` 를 반드시 넣어야 데이터베이스에 내용이 저장됨을 잊지 말자.

4) 이후, `redirect` 함수에따라, `/posts/{post.pk}` 주소로 이동된다. (`views.py` 의 `detail` 함수 실행)





**외부 사이트로 `redirect` 적용하기**

```python
#views.py
def naver(request, q):
    return redirect(f'https://search.naver.com/search.naver?query={q}')

#urls.py
urlpatterns = [
    path('naver/<str:q>/', views.naver),
]
```





**게시판 글 삭제 하기(Delete)**

```python
#views.py
def delete(request, post_id):
    post = Post.objects.get(pk=post_id)
    post.delete()
    return redirect('/posts/')

#urls.py
urlpatterns = [
    path('<int:post_id/delete/', views.delete),
]
```

특정 글을 삭제하기 위해서는 삭제를 하고자 하는 데이터의 정보가 필요함. 이때 우리는 id값을 통해 접근할 것임.
(`post_id` 를 `variable routing` 으로 `delete` 함수의 두번째 파라미터로 작성)

위에서 많이 반복한 방법과 같이,  데이터베이스 내 특정 레코드를 갖고 오는 `Post.objects.get(pk=post_id)` 을 적용하여 `post` 변수에 저장시킨다. 이때, `variable routing` 인 `post_id` 를 base로 에 해당 하는  레코드를 갖고 온다. 

(`urls.py`에서 정의된 urlpatterns 에 따라, `기본주소/[post_id]/delete`  주소가 요청되면,  `delete` 함수가 실행됨. url주소의 `post_id` 가 `variable routing` 으로 함수내에 특정 레코드를 갖고오는 id값으로 반환됨) 

`post.delete()` 메서드를 호출하여, 레코드를 삭제 한 후,  index 페이지인 `‘/posts/’` 로 redirect 시킨다.



게시글을 삭제하는데는 추가적인 웹페이지를 작성할 필요가 없음.  따라서,  레코드의 세부정보를 보여주는 `details.html`에 내용을 구현할 수 있음.

```html
<-- details. html-->
<body>
    <h1>Post Detail</h1>
    <h2>Title : {{post.title}}</h2>
    <p> Content : {{post.content}}</p>
    <a href="/posts/">List</a>
    <a href="/posts/{{post.pk}}/delete/">Delete</a>
</body>    
```

a태그를 사용하여, 삭제 기능이 실행하기 위한 urlpatterns을 `href` 속성의 값으로 적용해 준다. 
이때, id값을 불러오기 위해 템플릿 변수를 사용하여 삭제 기능을 동적으로 구현하자.

사용자가 해당 링크를 누를 경우, urlpatterns에 따라, `view.delete` 함수가 실행되어, 내용이 삭제되고,  `index`페이지로 `redirect`된다. 





**게시판 글 수정하기(Update)**

게시판 글을 수정하기 위해서는 어떠한 레코드를 수정할건지에 대한 정보가 필요하므로 다시 id값을 받도록 하자.



new & create 페이지에서 우리는 아래와 같이 페이지의 역할을 구분했었음.

1) `new.html`: 내용 입력하는 Form을 작성하는 페이지. 작성된 내용을 `/posts/create/`로 전달하는요청을 보냄
2) `create` 함수: `/posts/create/` 로 url이 접근되면, create 함수가 실행되어, 데이터베이스에 내용을 저장시킴.



마찬가지로, 게시판 글을 수정하는 페이지도 역할을 아래와 같이 2가지로 구분하여 작성해야함.

1) `edit.html` : 내용을 수정하는 Form을 작성하는 페이지, 수정된 내용을 `posts/[id값(템플릿변수)]/update`로전달하는 요청을 보냄. 
2) `update` 함수 :  `posts/[id값(템플릿변수)]/update`  url을 사용자가 입력하면 update 함수가 실행됨.



```python
#views.py
def edit(request, post_id):
    post = Post.objects.get(pk=post_id)
    return render(request, 'edit.html', {'post':post})

#urls.py
urlpatterns = [
    path('<int:post_id>/edit/', views.edit),
]
```

사용자가 `기본주소/[id값]/edit/` url을 서버에 요청을 보내면, urlpattern에 따라 `edit` 함수가 실행됨. 

 `[id값]` 은 variable routing으로 `edit` 함수의 두번째 파라미터로 받아오며 이 값을 가지고 데이터베이스의 특정 레코드에 접근한다. 레코드 값이 저장된 `post` 변수를 html 파일에서 사용하기 위해 템플릿 변수로 지정한다.



```html
<-- edit.html -->
<body>
    <h1>Post Edit</h1>
    <form action="/posts/{{ post.pk }}/update/", method="post">
        {% csrf_token %}
        <input type="text" name="title" value="{{ post.title }}"/>
        <input type="text" name="content" value="{{ post.content }}"/>
        <input type="submit" value="Submit"/>
    </form>
</body>
```

여기서 우리는 input 내용에 변경사항을 실어서 update 주소로 보내게 된다. 

기존에 입력된 내용을 보기 위해, 템플릿 변수로 연결된 post라는 인스턴스의 멤버변수인 `post.title` 와 `post.content` 를  value 속성의 값으로 저장한다.

입력한 내용은 각각 `title` 과 `content` 변수의 value로 저장되며, 저장된 내용을 `/update/` 주소로 넘겨준다.
이때,  어떠한 레코드를 수정하는지에 대한 정보가 들어가얗므로, `post.pk`  변수는 `variable routing`으로 사용하여, update주소에 반환한다.

여기서 요청방식은 `post`가 사용되었기 때문에, 추가로 `{% csrf_token %}` 을 입력하였다.



```python
#views.py
def update(request, post_id):
    #수정하는 코드
    post = Post.objects.get(pk=post_id)
    post.title =request.POST.get('title')
    post.content =request.POST.get('content')
    post.save()
    return redirect(f'/posts/{post_id}/')

#urls.py
urlpatterns = [
    path('<int:post_id>/update/', views.update),
]
```

앞의 과정을 거칠 경우, urlpatterns 에 따라 update 함수가 실행될 것이다. `variable routing` 인`post_id`를 통해 우리는 수정하고자 하는 레코드 무엇인지 알 수 있다.

`post_id` 를 base로 특정 레코드의 정보를 갖고와  `post` 변수 (Model 클래스인 `Post`의 인스턴스)에 저장시키고,   인스턴스의 멤버변수(테이블의 필드)의 내용을 수정하는 코드를 아래와 같이 작성한다.

```python
post.title =request.POST.get('title')
post.content =request.POST.get('content')
```

우항은,  `edit.html` 에서 각각 `title` 과 `content` 변수에 저장된 input 내용을 가져오는 코드이며,
좌항은, 그 내용을 모델 클래스 `Post` 의 인스턴스인 `post` 의 변수를 의미한다.

이를 통해, input에 작성한 내용이 인스턴스인 `post`의 멤버변수에 저장되어 내용이 업데이트 된다. 그 후 데이터베이스에 변경된 내용을 적용하기 위해 `post.save()`를 쓰는 것으 잊지말자.

게시글 수정이 완료되면, 레코드(게시글)의 세부내용이 적혀있는 디페일 페이지로 `redirect `시킨다.



게시글을 업데이트 하고싶을 때 마다  `/posts/{{post.pk}}/edit/` url주소를 직접 입력하는 방법은 매우 비효율적일 것이다. 따라서, 레코드의 세부정보를 보여주는 detail.html에  게시글을 업데이트하는 내용을 구현하도록 하자.

```html
<-- details.html-->
<body>
    <h1>Post Detail</h1>
    <h2>Title : {{post.title}}</h2>
    <p> Content : {{post.content}}</p>
    <a href="/posts/">List</a>
    <a href="/posts/{{post.pk}}/edit/">Edit</a>
    <a href="/posts/{{post.pk}}/delete/">Delete</a>
</body>    
```

a태그를 사용하여, 업데이트 기능이 실행하기 위한 urlpatterns을 `href` 속성의 값으로 적용해 준다. 
이때, id값을 불러오기 위해 템플릿 변수를 사용하여 삭제 기능을 동적으로 구현하자.

사용자가 해당 링크를 누를 경우, urlpatterns에 따라, `view.edit` 함수가 실행되어, 수정하고자 하는 내용을 입력하는 웹페이지를 이동하고,  내용 입력 후, `edit.html` 에서 연결된 `update` url으로 연결되어 함수 실행후, 내용이 업데이트 된다...

