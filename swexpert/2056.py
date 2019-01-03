init_num = int(input())
for i in range(init_num):
    a = input()
    year = a[0:4]
    month = a[4:6]
    day = a[6:9]
    int_month = int(month)
    int_day = int(day)
    combo = {1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
    if int_month > 12 and int_month < 1:
        print(-1)
    elif int_day > combo[int_month]:
        print(-1)
    else:
        print(year,month,day,sep="/")