'''
문제 5.
표준 입력으로 물품 가격 여러 개가 문자열 한 줄로 입력되고, 각 가격은 ;(세미콜론)으로 구분되어 있습니다.
입력된 가격을 높은 가격순으로 출력하는 프로그램을 만드세요.
# 입력 예시: 300000;20000;10000
'''

# 아래에 코드를 작성해 주세요.

#1. 분리: .split() 이용하여 분리
    # input : 10;2;3 -> ['10','2','3']
prices = input('물품 가격을 입력하시오: ')
prices = prices.split(';')

#2. 반복, 숫자변환: 반복을 통한 item들 int() 이용
int_prices =[] #or list()
for i in prices: #=> ['10','2','3']
    int_prices.append(int(i)) #=> 첫번째 반복: [10], 두번째 반복: [10,2], 마지막 반복: [10,2,3]

#3. 정렬: .sort() + revsered=True
int_prices.sort(reverse=True) #=> [2,3,10]

#3-1 .reverse()
#int_prices.reverse() #=> [10,3,2]

#3-2  sorted() + reversed()
#sorted_prices = reverse(sorted(int_prices))

    #3대장: reduce,select, map

#4. 출력
print(int_prices)

