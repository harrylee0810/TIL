# 다음의 결과와 같이 10진수를 2진수로 변환하는 프로그램을 작성하십시오.
# 입력: 25
# 출력: 1001

a = 25
result = ''

while a > 0:
    mok = a // 2
    nam = a % 2
    result = str(nam) + result
    a = mok

print((result))

