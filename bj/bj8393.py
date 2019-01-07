# n이 주어졌을 때, 1부터 n까지 합을 구하는 프로그램을 작성하시오.
# 첫째 줄에 n (1 ≤ n ≤ 10,000)이 주어진다.
# 1부터 n까지 합을 출력한다.

# 예제 입력: 3
# 예제 출력: 6

init_num = int(input())
result = 0
for i in range(1, init_num+1):
    result += i
print(result)

