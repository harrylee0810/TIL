# DAY 04 - 오전

### Json이란?

---------

json(JavaScript Object Notation)은 원래 자바스크립트에서 만들어진 데이터 표현방식으로 최근들어 사용이 부쩍 증가되고 있다. 예전에는 xml방식의 데이터 교환을 많이 했다면 요새는 거의 json으로 하는 추세이다.

json은 파이썬의 딕셔너리와 매우 비슷하게 생겼다.

*json 표현의 예*

```python
{
    "name": "홍길동",
    "birth": "0525",
    "age": 30
}
```



### Dictionary

----

API를 활용하는데 있어서 가장 많이 사용되는 자료형. 웹을 하면서 계속 만나게 될 자료형.

`Key`와 `Value`의 구조

`Key`는 `string`, `integer`, `float`, `boolean` 이 가능 (`list`, `dictionary`는 불가)

`Value`는 모든 자료형이 가능하다. (`list` , `dictionary` 도 가능)

`,(trailing comma)`가 들어가도 출력이 됨.

마지막 item에 trailing comma 를 넣는것이 현재 개발자들의 추세이다.

(아이템을 추가할 때, 위 line으로 올라가서 comma를 추가로 넣을 필요가 없음)

(git 으로 push 할때도,  comma를 넣을 경우, update가 되버리기 때문에, 실제 수정한 부분을 track하기 어려울 수도 있음)



```python
lunch = {
    '중국집':'02-123-123',
    '양식집':'051-111-1111',
}

print(lunch)
```

dict()를 사용하여 변수값을 딕셔너리로 변경할수 도 있음.

key에는 따옴표를 쓰지 않음을 유의하자

```python
dinner = dict(중국집='02-123-123')
```

딕셔너리에 내용 추가하기

```python
lunch['분식집'] = '051-323-777'  
```

딕셔너리 내용 가져오기

```python
print(lunch['중국집']) #=> '02-123-123'
```

딕셔너리 내에 또다른 딕셔너리가 있는 경우? (트리형)

```PYTHON
idol = {
    'bts' : {
        '지민':24,
        'RM':25,
    }
}
idol['bts'] #=> 결과 값: 하위 dictionary로 나옴.  {'지민':24, 'RM':25}
idol['bts']['RM'] #=> 25
```

딕셔너리에 반복문을 활용할 경우, 출력되는(기준이되는) 값은 key 이다.

value값 출력하기 위해서는 딕셔너리명[KEY명] 으로 접근해야함. 



딕셔너리 반복문 활용하기

```python
lunch = {
    '중국집':'02-123-123',
    '양식집':'051-111-1111',
}

#4. 딕셔너리 반복문 활용하기
#4-1. 기본 활용
for key in lunch:
    print(key) #=> key 값 출력
    print(lunch[key]) #=> value 값 출력

#4-2. key만 가져오기: .keys()
for key in lunch.keys():
    print(key)  #=> dict.keys()가 출력됨. 리스트와 유사한 형태.

#4-3. value만 가져오기: .values()
for value in lunch.values():
    print(value) #=> dict.values()가 출력됨. 또한 리스트와 유사한 형태.

#4-4. item(key. value) 가져오기: .items()
#lunch.items() => [('중식','02'), ....]  튜플의 형태로 출력됨.
for item in lunch.items():
    print(item)

for item in lunch.items():
    print(item[0], item[1])

for key, value in lunch.items(): 
#=> 변수를 넣을 때 key, value로 넣으면 파이썬에서 인식 가능.
    print(key, value)
```



# DAY 04 - 오후

