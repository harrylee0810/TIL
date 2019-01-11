# while문을 이용해 아래와 같이 별(*)을 표시하는 프로그램을 만드십시오.
# 출력:
# *******      => 7
#  *****       => 5
#   ***        => 3
#    *         => 1

# n = int(input())
# for i in range((n+1)//2):
#     star = '*'*(n-(i*2))
#     blank =' '*i 
#     print(blank,star,sep='')


n = int(input())
for i in range((n+1)//2):
    print(' '*i + '*'*(n-2*i) + ' '*i)