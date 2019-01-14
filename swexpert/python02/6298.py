# 주어진 튜플 (1,2,3,4,5,6,7,8,9,10)의 앞 항목 절반과 뒤 항목 절반을 출력하는 프로그램을 작성하십시오.
# 출력:
# (1, 2, 3, 4, 5)
# (6, 7, 8, 9, 10)

a = (1,2,3,4,5,6,7,8,9,10)

lst1 = []
lst2 = []
for num, item in enumerate(a):
    if num <= (len(a)-1)//2:
        lst1.append(item)
    else:
        lst2.append(item)
print(tuple(lst1))
print(tuple(lst2))