```python
ssafy = {
    "location": ["서울", "대전", "구미", "광주"],
    "language": {
        "python": {
            "python standard library": ["os", "random", "webbrowser"],
            "frameworks": {
                "flask": "micro",
                "django": "full-functioning"
            },
            "data_science": ["numpy", "pandas", "scipy", "sklearn"],
            "scrapying": ["requests", "bs4"],
        },
        "web" : ["HTML", "CSS"]
    },
    "classes": {
        "gm":  {
            "lecturer": "junwoo",
            "manager": "pro-gm",
            "class president": "엄윤주",
            "groups": {
                "1조": ["강대현", "권민재", "서민수", "이규진"],
                "2조": ["박재형", "서민호", "윤종원", "이지현"],
                "3조": ["김미진", "김영훈", "엄윤주", "여성우"],
                "4조": ["김교훈", "김유림", "송현우", "이현수", "진민재", "하창언"],
            }
        },
        "gj": {
            "lecturer": "change",
            "manager": "pro-gj"
        }
    }
}
```

## Quiz 

지역(location)은 몇개 있나요? : list length (난이도 1)

 출력예시) 4

```PYTHON
lst_location = ssafy["location"]
print(len(lst_location))
```



python standard library에 'requests'가 있나요? : 접근 및 list in (난이도 2)

출력예시) false

```python
lst_library = ssafy['language']['python']['python standard library']
if 'requests' in lst_library:
    print('true')
else:
    print('false')
```



gm반의 반장의 이름을 출력하세요. : depth 있는 접근 (난이도 2)

출력예시) 엄윤주

```python
print(ssafy['classes']['gm']['class president'])
```



ssafy에서 배우는 언어들을 출력하세요. : dictionary.keys() 반복 (난이도 3)

출력 예시) python web

```python
python_language = ssafy['language']
for i in python_language.keys():
    print(i)
```



ssafy gj반의 강사와 매니저의 이름을 출력하세요. dictionary.values() 반복 (난이도 3)

출력 예시) change pro-gj

```python
name_gj = ssafy['classes']['gj']
for name in name_gj.values():
    print(name)
```



framework들의 이름과 설명을 다음과 같이 출력하세요. : dictionary 반복 및 string interpolation (난이도 5)

출력 예시) flask는 micro이다. / django는 full-functioning이다.

```python
frameworks = ssafy['language']['python']['frameworks']
for key, value in frameworks.items():
    print(f'{key}는 {value}이다')
```



오늘 당번을 뽑기 위해 groups의 4조 중에 한명을 랜덤으로 뽑아주세요. : depth 있는 접근 + list 가지고 와서 random. (난이도 5)

출력예시) 오늘의 당번은 하창언

```python
import random

group4 = ssafy['classes']['gm']['groups']['4조']
choice = random.choice(group4)
print(f'오늘의 당번은 {choice}')
```



오늘 당번을 뽑기 위해 groups 전체 중에 한명을 랜덤으로 뽑아주세요. : depth 있는 접근 + list 가지고 와서 random. **(난이도 7)**

```python
import random
group = ssafy['classes']['gm']['groups']
group_list = []
for i in group.values():
    for j in i:
        group_list.append(j)
choice1 = random.choice(group_list)
print(f'오늘의 당번은 {choice1}')
```

```python
import random
group = ssafy['classes']['gm']['groups']
group_list = []
for i in group.values():
    group_list += i
choice1 = random.choice(group_list)
print(f'오늘의 당번은 {choice1}')
```

```python
import random
group = ssafy['classes']['gm']['groups']
group_list = []
for i in group.values():
    group_list.extend(i)
choice1 = random.choice(group_list)
print(f'오늘의 당번은 {choice1}')
```

## Flask

```python
from flask import Flask, render_template
app = Flask(__name__)

@app.route("/ping")
def ping():
    return render_template('ping.html')
```





#request: 어디선가 정보를 넘겨주면 요청에 대한 정보를 컨트롤 해주는 함수(flask 함수)

요청을 보내는 라이브러리.



request.args: 딕셔너리 타입

args를 넘겨받고 받는데는 딕셔너리 형태를 씀



{{}} : 플라스크에서 사용하고 있는 진자 템플릿(jinja2)을 이용한 것. 



파이썬: json 형태를 딕셔너리 형태로 자동으로 변경해줌.

json은 딕셔너리와 유사한 형태

json viewer





git ignore



.gitignore 라는 파일생성



python gitignore

git으로 관리해선 안되는 리스트를 찾을 수 있음.



