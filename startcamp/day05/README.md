# DAY 05 - 오전

## Telegram을 이용한 챗 봇 만들기

1. @botfather 검색
2. /newbot 입력
3. bot name & username 입력
4. user name으로 검색(@harry0810_bot)
5. Bot API 에 대한 Description: https://core.telegram.org/bots/api

## Authorizing your bot

### Making requests

`https://api.telegram.org/bot<TOKEN>/METHOD_NAME` : 요청(Request)를 보내는 기본 양식

예시) `https://api.telegram.org/bot123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11/getMe`

- token: HTTP API에 access 하기 위한 Bot 고유 번호 (Bot의 주민등록번호 같은 개념)
- METHOD_NAME: 메소드 명 입력 (예. getUpdates / sendMessage)

### Getting updates

### GetUpdates

https://api.telegram.org/bot1111111111111[^1]/getUpdates

getUpdates Method를 통해서 ID에 대한 고유번호(주민번호) 찾기

result -> message ->  from -> id

```
{
"result": [
  {
    "message" : {
        "from" : {
            "id":
        }
    }  
  }
```



#### sendMessage

`기본주소/bot<TOKEN>/sendMessage?chat_id=<계정 고유번호>&text=<text명>`

예시)https://api.telegram.org/bot123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11[^1]/getMe/sendMessage?chat_id=111111[^2]&text=hi[^3]



#### sendMessage - VSCODE & Python3를 활용한 변수화 &  Formatting

```PYTHON
import requests

chat_id = 'id고유번호'
text = '반갑습니다'
token = 'token고유번호'

requests.get(f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={text}')
```

chat_id & token은 고유번호(주민등록번호) 이므로, py  파일 안에 저장하기에는 정보노출 등의 문제가 있을 수 있음. 따라서, 해당 고유번호를 gitbash에게 들고있게 하고, 그번호를  gitbash 로부터 갖고오는 작업을 진행해야 함. 

1. 코드를 gitbash한테 들고 있어라고 알려줘야함.
2. code ~/.bash_profile: .bash_profile 파일 만듬
3. 데이터를 다음과 같이 입력(.bash_profile 파일 내용)

```python
export TELEGRAM_BOT_TOKEN='71111:AAG7abababadfafsfsdfsdf'
export CHAT_ID='1111111'
```



저장

gitbash 새로고침필요 : exec $SHELL

​					source ~/.bash_profile



printenv: 깃배쉬가 들고있는정보 확인하는 명령어





```PYTHON
import requests
import os

token = os.getenv('TELEGRAM_BOT_TOKEN')
chat_id = os.getenv('CHAT_ID')
text = '반갑습니다'

requests.get(f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={text}')
```

os.getenv 를 통해서 gitbash에 저장된 정보를 가지고 옴.



**플라스크를 이용하자!**

```python
@app.route('/write')
def write():
    return render_template('write.html') 
#write.html을 띄워주는 /write 페이지 생성

@app.route('/send')
def send():
    return render_template('send.html') 
```

```html
<h1>메세지 작성</h1>

<form action= "/send">
    <input type="text" name="message">
    <input type="submit">

</form>
```

```html
<h1>전송 완료!</h1>

<a href="/write">돌아가기</a>
```

`action="/send" ` send page로 이동하겠다.

`<input type="submit">` submit 제출하겠다. (페이지 이동 버튼)

input: 내용을 입력하는데, action 뒤의 ? 이하 내용

name: 말그대로 이후 인풋에 대한 제목? 이름. 

type:어떤 종류?

#### 최종 복합...

```python
import os

@app.route('/send')
def send():

    token = os.getenv('TELEGRAM_BOT_TOKEN')
    chat_id = os.getenv('CHAT_ID')
    text = request.args['message']

    # args는 dic형태임. []쓸것.

requests.get(f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={text}')

    return render_template('send.html') 
```

http://127.0.0.1:5000/send?message=오호



## setWebhook

텔레그램으로 메세지를 작성 -> 텔레그램 서버로 전송 (어딘가의 데이터 베이스에 저장)

봇을 통해서 메세지를 보내면 여기까지의 과정만 구현되어있음.

유저에게 보낼때는, 어딘가의 저장된 데이터베이스로부터 유저에 전송



메세지  ------------->           텔레그램 서버    --------------------> 유저

​						(데이터베이스)



> Webhook이란?
>
> Webhook(웹훅)이란, 서버에서 어떠한 작업이 수행 되었을 때 해당 작업이 수행되었음을 `HTTP POST`로 알리는 개념을 말합니다. Webhook을 구현한 웹 애플리케이션은, 특정 작업이 수행될 때 `URL`에 대해 `POST`방식으로 요청을 생성합니다. 이 때, url(콜백 url)은 웹 애플리케이션을 사용하는 유저가 자신의 `URL`을 지정할 수 있습니다.



웹훅이라는 것을 이용하여,  DB에 저장되는 행위가 발생하면,  이 행위에 대한 특정한 URL을 통해서 이 내용을 알려주는 기능을 함.

URL 주소를 텔레그램에게 알려줘야함.

그런데 IP 주소 기반의 URL 주소는 텔레그램에 알려줄 수 없음.

따라서 외부 서버가 필요함. C9 (AWS Cloud 9) 리눅스 서버



https://gist.github.com/nwith

pyenv :파이썬 버젼 설정하게 하는 명령어

simple Python Version Management: pyenv

pyenv install 3.6.7: 3.6.7버젼 설치 명령어

pyenv versions : pyenv로 설치된 파이썬 버젼 확인 명령어

pyenv global 3.6.7:  global을 3.6.7 으로 변경



FLASK 웹사이트를 통해 설정 할 것



FLASK_APP=app.py flask run --host=$IP --port=$PORT

