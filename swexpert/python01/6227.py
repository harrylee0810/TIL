# 100~300 사이의 숫자에서 각각의 자리 숫자가 짝수인 숫자를 찾아 
# 콤마(,)로 구분해 출력하는 프로그램을 작성하십시오.

# 입력:
# 출력:
# 200,202,204,206,208,220,222,224,226,228,240,242,244,246,248,260,262,
# 264,266,268,280,282,284,286,288

lst = []
for i in range(100,301):
    lst.append(str(i))
print(lst)


lst2 = []
for j in lst: # j = '210', '200'
    if int(j[0]) % 2 == 1 or int(j[1]) % 2 == 1 or int(j[2]) % 2 == 1:
        continue
    else:
        lst2.append(j)

result = ','.join(map(str,lst2))
print(result)