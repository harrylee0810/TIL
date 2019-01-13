# 정렬된 숫자를 가진 리스트에서 특정 숫자를 찾는 함수를 정의하고,
# 이 함수를 이용해 임의의 숫자의 포함 여부를 출력하는 프로그램을 작성하십시오.
# 출력
# [2, 4, 6, 8, 10]
# 5 => False
# 10 => True

a = 5
b = 10
lst1 = [2, 4, 6, 8, 10]
print(lst1)
if a in lst1:
    print(f'{a} => {True}')
else:
    print(f'{a} => {False}')

if b in lst1:
    print(f'{b} => {True}')
else:
    print(f'{b} => {False}')
