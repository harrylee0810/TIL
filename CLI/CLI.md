# CLI (Command Line Interface) 

## Standard Form

```bash
harrylee0810:~/workspace $ rm -f foo.txt
```

명령어를 실행할때, -f 이하 의 내용을 인자(파라미터)로 넘겨줘서 명령어 실행

- `$앞쪽`: prompt
- `$뒤쪽`: 명령어 입력 칸
  - `rm` : command(명령어)
  - `-f`  : command의 옵션( force 의 약자)
  - `foo.txt` : 파라미터

- `shell` : 컴퓨터랑 상호작용을 할 수있게 하는 프로그램 (예. bash / Zsh)
- `$`  bash에서 사용하는 변수

```bash
harrylee0810:~/workspace $ echo $SHELL
>>>/bin/bash
```

## Git Bash Command

- `echo <string>` : 화면에 문자열 출력
- `man <command>`  : 특정 커맨드(명령어) 매뉴얼 페이지 출력 

```bash
harrylee0810:~/workspace $ echo hello
>>>hello
harrylee0810:~/workspace $ echo 'hello'
>>>hello
harrylee0810:~/workspace $ echo "hello"
>>>hello

#작은 따옴표는 안의 내용을 그대로 출력함
harrylee0810:~/workspace $ echo '$SHELL'
>>>$SHELL
#큰 따옴표 사용 시, echo $SHELL의 명령어의 결과값이 나옴
harrylee0810:~/workspace $ echo "$SHELL"
>>>/bin/bash

#echo 명령어에 대한 매뉴얼 페이지 출력
harrylee0810:~/workspace $ man echo
```



## Git Bash 단축키

- `ctrl + c` : 현재 입력중인 작업 취소(Cancel)
  - 명령어를 잘못입력하는 경우, 원래의 `prompt(harrylee0810:~/workspace $)`로 빠져나오는 기능 (또는 `esc`)
- `ctrl + l ` : 터미널 내용 전체 삭제 (또는 `clear` 입력)
- `ctrl + a` : 맨 앞으로 이동
- `ctrl + e` : 맨 뒤로 이동
- `ctrl + u` : 커서 기준으로 앞의 내용 삭제
- `ctrl + k` : 커서 기준으로 뒤의 내용 삭제
- `ctrl + w` : 단어 단위로 내용 삭제
- `ctrl + d` : 터미널 종료 (또는 `exit` 입력)
- `alt + 마우스클릭` : 마우스로 커서 이동 (C9에서만 작동함)



## Exercise

```bash
#터미널에 Hello, World를 출력해보자
harrylee0810:~/workspace $ echo Hello, world
>>>Hello, world
harrylee0810:~/workspace $ echo 'Hello, world'
>>>Hello, world

#eho 'hello라고 입력하고 이 문제상황에서 빠져나와보자
harrylee0810:~/workspace $ echo 'Hello
>>>
#1. ctrl + c로 빠져나오기
#2. 작은따옴표 입력하여 닫기
harrylee0810:~/workspace $ echo 'Hello
'
>>>Hello

#echo 매뉴얼을 참고하여 줄바꿈(개행, newline)을 하지않고 'hello,world'를추출해보자.
harrylee0810:~/workspace $ echo -n 'hello'
>>>helloharrylee0810:~/workspace $ 

#`sleep` 이라고 하는 명령어의 매뉴얼 페이지를 읽고, 우리의 터미널을 5초간재워보자.
harrylee0810:~/workspace $ sleep 5

#이번에는 터미널을 100초간 재워보고, 중간에 깨워 보도록 하자.
harrylee0810:~/workspace $ sleep 100
^C #=> Ctrl + C
harrylee0810:~/workspace $ 
```







