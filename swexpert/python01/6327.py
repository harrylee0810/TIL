# 숫자에 대해 제곱을 구하는 함수를 정의히고, 다음과 같이 숫자를 콤마(,)로 구분해 입력하면
# 정의한 함수를 이용해 제곱 값을 출력하는 프로그램을 작성하십시오.

# 입력: 2, 3
# 출력: square(2) => 4
#       square(3) => 9



def square(x):
    return f'square({x}) => {x**2}'
    
a = list(map(int, input().split(',')))
for i in a:
    print(square(i))