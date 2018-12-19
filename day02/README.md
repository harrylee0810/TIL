# Day 02

## Git 설정

* `git config --global user.name 'Harry lee'` : 이름 설정
* `git config --global user.email 'sinyo0523@gmail.com'`  : 이메일 설정
* `git init` : Git 초기화, 현재 폴더를 git으로 관리하겠다!
* `git remote add origin 주소 `  : 원격 저장소 등록
  * `git remote set-url origin 주소` : 원격저장소 수정 
* `git clone 주소(github web URL 주소)` : 다른 컴퓨터에서 Github에 저장된 파일 동기화 및 Init

## commit & Push

* `git status` : 현재 폴더의 git의 상태 (수정사항이있는지? 저장이되었는지 등)
* `git add .` : 현재 폴더의 변경사항들을 commit하기 위해서 준비
* `git commit -m 'day 02입니다.' ` : commit, 변경사항 저장. 메세지는 자유롭게 작성 가능
* `git push -u origin master` : remote로 등록된 원격 저장소(remote repository).

  * 이후에는 `git push` 만입력해도 동작 

  * `-u`  : 현재컴퓨터에 있는 branch 이랑과 github의  branch 이름이 같은 경우, 

    뒤의 명령어를 생략하는 기능임 -u 이후 명령어 생략


* Mark down을 이용한 메모/저장
  * typora 또는 VSCode
* GitHub student Developer pack



## 파일조작

### 1. 파일명 변경 (import os)

1. `os.chdir(r'폴더 주소')` : 작업하고 있는 위치 변경
2. `os.listdir('.')` : 현재 working directory의 파일 목록 리스트 얻기
3. `os.rename('바꾸고자 하는 파일 이름' , '바꿀 이름')`



### Exercise 1 - Random & OS를 이용한 파일 생성 및 이름 변경

------------

#### 사람 이름이 적힌 txt파일 500개 생성하기

```python
import os
import random
family = ['김','이','박','최','황','오','강','한','제갈','하','정','송','현','손','조']
given = ['길동','준','민준','소미','수진','지은','동해','민태','준호','세정','지훈','성우','성원']

for i in range(1,501):
    cmd = f"touch {str(i)}_{random.choice(family)}{random.choice(given)}.txt"
    print(cmd)
    os.system(cmd)
```

*  `str(i)` : i는 기본적으로 숫자형임. `str()` 을 사용하여 문자열 type으로 변경

####  파일 제목을 변경하기

```python
import os
os.chdir(r'C:\Users\student\harry\day02\dummy')
for filename in os.listdir('.'):
    new_filename = filename.replace('지원자_지원자','합격자')
    os.rename(filename, new_filename)
print(os.listdir())    
```

----------

### 2. 파일 생성; 쓰기 및 읽기

#### 1) 파일 생성 및 쓰기

```python
f = open('ssafy.txt','w') #w: write. r:read, a:append
f.write('This is SSAFY!')
f.close() 
```

* `w: write, r: read, a: append`

* `close()`를 꼭 넣어야 정상적으로 종료가 됨. (계속 열려있는 상태) 

  Otherwise, `open()` 사용 시, 열려 있다는 에러가 뜰 수 있음.

#### 2) 파일 생성 및 쓰기 -1

```python
with open('ssafy.txt','w', encoding='utf8') as f:
    #각 줄에 1,2,3 입력하기
    f.writelines(['1\n','2\n','3\n']) 
    #This is 'SSAFY!' 숫자 입력하기
    for i range(10): 
        f.write(f'This is \'SSAFY\' {i}\n')
```

* `with` 문은 가장 대표적으로 쓰이는 `Context Manager` 임
* `write` : 기본적인 입력 함수 
* `writelines`  : 리스트 등 여러문장을 입력할 때 사용하는 함수
* `\` 는 `\` 다음 오는 문자가 반드시 입력되게 할 때 사용 (예. "" 안에 "" 입력)

#### 3) 파일 읽기

```python
with open('ssafy.txt','r', encoding='utf8') as f:
    lines = f.readlines()
    print(lines) #결과값: ['1\n', '2\n', '3\n']
    
    #개행문자 제거하여 출력하기 (strip 함수 이용)
    for l in lines
	    print(l.strip()) 
        #결과값:
        # 1
        # 2
        # 3
```












### vscode 기본 terminal 변경

* `ctrl + shift + p`

* shell 검색
* Select Default shell
* Git bash

### vscode  단축키

1. `ctrl + shift + p` : vscode 기본 terminal 변경 
2. `ctrl + L` : 터미널 지우기
3. `ctrl + backtick` : 터미널 열기



`git push -u origin master`





# Git 사용법/명령어

`git config --global  --list` :  현재  Git에 등록된 User 정보 확인

`git config --global user.name "이름"` : Git에 유저이름 등록

`git config --global user.email "이메일 주소"`  : Git에 이메일 등록

`ls` : Git에 등록된 폴더 리스트 확인

`cd 폴더명`  : 폴더명으로 이동

`git init`  : 현재 디렉토리로 지정된 폴더를 git으로 관리하겠다 (Initiate)

`git status` : git의 현재 Status를 확인 (추가/수정/삭제된 파일이 있는지?)

`git add 파일명.확장자` : 해당 파일을 git에 추가

`git add .` 현재 디렉토리 내 모든 파일을 업데이트

`cd ..`  : 상위폴더로 이동



 









