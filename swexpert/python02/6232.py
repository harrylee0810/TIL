# 다음의 결과와 같이 회문(앞뒤 어느 쪽에서도 같은 단어, 말) 여부를 판단하는 코드를 작성하십시오.
# 입력: madam
# 출력: madam
# 입력하신 단어는 회문(Palindrome)입니다.

a = 'madam'
if a == a[::-1]:
    print('입력하신 단어는 회문(Palindrome)입니다.')
else:
    print("입력하신 단어는 회문(Palindrome)이 아닙니다.")