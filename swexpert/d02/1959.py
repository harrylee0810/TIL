# N 개의 숫자로 구성된 숫자열 Ai (i=1~N) 와 M 개의 숫자로 구성된 숫자열 Bj (j=1~M) 가 있다.
# 아래는 N =3 인 Ai 와 M = 5 인 Bj 의 예이다.
# Ai 나 Bj 를 자유롭게 움직여서 숫자들이 서로 마주보는 위치를 변경할 수 있다.
# 단, 더 긴 쪽의 양끝을 벗어나서는 안 된다.
# 서로 마주보는 숫자들을 곱한 뒤 모두 더할 때 최댓값을 구하라.



# 10

# 3 5
# 1 5 3
# 3 6 -7 5 4

# 7 6
# 6 0 5 5 -1 1 6
# -4 1 8 7 -9 3

# aj > bj 큰경우
# 아닌경우

result = 0
sub_result = 0

len_a, len_b = map(int, input().split())
gap = abs(len_a - len_b)

a = list(map(int, input().split()))
b = list(map(int, input().split()))
result = sum([x*y for x,y in zip(a,b)])

for i in range(gap):
    a.insert(0,0)
    sub_result = sum([x*y for x,y in zip(a,b)])
    if sub_result > result:
        result = sub_result
    print(result)


    # result = sum([x*y for x,y in zip(a,b)])
    # print(result)

# a.insert(0,0)
# print(a)

# if len_a < len_b:
