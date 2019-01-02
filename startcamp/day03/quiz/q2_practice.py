'''
문제 2.
자연수 N이 주어졌을 때, 1부터 N까지 한 줄에 하나씩 출력하는 프로그램을 작성하시오.
'''

n = int(input('숫자를 입력하세요: ')) 
# i = 0
# while i < n:
#     print(i+1)
#     i += 1

for i in range(n):
    print(i+1)