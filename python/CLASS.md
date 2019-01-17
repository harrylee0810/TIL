# 객체 지향 프로그래밍

프로그램의 로직을 상태와 행위로 이루어진 객체로 만든 다음 해당 객체를 레고 블럭처럼 조립하여 하나의 프로그램으로 형성하는 것

즉 객체를 만들고 객체들을 이용해 문제를 해결하려는 프로그래밍.



#### 객체

변수와 메소드를 하나로 묶은것. 변수는 값을 가지고 메소드는 실행할 코드를 가짐. 

이러한 변수와 메소드를 서로 연관된것들끼리 묶어 만든것이 객체.



자동차로 예를 들면,

자동차의 변수는 연료량을 나타내는 Gauge, 속도를 나타내는 속도계가 있음. 

메소드에는 자동차가 달리고 멈추는 기능(주행기능). 

차가 가고 멈추는 과정에서 변수인 연료량과 속도계의 값에 변화를 가져옴



이처럼 변수와 연관된 기능을 메소드라고 함. 객체 지향에서는 서로 연관된 변수와 메소드를 잘 파악하고 묵어 객체를 형성하는 것이 중요

결국 객체지향은 객체라는 부품으로 잘 만들어진 레고블럭이라 볼 수 있음.

이러한 부품은 한군데서만 사용하는게 아니라 여러군데서 재 사용 가능(부품화, 재사용성)



#### 클래스

부품 객체를 만들기 위한 청사진, 설계도, 템플릿.

추상화의 과정을 통해 만들어짐



자동차를 예를 들면, 자동차의 클래스는 다음과 같이 구성되어 있다고 볼 수 있음.

변수: 연료량 속도 등의 데이터

메소드: 주행기능



## 객체지향의 구성요소

#### 클래스

같은 문제 도메인에 속하는 속성(attribute)와 행위(behavior)를 정의함.

객체지향 프로그램의 기본적인 사용자 정의 데이터 타입



#### 객체

 메모리에 로딩된 클래스를 통해 클래스를 템플릿으로 하여 메모리 상에 생산된 정보로, 인스턴스라고도 불림,

자신 고유의 속성을 가지며, 클래스에서 정의한 행위를 수행할 수 있음

객체의 행위는 클래스에서 정의된 행위에 대한 정의를 공유함으로써 메모리를 효율적으로 사용



#### 메소드

Message라고도 불림.

클래스로부터 생성된 객체 사용 시, 객체에 명령을 내리는 행위.

"객체가 가지고 있는 메소드를 호출한다. " ,  "객체에 메세지를 전달한다." 라고 표현함.

한 객체의 속성을 조작할 목적으로 사용. 객체간의 통신은 메세지 전달을 통해 이루어짐



## 객체 지향 프로그램의 특징

### 1) 추상화

객체에서 공통된 속성과 행위를 찾아서 타입을 정의하는 과정

예) 홍길동, 이순신, 강감찬 학생

공통된 속성과 행위를 통해 "학생" 이라는 타입을 정의할 수 있음.

- 공통된 속성: 학번, 이름, 주민번호, 학과, 주소, 전화번호

- 공통된 행위: 수강 신청하기, 취소하기, 휴학 신청하기, 복학신청하기

쉽게 말해, **불필요한 정보를 숨기고 중요한 정보만 표현해 프로그램을 간단히 만드는 과정.**



**추상 데이터 타입**

데이터 타입의 표현과 연산을 캡슐화

접근 제어를 통해 데이터의 정보를 은닉 할 수 있음

- 추상 데이터 타입: 클래스

- 추상 데이터 타입의 인스턴스: 객체

- 추상 데이터 타입에서 정의된 연산: 메소드



### 2) 상속

클래스의 속성과 행위를 하위 클래스에 물려주거나, 상위클래스에서 물려받는 것으로 새로운 클래스가 기존의 클래스의 데이터와 연산을 이용할 수 있게 하는 기능

기존의 클래스: 부모 / 기반 / 상위 / 슈퍼 클래스

