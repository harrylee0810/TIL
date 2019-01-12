# 다음과 같이 사용자 2명으로부터 가위, 바위, 보를 입력 받아
# 가위, 바위, 보 규칙이 정의된 함수를 이용해 승패를 결정하는 코드를 작성하십시오.

# 입력:
# 홍길동
# 이순신
# 가위
# 바위
# 출력: 바위가 이겼습니다!

def death_match(user1, user2, user1_deck, user2_deck):

    user1_win_case = {'가위':'보', '바위':'가위','보':'바위'}
    user2_win_case = {'가위':'보', '바위':'가위','보':'바위'}
    
    if user1_deck in user1_win_case.keys() and user2_deck in user2_win_case.keys():
        if user1_win_case[user1_deck] == user2_deck:
            return user1_deck + '가 이겼습니다!'
        elif user1_deck == user2_deck:
            return '무승부 입니다'
        elif user2_win_case[user2_deck] == user1_deck:
            return user2_deck +'가 이겼습니다!.'
    else:
        return '가위/바위/보 중 입력해주세요'


a = input()
b = input()
c = input()
d = input()
print(death_match(a,b,c,d))