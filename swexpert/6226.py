# 1~200 사이의 정수 가운데 7의 배수이면서 5의 배수는 아닌 모든 숫자들을 찾아
# 콤마(,)로 구분된 문자열을 구성해 출력하는 프로그램을 작성하십시오.
# 입력:
# 출력:
# 7,14,21,28,42,49,56,63,77,84,91,98,112,119,126,133,147,154,161,168,182,189,196


lst1 =[]
for j in range(1,201):
    if j % 7 == 0:
        if not j % 5 == 0:
            lst1.append(j)
print(lst1)
print(', '.join(map(str,lst1)))