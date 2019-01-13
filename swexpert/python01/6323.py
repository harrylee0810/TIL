# 다음의 결과와 같이 피보나치 수열의 결과를 생성하는 프로그램을 작성하십시오.
# 입력: 10
# 출력: [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]


def pibo(x):
    base = [1,1]
    for i in range(2,x):
        next_num = base[-1] + base[-2]
        base.append(next_num)
    return base

print(pibo(int(input())))