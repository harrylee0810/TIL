# 다음의 결과와 같이 반목문을 이용해 단어의 순서를 거꾸로 해 반환하는 함수를 작성하고
# 그 함수를 이용해 회문(앞뒤 어느 쪽에서도 같은 단어, 말) 여부를 판단하는 코드를 작성하십시오.

# 입력: eye
# 출력: 입력하신 단어는 회문(Palindrome)입니다.

def palin(a):
    b = a[::-1]
    if a == b:
        return "입력하신 단어는 회문(Palindrome)입니다."
    else:
        return "입력하신 단어는 회문(Palindrome)이 아닙니다"

print(palin(input()))