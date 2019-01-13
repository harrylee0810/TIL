# 가변형 인자를 전달 받아 가장 큰 값을 반환하는 함수를 정의하고,
# 다음과 같은 결과를 출력하는 프로그램을 작성하십시오.
# 출력:
# max(3, 5, 4, 1, 8, 10, 2) => 10

def my_max(*args):
    result = ''
    for i in args:
        if not result:
            result += str(i)
        elif int(result) < i:
            result = i
    
    return result

print(f'max(3, 5, 4, 1, 8, 10, 2) => {my_max(3,5,4,1,8,10,2)}')