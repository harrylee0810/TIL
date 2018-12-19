'''
문제 5.
표준 입력으로 물품 가격 여러 개가 문자열 한 줄로 입력되고, 각 가격은 ;(세미콜론)으로 구분되어 있습니다.
입력된 가격을 높은 가격순으로 출력하는 프로그램을 만드세요.
# 입력 예시: 300000;20000;10000
'''

# 아래에 코드를 작성해 주세요.

prices = list(map(int, input('물품 가격을 입력하세요: ').split(';')))
prices.sort(reverse=True)

for i in prices:
    print(i)

for i in range(len(prices)):
    print(prices[i])

#map 이라는 형태의 다른 데이터 type 
#class: 딕셔너리 튜플 맵 리스트 등을 일컫는 명칭
#iterable : 뽑아낼수 있는 자료 
