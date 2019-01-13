k = int(input())
l = []
for j in range(k):
    a = input().split()
    sum_num = 0
    for i in a:
        int_num = int(i)
        if int_num % 2 == 1:
            sum_num += int_num
    l.append(sum_num)

count_num = 0
for i_num in l:
    count_num =+1
    print(f'#{count_num} {i_num}')
