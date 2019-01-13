#2개의 수 a, b를 입력 받아, a를 b로 나눈 몫과 나머지를 출력하는 프로그램을 작성하라.
# [입력]
#   3   
#    9 2  
#   15 6 
#   369 15
# [출력]
#   #1 4 1
#   #2 2 3
#   #3 24 9

a = int(input())
for i in range(a):
    num = list(map(int, input().split()))
    share = num[0] // num[1]
    remainder = num[0] % num[1]
    print(f'#{i+1} {share} {remainder}')
