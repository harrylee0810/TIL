# 리스트 내포 가능을 이용해 피보나치 수열 10번째까지 출력하는 프로그램을 작성하십시오.
# 출력:
# [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

base = [1,1]
for i in range(2,10):
    a = base[-1] + base[-2]
    base.append(a)
print(base)