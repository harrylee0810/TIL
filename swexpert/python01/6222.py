# 다음의 결과와 같이 입력된 문자가 대문자일 경우 소문자로, 
# 소문자일 경우 대문자로 변경하고,
# 알파벳이 아닐 경우엔 그냥 출력하는 코드를 작성하십시오.
# 출력 시 아스키코드를 함께 출력합니다.

# 입력: c
# 출력: c(ASCII: 99) => C(ASCII: 67)

a = input()

small_a = a.lower()
cap_a = a.upper()
ord_small_a = ord(small_a)
ord_cap_a = ord(cap_a)

small = "abcdefghijklmnopqrstuvwxyz"
capital = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

if a in small:
    print(f'{small_a}(ASCII: {ord_small_a}) => {cap_a}(ASCII: {ord_cap_a})')
elif a in capital:
    print(f'{cap_a}(ASCII: {ord_cap_a}) => {small_a}(ASCII: {ord_small_a})')
else:
    print(a)

