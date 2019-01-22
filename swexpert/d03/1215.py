# "기러기" 또는 "level" 과 같이 거꾸로 읽어도 앞에서부터 읽은 것과 같은 문장이나 낱말을 회문(回文, palindrome)이라 한다.
# 주어진 8x8 평면 글자판에서 가로, 세로를 모두 보아 제시된 길이를 가진 회문의 총 개수를 구하는 문제이다.
# [제약 사항]
# 각 칸의 들어가는 글자는 c언어 char type으로 주어지며 'A', 'B', 'C' 중 하나이다.
# 글자 판은 무조건 정사각형으로 주어진다.
# ABA도 회문이며, ABBA도 회문이다. A또한 길이 1짜리 회문이다.
# 가로, 세로 각각에 대해서 직선으로만 판단한다.
# 즉, 아래 예에서 노란색 경로를 따라가면 길이 7짜리 회문이 되지만 직선이 아니기 때문에 인정되지 않는다.

for z in range(1,11):
    n_palin = int(input())
    count1 = 0
    total_lst1 = []
    for j in range(8):
        a = input()
        total_lst1.append(a)
        for i in range(len(a)-n_palin+1):
            if a[i:n_palin+i] == a[i:n_palin+i][::-1]: 
                count1 +=1

    total_lst2=[]
    sub_lst2=''
    for l in range(8):
        for k in total_lst1:
            sub_lst2 += k[l]
        total_lst2.append(sub_lst2)
        sub_lst2=''

    for m in total_lst2:
        for n in range(len(m)-n_palin+1):
            if m[n:n_palin+n] == m[n:n_palin+n][::-1]:
                count1 +=1

    print(f'#{z} {count1}')

# for i in range(1,11):
#     e=int(input())
#     p=[input() for i in range(8)]
#     s=[''.join(k) for k in list(zip(*p))]
#     c=0
#     for x in [p,s]:
#         for x in x:
#             for j in range(9-e):
#                 if x[j:j+e]==x[j:j+e][::-1]:
#                     c+=1
#     print(f'#{i} {c}')


#  C   B   B   C   B   A   A   B
#  0   1   2   3   4   5   6   7
# -8  -7  -6  -5  -4  -3  -2   -1

#회문3    4    5     6     7
# [0:3] [0:4] [0:5] [0:6] [0:7]
# [1:4] [1:5] [1:6] [1:7] [1:8]
# [2:5] [2:6] [2:7] [2:8]
# [3:6] [3:7] [3:8]
# [4:7] [4:8] 
# [5:8]      
#  6번  5번   4번    3번   2번  