상속받는 새로운 클래스: 자식 / 파생 / 하위 / 서브 클래스

상속 받은 하위 클래스를 이용해 프로그램의 요구에 맞추어 클래스 수정 가능

클래스 간의 종속 관계를 형성하여 객체 조직화 가능



상속의 효과?

재사용으로 인한 코드가 줄어듦 (속성이나 행위를 다시 정의할 필요가 없음)

범용적인 사용 가능(예: object 타입의 매개변수에는 strting이나 int의 객체가 쓰여도 문제되지 않음. string과 int 모두 object를 상속 받기 때문)

물려받은 자료와 메소드를 자유롭게 사용  + 추가 가능



### 3) 다형성

다양한 형태로 나타날 수 있는 특징. 어떤  한 요소에 여러개념을 넣어 놓는것.

 	가) 오버라이딩: 같은 이름의 메서드를 여러클래스에서 다른 기능을 하는 것

 	나) 오버로딩: 같은 이름의 메소드가 인자의 개수나 자료형에 따라서 다른 기능을 하는 것.



**메소드 오버라이딩**

상속으로 물려받은 자료나 메소드를 그대로 사용하지 않고 하위클래스에서 새로 정의해 사용하는 기법

상위 클래스의 메소드와 동일한 서명(매개변수의 타입, 개수, 리턴타입)을 가져야함. => 코드의 재사용성 향상



**메소드 오버로딩**

클래스 내부에 동일한 이름의 행위를 여러개 정의하는 것.

메소드의 이름이 같고, 매개변수의 타입과 수는 서로 달라야함. (리턴 타입은 관계하지 않음)

메소드로이름을 하나로 통일 할 수 있고, 같은 이름의 메소드에 여러 종류의 매개변수를 받을 수 있음.



## Excercise

멤버들의 이름과나이를 관리하기 위한 객체지향 프로그램을 만들어보자

멤버의 정보를 관리하려면? 딕셔너리 객체가 필요할 것

더 많은 멤버를 관리하기 위해서는?  딕셔너리 객체를 리스트 객체의 항목으로 사용해야 할 것임.

```python
members = [
    {"name": "홍길동", "age": 20},
    {"name": "이순신", "age": 45},
    {"name": "강감찬", "age": 35},
]

for member in members:
    print(f'{member["name"]} {member["age"]}')
```

[결과]

```
홍길동 20
이순신 45
강감찬 35
```



### 클래스 정의 및 객체 생성

```python
#클래스 정의:
class 클래스명:

#객체 생성
변수 = 클래스명() #=> 생성자 메소드: 클래스 이름과 동일한 메소드
```

```python
class Person:
    pass

member = Person() #member 객체 생성 / Persons(): 생성자 메소드

if isinstance(member, Person):
#첫번째 인자의 객체가 두번째 인자의  클래스 인스턴스인지 검사
	print("member는 Person 클래스의 인스턴스 입니다.")
```

[결과] 

```
member는 Person 클래스의 인스턴스 입니다.
```



```python
class Person:                      #=> 클래스 정의(선언) : 클래스 객체 생성
    name = '홍길동'                 #=> 멤버 변수(데이터 어트리뷰트)
    def greeting(self):            #=> 멤버 메서드(메서드)
        print(f'{self.name}')
 
iu = Person()       # 인스턴스 객체 생성 #iu는 Person이라는 클래스의 인스턴스. Person():생성자메소드
iu.name             # 멤버 변수 호출
iu.greeting()       # 메서드 호출
```

[결과]

```
'홍길동'
홍길동 입니다
```



### 객체의 생성과 소멸, 그리고 self

생성자 메소드: 객체를 생성하기 위해 호출하는 메소드

소멸자 메소드: 객체가 소멸되기전에 호출하는 메소드

생성자 메소드를 호출하면,  `__init__` 메소드가 실행되고,

소멸자 메소드를 호출하면, `__del__` 메소드가 실행 됨.



```python
class Person:
    def __init__(self, name):
        print(f'응애, {name}')
    
    def __del__(self):
        print('빠잉')
```



