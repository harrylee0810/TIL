#10개의 수를 입력 받아, 평균값을 출력하는 프로그램을 작성하라.
# 가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고, 그 아래로 각 테스트 케이스가 주어진다.
# 각 테스트 케이스의 첫 번째 줄에는 10개의 수가 주어진다.
# 3
# 3 17 1 39 8 41 2 32 99 2
# 22 8 5 123 7 2 63 7 3 46
# 6 63 2 3 58 76 21 33 8 1

init_num = int(input())
for num in range(init_num):
    num_lst = list(map(int, input().split()))
    sum_i = 0
    for num_i in num_lst:
        sum_i += num_i
        avg_i = int(round(sum_i / len(num_lst)))
    print(f'#{num+1} {avg_i}')
    

# count = 0
# for i in lst:
#     count += 1
#     print(f'#{count} {i}')
