# 인자로 전달된 두 개의 문자열 중 길이가 더 긴 문자열을 출력하는 함수를 정의하고
# 결과를 출력하는 프로그램을 작성하십시오.
# 입력: one, three
# 출력: three

a = list(input().split(', '))
result = ''
for i in a:
    if bool(result) == False:
        result = i
    elif len(i) > len(result):
        result = i
print(result)