# 달팽이는 1부터 N*N까지의 숫자가 시계방향으로 이루어져 있다.
# 다음과 같이 정수 N을 입력 받아 N크기의 달팽이를 출력하시오.
# 입력:
# 2
# 3
# 4

# 출력
# #1
# 1 2 3
# 8 9 4
# 7 6 5
# #2
# 1 2 3 4
# 12 13 14 5
# 11 16 15 6
# 10 9 8 7


n = int(input())

lst = [[0 for i in range(n)] for i in range(n)]
x=y=s=0
for i in range(n*n):
    lst[x][y] = i+1
    if s == 0:
        if y+1>=n or lst[x][y+1] > 0:
            s=1
            x+=1
        else:
            y+=1
        print(lst)
    elif s==1:
        if x+1>=n or lst[x+1][y] > 0:
            s=2
            y-=1
        else:
            x+=1
        print(lst)
    elif s==2:
        if y-1<0 or lst[x][y-1] >0:
            s=3
            x-=1
        else:
            y-=1
        print(lst)
    elif s==3:
        if x-1<0 or lst[x-1][y]>0:
            s=0
            y+=1
        else:
            x-=1
        print(lst)