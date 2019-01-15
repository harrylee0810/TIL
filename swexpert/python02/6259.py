# 다음과 같이 사용자가 입력한 문장에서 숫자와 문자를 구별해 각각의 개수를 출력하는 프로그램을 작성하십시오.
# 입력: hello world! 123
# 출력:
# LETTERS 10
# DIGITS 3

a = input()
l ="LETTERS "
count1 = 0
d="DIGITS "
count2 = 0
for i in a:
    if i.isalpha():
        count1 += 1
    elif i.isdigit():
        count2 += 1

print(f'{l}{count1}')
print(f'{d}{count2}')