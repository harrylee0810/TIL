# 1부터 100사이의 숫자 중 홀수를 for 문을 이용해 다음과 같이 출력하십시오.
# 입력:
# 입력값 없음
# 출력
# 1, 3, 5, 7, 9, ... 95, 97, 99

lst= []
for i in range(1, 100, 2):
    lst.append(i)
print(', '.join(map(str,lst)))