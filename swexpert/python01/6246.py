# while문을 이용해 아래와 같이 별(*)을 표시하는 프로그램을 만드십시오.
# 입력:
# 출력
# *****
# ****
# ***
# **
# *

a = int(input())
for i in range(1,a+1):
    for j in range(a-i+1):
        print('*', end="")
    print()
