# 숫자 N은 아래와 같다.
# N=2a x 3b x 5c x 7d x 11e
# N이 주어질 때 a, b, c, d, e 를 출력하라.


k = int(input())
for num in range(k):
    base = [2,3,5,7,11]
    lst = []
    a = int(input())
    for i in base:
        count = 0
        while a % i == 0 :
            a = a / i
            count += 1
        lst.append(str(count))
    result = ' '.join(lst)
    print(f'#{num+1} {result}')

# 입력
# 10  
# 6791400
# 1646400
# 1425600
# 8575
# 185625
# 6480
# 1185408
# 6561
# 25
# 330750

# 출력
#1 3 2 2 3 1
#2 6 1 2 3 0
#3 6 4 2 0 1
#4 0 0 2 3 0
#5 0 3 4 0 1
#6 4 4 1 0 0
#7 7 3 0 3 0
#8 0 8 0 0 0
#9 0 0 2 0 0
#10 1 3 3 2 0
 