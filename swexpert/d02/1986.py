# 1부터 N까지의 숫자에서 홀수는 더하고 짝수는 뺐을 때 최종 누적된 값을 구해보자.
# N은 1 이상 10 이하의 정수이다. (1 ≤ N ≤ 10)

base = int(input())
for k in range(base):
    a = int(input())
    result = 0
    for i in range(1,a+1):
        if i % 2:
            result += i
        else:
            result -= i
    print(f'#{k+1} {result}')





# [예제 풀이]
# N이 5일 경우: 1 – 2 + 3 – 4 + 5 = 3
# N이 6일 경우: 1 – 2 + 3 – 4 + 5 – 6 = -3

# 입력
# 2
# 5
# 6

# 출력
# #1 3
# #2 -3