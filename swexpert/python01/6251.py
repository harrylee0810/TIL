# for문을 이용해 아래와 같이 별(*)을 표시하는 프로그램을 만드십시오.
# 출력:
#     *
#    **
#   ***
#  ****
# *****

a = int(input())
for i in range(1, a+1):
    blank = ' '*(a-i)
    star = '*'*i
    print(blank, star, sep='')