# 인자로 전달된 숫자를 이용해 카운트다운하는 함수를 정의하고,
# 이 함수를 이용한 프로그램을 작성하십시오.

# 출력
# 카운트다운을 하려면 0보다 큰 입력이 필요합니다. # 0 보다 작은 값을 전달했을 경우
# 10
# 9
# 8
# 7
# 6
# 5
# 4
# 3
# 2
# 1

x = int(input())
if x <= 0:
    print('카운트다운을 하려면 0보다 큰 입력이 필요합니다')  
else:
    for i in range(1,x+1):
        print(x-i+1)