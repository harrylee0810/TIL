#알파벳으로 이루어진 문자열을 입력 받아 각 알파벳을 1부터 26까지의 숫자로 변환하여 출력하라.
#입력
#ABCDEFGHIJKLMNOPQRSTUVWXYZ
#출력
#1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26

alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

for i in range(len(alpha)):
    print(alpha.index(alpha[i])+1, end=" ")



# print(alpha.index('A')+1)
# print(alpha[0]) => A