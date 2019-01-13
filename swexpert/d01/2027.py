#주어진 텍스트를 그대로 출력하세요.
#  #++++
#  +#+++
#  ++#++
#  +++#+
#  ++++#

a = int(input())

for i in range(1,a+1):
    for j in range(1,a+1):
        if i == j:
            print("#", end="")
        else:
            print("+", end="")
    print("")

# for 1 in 2
#     for 1 in 2
#      print #
#     for 2 in 2
#      print +

# for 2 in 2
#     for 1 in 2
#     print +
#     for 1 in 2
#     print #
