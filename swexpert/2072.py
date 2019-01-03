init_num = int(input())
for num in range(init_num):
    num_lst = list(map(int, input().split()))
    sum_num = 0
    for num_i in num_lst:
        if num_i % 2:
            sum_num += num_i
    print(f'#{num+1} {sum_num}')    





# k = int(input())
# l = []
# for j in range(k):
#     a = input().split()
#     sum_num = 0
#     for i in a:
#         int_num = int(i)
#         if int_num % 2 == 1:
#             sum_num += int_num
#     l.append(sum_num)

# count_num = 0
# for i_num in l:
#     count_num += 1    
#     print(f'#{count_num} {i_num}')


# for i_num in range(k):
#     print(f'#{i_num+1} {l[i_num]}') 