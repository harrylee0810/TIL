# 2개의 수를 입력 받아 크기를 비교하여 등호 또는 부등호를 출력하는 프로그램을 작성하라.
# 3
# 3 8 
# 7 7 
# 369 123
# #1 <
# #2 =
# #3 >


init_num = int(input())
for num in range(init_num):
    num_lst = list(map(int,input().split()))
    if num_lst[0] > num_lst[1]:
        print(f'#{num+1} >')
    elif num_lst[0] < num_lst[1]:
        print(f'#{num+1} <')
    else:
        print(f'#{num+1} =')