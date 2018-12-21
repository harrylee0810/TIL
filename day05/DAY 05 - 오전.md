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
export TELEGRAM_BOT_TOKEN='766959295:AAG7uArdPfidy1JjPQaVr2A1aJMJrvuc9pU'
export CHAT_ID='760097723'
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



#### setWebhook

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









[^1]: bot 고유 token 번호 (bot 주민번호)
[^2]: 계정에 대한 고유번호 (계정 주민번호)
[^3]: text 내용



 





 

