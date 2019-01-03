#하나의 자연수를 입력 받아 각 자릿수의 합을 계산하는 프로그램을 작성하라.
#입력
#6789
#30

a = input()

sum_i = 0
for i in a:
    int_i = int(i)
    sum_i += int_i
print(sum_i)

