# 1부터 100사이의 숫자 중 짝수를 for 문을 이용해 다음과 같이 출력하십시오.
# 입력: 입력값 없음
# 출력: 2 4 6 8 10 12 14 16 18 ... 90 92 94 96 98 100

lst =[] 
for i in range(2,101,2):
    lst.append(i)
print(' '.join(map(str,lst)))