외부에서 접속하는 통로와 접근하는 주소를함께 지정



1) URL을 텔레그램에 알려주기

​	c9 ~/.bashrc : 윈도우 배쉬프로그램에 숨겨놨던 키 값 찾기

​	생긴 .bashrc 파일에 텔레그램 봇 토큰 값을 입력 (export TEL EGRAM_BOT_TOKEN = '토큰값')

2) printenv: 운영체제가 어떠한 값들을 keep하고 있는지? 



get: 주소창에 입력하는 방식 

post: 어떠한 정보를 보내서, 데이터베이스에 저장을 한다거나, 파일을  내부적으로생성하는 동작

텔레그램은 항상 POST방식 사용



SetWebhook에 있는 url  파라미터를 사용해야함.

기본 url 구조는?

`https://api.telegram.org/bot<token>/setWebhook?url=<cloud9 Application주소>/<token>`



`https://api.telegram.org/bot<token>/METHOD_NAME` : 요청(Request)를 보내는 기본 양식

`METHOD_NAME`으로  `setWebhook`  이라는 METHOD_NAME + url이라는 파라미터를 조합 -> `setWebhook?url=`

url 이하 주소는 cloud9 application 주소

`https://api.telegram.org/bot<token>/setWebhook?url=http://telegram-harrylee0810.c9users.io:8080/<token>`

url이하에 cloud9 application주소 입력 후 / 토큰 입력



C9이라는 것을 사용하는 이유? 웹훅이라는 것을 사용하기위해

해당 유저가 어떠한 메세지를 텔레그램에 보내면, 

텔레그램은 데이터를 저장하고 가지고있을것.

그리고 그것을 응답해야 유저가 받을 수 있음.

```python
import os
from flask import Flask
app = Flask(__name__)

token = os.getenv('TELEGRAM_BOT_TOKEN')

@app.route(f'/{token}', methods=['POST'])
def telegram():
    
    return '', 200

if __name__ == '__main__':
    app.run(host=os.getenv('IP','0.0.0.0'),port=int(os.getenv('PORT',8080)))

```

1. 유저A가 텔레그램을 통해 메세지를 보냄

2. 메세지는 텔레그램 서버로 전송 & 메세지를 들고 있음.

   2.1 (원래라면) 갖고 있는 메세지를 유저B로보낼것

3.  여기서 우리는 봇을 생성함 (가상의 유저)

4. 봇은 가상의 채팅방,사람이므로, 누군가가 관리를 해줘야함

    => 토큰을 이용 (토큰은 봇을  봇을 조작 할 수 있는 권한 개념)

5.  원래는 깡통봇. 어떠한 메세지를  입력해도 채팅방 내에서만 돌고돔.

6.  웹훅이라는  개념을 이용해서, 텔레그램아, 봇한테 어떠한 사용자가 메세지를보내면 그걸 다른사람에게도 알려줘~

   => setWebhook?url= "서버주소"

   텔레그램한테 이 서버주소로 메세지를 보내라고 설정하는것

   이 주소는 C9과 같음.(FLASK & C9 WEB SERVER)

   SSAFY 컴퓨터는 개인 컴퓨터이므로, 접속할 수 있는 주소가 없음.

   개인컴퓨터 -> 웹사이트, 서버 접속은 가능하나,

   웹서버, 사이트 -> 개인컴퓨터 로의 접속 은 매우 까다롭다 (도메인도 사야함)

   이러한 절차를 간편하게한것이 C9

   http://telegram-harrylee0810.c9users.io:8080/ C9 서버를 이용하면 텔레그램이 메세지를 보낼 수 있음.

7. 여기까지, 텔레그램이 메세지를 보내면, C9에서 지금 Positive한 응답을 하는 것임.

 [21/Dec/2018 05:45:48] "GET / HTTP/1.1" 200 - 이라 뜨면, 응답이 재대로 되는것임.



#1. 어떤 메세지가 뜨는지 확인하기 위해서는?(구조 확인 하기)

#2. 그대로 돌려보내기 (메아리)

```python
import os
import requests #=> requests를 import 해야함. 
				#=> pip install requests도 할것
from flask import Flask, request
app = Flask(__name__)

token = os.getenv('TELEGRAM_BOT_TOKEN')

@app.route("/")
def hello():
    return "Hello World!"

@app.route(f'/{token}', methods=['POST'])
def telegram():
    
    #1. 구조 확인하기
    from_telegram = request.get_json()  #=> dict
    print(from_telegram)
    
    #2. 그대로돌려보내기 (메아리)
    #['message']  #=> 키가 없으면 에러 발생!
    #.get('message') #=> 키가 없으면 None (에러 발생 x)
    if from_telegram.get('message') is not None:
        chat_id = from_telegram['message']['from']['id']
        text = from_telegram['message']['text']
        #api.telegram.org => api.hphk.io/telegram
        requests.get(f'https://api.hphk.io/telegram/bot{token}/sendMessage?chat_id={chat_id}&text={text}')
    
    
    return '', 200

if __name__ == '__main__':
    app.run(host=os.getenv('IP','0.0.0.0'),port=int(os.getenv('PORT',8080)))
```



https://gist.github.com/nwith/

completed.py에 지정한  변수명을 .bashrc 에 업로드 해야함

c9 ~/.bashrc

```python
export NAVER_CLIENT_ID=''
export NAVER_CLIENT_SECRET=''
```



exec $SHELL : 























https://core.telegram.org/bots/api#setWebhook?url=https://telegram-harrylee0810.c9users.io/766959295:AAG7uArdPfidy1JjPQaVr2A1aJMJrvuc9pU





[^1]: bot 고유 token 번호 (bot 주민번호)
[^2]: 계정에 대한 고유번호 (계정 주민번호)
[^3]: text 내용



 





 

