# 10개의 수를 입력 받아, 그 중에서 가장 큰 수를 출력하는 프로그램을 작성하라.
# 입력
# 3 
# 3 17 1 39 8 41 2 32 99 2
# 22 8 5 123 7 2 63 7 3 46
# 6 63 2 3 58 76 21 33 8 1
# 출력
# #1 99
# #2 123
# #3 76

init_num = int(input())
for i in range(init_num):
    num_lst = list(map(int,input().split()))
    max_num = max(num_lst)
    print(f'#{i+1} {max_num}')
