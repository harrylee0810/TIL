# 가변형 인자로 정수들을 입력받아 곱을 반환하는 함수를 정의하고,
# 단, 1, 2, '4', 3와 같이 제대로 입력되지 않은 경우 예외를 처리하는 프로그램을 작성하십시오.
# 출력: 에러발생

def gop(*args):
    result = []

    for i in args:
        if type(i) == int:
            result.append(str(i**2))
        else:
            return '에러발생'
    
    return ' '.join(result)

print(gop(1,2,'4',3))