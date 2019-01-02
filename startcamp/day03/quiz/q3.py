'''
문제 3.
숫자를 입력 받아 짝수/홀수를 구분하는 코드를 작성하시오.
'''

number = int(input('숫자를 입력하세요: '))
if number % 2==1:
    print('홀수')
else:
    print('짝수')

# number % 2: 숫자에서 2를 나눴을 때의 나머지
# number // 2: 숫자에서 2를 나눴을 때의 몫

# 0, [], (), {}, falase

if number % 2:
    print('홀수')
else:
    print('짝수')