# 소수를 검사하는 함수를 정의하고, 다음의 결과와 같이 사용자가 입력한 숫자가
# 소수인지를 판단하는 프로그램을 작성하십시오.
# 소수일 경우 "소수입니다." 출력, 아닐 경우 "소수가 아닙니다." 출력
# 입력:13
# 출력: 소수입니다.

def sosu(a):
    lst = []
    for i in range(2,a):
        if a % i != 0:
            continue
        else:
            lst.append(i)

    if bool(lst) == True:
        return '소수가 아닙니다.'
    else:
        return '소수입니다.'

print(sosu(int(input())))