self는 class에 의해 생성된 객체 공간을 가리키는 식별자

인스턴스 객체 자기자신을 의미한다.

 keyword는 아니지만 관습적으로 'self'라는 명칭을 씀. 따라서 객체 공간의 필드와 메소드에 접근 할 경우, self 식별자 형식을 이용



```python
class Person:
    def __init__(self, name, age): #self가 가리키는 객체 공간에 name, age 필드 생성
        self.name = name
        self.age = age
        print(f'{self.name} 객체가 생성되었습니다.')
    
    def __del__(self):
        print(f'{self.name} 객체가 제거되었습니다.')
        
member = Person("홍길동",20)
print(f'{member.name} {member.age}')
print(dir(member))
```

[결과]

홍길동 객체가 생성되었습니다.
홍길동 20
['class', 'del', 'delattr', 'dict', 'dir', 'doc', 'eq', 'format', 'ge', 'getattribute', 'gt', 'hash', 'init', 'init_subclass', 'le', 'lt', 'module', 'ne', 'new', 'reduce', 'reduce_ex', 'repr', 'setattr', 'sizeof', 'str', 'subclasshook', 'weakref', 'age', 'name']



### 클래스와 인스턴스의 특징

인스턴스 메서드

self가 가리키는 객체의 필드 정보에 접근해 특정 목적의 기능을 수행하도록 정의된 메소드

```python
class Person:
    def __init__(self, name, age): #self가 가리키는 객체 공간에 name, age 필드 생성
        self.name = name
        self.age = age
        print(f'{self.name} 객체가 생성되었습니다.')
    
    def __del__(self):
        print(f'{self.name} 객체가 제거되었습니다.')
        
    def to_str(self): #인스턴스 메소드
        return f'{member.name} {member.age}'

#Person 클래스의 객체 세 개를 항목으로 가진 members 리스트 객체 생성
members = [
    Person("홍길동", 20),
    Person("이순신", 40),
    Person("강감찬", 35)
]

for member in members:
    print(member.to_str())
```

[결과]

홍길동 객체가 생성되었습니다.
이순신 객체가 생성되었습니다.
강감찬 객체가 생성되었습니다.
홍길동 20
이순신 40
강감찬 35



### 인스턴스 변수

클래스 내에서 self.변수 형태를 가지는 변수

객체마다 가지고 있는 객체 고유의 정보

```python
class Person:
    def __init__(self, name, age): 
        self.name = name
        self.age = age
        
#캡슐화 된 필드로 만드는 것이 필요 할 수 있음.
#입력시 유효성 검사를 할 수 없으므로 잘못된 값이 저장 될 수 있음.
        
        print(f'{self.name} 객체가 생성되었습니다.')
        
```

멤버 필드의 접근 제한이 이루어 지지 않을 경우, 나이 값에 200이 들어가거나 음수값이 들어가는 경우가 발생 할 수도 있다.

따라서 입력 데이터의 검증을 위해 적절한 멤버 필드의 접근 제한이 필요함.

파이썬에서는 외부에서 필드에 접근하는 것을 제한하기 위해 인스턴스 변수의 접근제한 기능을 가지고 있음.



```python
class Person
...
	self.__name = name
    #프라이빗 필드 생성
```

프라이빗 필드를 만들게 되면, 외부에서 접근 할 수 있는 공개된 getter / setter 메소드를 제공할 것인지 아니면 getter만 제공할지 setter까지 제공할지 고민을 해야함.

getter: 멤버를 읽어오는 메소드

setter: 멤버를 변경하는 메소드

```python
class Person:
    def __init__(self, name, age): 
        self.__name = name #프라이빗 필드 생성
        self.__age = age
        print(f'{self.__name} 객체가 생성되었습니다.')
    
    def __del__(self):
        print(f'{self.__name} 객체가 제거되었습니다.')
        
    def to_str(self): 
        return f'{member.name} {member.age}'
    
    def get_name(self): 
        #__name 필드의 값을 반환하는 getter 메소드
        return self.__name 
    	#__name 필드에 대해서는 getter 메소드만 제공하겠다는 의미
    
    def get_age(self): #__age 필드의 값을 반환하는 메소드
        return self.__age
    
    def set_age(self, age): #__age 필드의 값을 변경하는 메소드
        if age < 0:
            raise TypeError("나이는 0이상의 값만 허용합니다.")
        self.__age = age

members = [
    Person("홍길동", 20),
    Person("이순신", 40),
    Person("강감찬", 35)
]

members[0].set_age(-20)

for member in members:
    print(member.to_str())
```

