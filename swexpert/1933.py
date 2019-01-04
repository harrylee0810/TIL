# 입력으로 1개의 정수 N 이 주어진다.
# 정수 N 의 약수를 오름차순으로 출력하는 프로그램을 작성하라.
# 10
# 1 2 5 10


init_num = int(input())
lst =[]
for i in range(1,init_num+1):
    if init_num % i == 0:
        lst.append(i)

for i in lst:
    print(i, end=" ")







# init_num = int(input())
# lst =[]
# for i in range(1,init_num+1):
#     if init_num % i == 0:
#         lst.append(i)

# for i in lst:
#     print(i, end=" ")