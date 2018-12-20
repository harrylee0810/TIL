#1. 딕셔너리 만들기
lunch = {
    '중국집':'02-123-123',
    '양식집':'051-111-1111',
}

dinner = dict(중국집='02-123-123')

#2. 딕셔너리에 내용추가하기.
lunch['분식집'] = '051-323-777'

print(lunch)

#3. 딕셔너리 내용 가져오기
print(lunch['중국집']) #=> '02-123-123'

idol = {
    'bts' : {
        '지민':24,
        'RM':25,
    }
}

idol['bts'] #=> 결과 값: 하위 dictionary로 나옴.  {'지민':24, 'RM':25}
idol['bts']['RM'] #=> 25


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

for key, value in lunch.items(): #=> 변수를 넣을 때 key, value로 넣으면 파이썬에서 인식 가능.
    print(key, value)

# 앞에 선언된 변수의 갯수와 뒤의 자료형(리스트,튜플 등) 길이가 같은 경우는 아래와 같이 활용이 가능하다.
a, b = [1, 2]
print(a, b)
print(a)
print(b)


