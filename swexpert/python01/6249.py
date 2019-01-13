# 다음의 결과와 같이 어떤 한 양의 정수를 입력하여 그 숫자에 0~9가 몇 번 사용되었는지 표시하십시오.
# 입력 : 11
# 출력 :
# 0 1 2 3 4 5 6 7 8 9
# 0 2 0 0 0 0 0 0 0 0

# a = list(input())
# lst = ['0' ,'1' ,'2', '3', '4', '5', '6', '7', '8', '9'] 
# lst2 = []

# for i in lst:
#     if i not in a:
#         lst2.append(0)
#     else:
#         lst2.append(a.count(i))

# print(' '.join(lst))
# print(' '.join(list(map(str,lst2))))

a = input()
d = {'0':0, '1':0, '2':0, '3':0, '4':0, '5':0, '6':0, '7':0, '8':0, '9':0}
lst1 =[]
lst2 = []

for i in a:
        d[i]+=1

for k, v in d.items():
    lst1.append(k)
    lst2.append(v)

print(' '.join(lst1))
print(' '.join(list(map(str,lst2))))