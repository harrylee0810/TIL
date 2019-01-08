# 다음의 결과와 같이 가상의 두 사람이 가위 바위 보 중 하나를 내서 승패를 가르는 가위 바위 보 게임을 작성하십시오.
# 이 때 ["가위", "바위", "보"] 리스트를 활용합니다.

# 입력:
# 바위
# 가위

# 출력:
# Result : Man1 Win!

game = ["가위", "바위", "보"]

a = input()
b = input()

if (a == game[0] and b == game[2]) or (a == game[1] and b == game[0]) or (a == game[2] and b == game[1]):
    print("a win")
else:
    print("b win")
 
# win case
# 가위 보
# 바위 가위
# 보 바위

