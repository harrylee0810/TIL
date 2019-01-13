# 다음과 같이 팩토리얼을 구하는 함수를 정의해 입력된 숫자에 대한
# 팩토리얼 값을 구하는 프로그램을 작성하십시오.
# 입력:5
# 출력:120

# for문 사용
# a = int(input())
# b = 1
# for i in range(1,a+1):
#     b *= i
# print(b)

#재귀함수 사용


def fact(x):
    if x == 1:
        return 1
    else:
        return x * fact(x-1)

print(fact(int(input())))       