[결과]

```
홍길동 객체가 생성되었습니다.
이순신 객체가 생성되었습니다.
강감찬 객체가 생성되었습니다.
이순신 객체가 제거되었습니다.
홍길동 객체가 제거되었습니다.
TypeError: 나이는 0이상의 값만 허용합니다.
```



파이썬에서는 getter/setter를 대신 할 수 있는 decorator 기능도 제공하고 있음.

```python
class Person:

    @property 또는 @property의 이름.setter
    def name(self): #변수 이름과 같은 메소드를 만들어 사용 가능
```



### 클래스 변수

클래스 내에서 클래스 명.변수 형식으로 선언된 변수

클래스 변수의 count 활용법

```python
class Person:
    count = 0
    
    def __init__(self, name, age): #객체가 생성될 때마다 호출되는 __init__메소드
        self.__name = name 
        self.__age = age
        Person.count += 1
        print(f'{self.__name} 객체가 생성되었습니다.')
    
    def __del__(self):
        print(f'{self.__name} 객체가 제거되었습니다.')
        
    def to_str(self): 
        return f'{member.name} {member.age}'
    
    @property 
    def name(self): 
        return self.__name 
    
    @property
    def age(self):
        return self.__age 
    
    @age.setter
    def age(self, age):
        if age < 0:
            raise TypeError("나이는 0이상의 값만 허용합니다.")
        self.__age = age            
    
people = [
    Person("홍길동", 20),
    Person("이순신", 40),
    Person("강감찬", 35)
]

print(f'현재 Person 클래스의 인스턴스는 총{Person.count} 개 입니다')
```

[결과]

```
홍길동 객체가 생성되었습니다.
이순신 객체가 생성되었습니다.
강감찬 객체가 생성되었습니다.
현재 Person 클래스의 인스턴스는 총3 개 입니다
```



### 클래스 메소드

클래스가 소유한 메소드

정의

```python
@classmethod
def 클래스메소드(cls, 매개변수목록): 
    #cls: 클래스 자신에 대한 참조 전달
    ...
```

사용

클래스명.클래스메소드(매개변수목록)



```python
class Person:
    count = 0
    
    def __init__(self, name, age): #객체가 생성될 때마다 호출되는 __init__메소드
        self.__name = name 
        self.__age = age
        Person.count += 1
        print(f'{self.__name} 객체가 생성되었습니다.')
    
    def __del__(self):
        print(f'{self.__name} 객체가 제거되었습니다.')
        
    def to_str(self): 
        return f'{member.name} {member.age}'
    
    @property 
    def name(self): 
        return self.__name 
    
    @property
    def age(self):
        return self.__age 
    
    @age.setter
    def age(self, age):
        if age < 0:
            raise TypeError("나이는 0이상의 값만 허용합니다.")
        self.__age = age            
    
    @classmethod
    def get_info(cls): #클래스 참조 정보가 인자로 넘어올 매개변수
        return f'현재 Person 클래스의 인스턴스는 총 {cls.count}개 입니다'
    
members = [
    Person("홍길동", 20),
    Person("이순신", 40),
    Person("강감찬", 35)
]

print(Person.get_info()) #Person class 통해 호출
```

[결과]

```
홍길동 객체가 제거되었습니다.
홍길동 객체가 생성되었습니다.
이순신 객체가 생성되었습니다.
강감찬 객체가 생성되었습니다.
이순신 객체가 제거되었습니다.
홍길동 객체가 제거되었습니다.
현재 Person 클래스의 인스턴스는 총 3개 입니다
```

  

