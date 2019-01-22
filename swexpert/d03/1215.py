# "기러기" 또는 "level" 과 같이 거꾸로 읽어도 앞에서부터 읽은 것과 같은 문장이나 낱말을 회문(回文, palindrome)이라 한다.
# 주어진 8x8 평면 글자판에서 가로, 세로를 모두 보아 제시된 길이를 가진 회문의 총 개수를 구하는 문제이다.
# [제약 사항]
# 각 칸의 들어가는 글자는 c언어 char type으로 주어지며 'A', 'B', 'C' 중 하나이다.
# 글자 판은 무조건 정사각형으로 주어진다.
# ABA도 회문이며, ABBA도 회문이다. A또한 길이 1짜리 회문이다.
# 가로, 세로 각각에 대해서 직선으로만 판단한다.
# 즉, 아래 예에서 노란색 경로를 따라가면 길이 7짜리 회문이 되지만 직선이 아니기 때문에 인정되지 않는다.

n_palin = int(input())

count1 = 0
total_lst1 = []
sub_lst1 = []
for i in range(8):
    a = input()
    sub_lst1.append(a)
    total_lst1.append(sub_lst1)
    sub_lst1 = []  
    for i in range(int(len(a)/2)+1):
        if a[i:n_palin+i] == a[i:n_palin+i][::-1]: 
            count1 +=1
            

print(count1)
print(total_lst1)



#  C   B   B   C   B   A   A   B
#  0   1   2   3   4   5   6   7
# -8  -7  -6  -5  -4  -3  -2   -1

# [0:4] == [-4:-8]
# [1:5] == [-7:-3]
# [2:6] == [-6:-2]
# [3:7] == [-5:-1]
# [4:8]