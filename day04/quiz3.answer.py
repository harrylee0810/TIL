#문제 3. 도시별 최근 3일 온도 입니다.

city = {
    '서울': [-6, -10, 6],
    '대전': [-3. -6, 2],
    '광주': [0, -2, 10],
    '구미': [2, -2, 9],
}

#3-1 도시별 최근 3일의 온도 평균은?
'''
출력 예시)
서울: 값
대전: 값
광주: 값
구미: 값
'''
#1. 반복
#city.items() #=> 리스트의 형태로 출력; [('서울'),[-6, -10, 6], ....]
for name, temp in city.items():
    #name #=> '서울'
    #temp #=> [-6, -10, 6]
    total_temp = 0
    count = 0
    for t in temp:
        #1번째 시행: t = -6
        total_temp += t
        count += 1
    avg_temp = total_temp / count
    print(f'{name}:{avg_temp}')

#2. 내장함수
for name, temp in city.items():
    avg_temp = sum(temp) /len(temp)
    print(f'{name}:{avg_temp}')   