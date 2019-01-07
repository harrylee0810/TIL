# Git & GitHub

#### *새로운 자리에 깃 동기화 하는 방법*

#### 1. 복사하고자 하는 폴더를 Github에서 가져 오기.

`git clone <깃헙 복사된 주소> <폴더명>`

`git clone https://github.com/harrylee0810/TIL.git harry`

- 개인 설정을 하지 않은 상태에서 내려 받을 수 있는 이유?
- TIL repository  는 public으로 공개 설정되어있기 때문에, 누구나 다운로드는 사용 가능.
- but 업로드 및 수정은 권한이 있는 사람만 가능.
- git clone으로 내려 받은 파일/폴더는 git init/git remote add origin 등을 할 필요 없음 
- (이미 git으로 관리 되고 있기 때문임) 

- `git remote add origin`: github 주소를 등록해서 어디에 올릴 지에 대한 정보를 입력하는 명령어)

#### 2. Git bash에 입력된 기존의 계정 정보 삭제하기

`git credential reject`

`protocol=https`

`host=github.com`

#### 3. 새로운 계정 정보 입력하기

`git push`  후 계정 로그인 하기

#### 4. Git내 정보 설정 

`git config --global --list` : git에 저장된 정보 설정 확인

`git config --global user.name 'Harry Lee'                                                                                           ` :  이름 설정

`git config --global user.email 'sinyo0523@gmail.com'` : 이메일 주소설정

커밋을 작성할 때,  깃이라는프로그램에 커밋한 사람에 대한 정보를 알려주기 위한 용도.

`git log`  :  git에서 commit 시 저장된 user name 과 user email의 정보 확인 가능.



*public으로 공개된 타인의 폴더를 clone으로 내려 받은 후, push가 가능한가?*

*commit은 누구나 할 수있음 (git log시, commit된 정보가 update된 것을 알 수 있다/)*

*그러나 git push 시, 권한이 없어deny 됨.*

> remote: Permission to sgmpy/materials.git denied to harrylee0810.                                                                     fatal: unable to access 'https://github.com/sgmpy/materials.git/': The requested URL returned error: 403



## Git repository를 처음 생성한 경우

`git init`  : git 초기화. 지금 폴더를 git으로 관리하겠다!

(관리하려는 폴더 내에서 입력 할 것)

`git remote add origin 주소 ` : 원격 저장소 (remote repository) 주소 등록

`git remote set-url origin 주소` : 원격 저장소 수정



