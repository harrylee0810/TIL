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


for key in city.keys():
    #1번째 시행: '서울'
    #city[key] #=> city[서울] #=> [-6, -10, 6]
    #sum(city[key]) #=> -10
    #len(city[key]) #=> len([-6, -10, 6]) #=> 3

    #avg_temp = -10 / 3 #=> -3.333333
    avg_temp = sum(city[key])/len(city[key])  
    
    print(f'{key}:{avg_temp}')

