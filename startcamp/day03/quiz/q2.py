'''
문제 2.
자연수 N이 주어졌을 때, 1부터 N까지 한 줄에 하나씩 출력하는 프로그램을 작성하시오.
'''

n = int(input('숫자를 입력하세요: ')) 

#1. while문 사용
i = 0
while i < n:
    print(i+1)
    i += 1

# #2. For문 사용
# for i in range(n):
#     print(i+1)

# #2. For문 사용 2
# for i in range(1,n+1):
#     print(i)


# # input은 항장 문자열로 출력함. 
# # int는 문자열 -> 숫자로 변환하는 함수
# # str은 숫자 -> 문자열로 변환하는 함수


