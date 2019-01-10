# 다음은 10명의 학생들의 혈액형(A, B, AB, O) 데이터입니다.
# ['A', 'A', 'A', 'O', 'B', 'B', 'O', 'AB', 'AB', 'O']
# for 문을 이용하여 각 혈액형 별 학생수를 구하십시오.

# 입력: 입력값 없음
# 출력: {'A': 3, 'O': 3, 'B': 2, 'AB': 2}

a = ['A', 'A', 'A', 'O', 'B', 'B', 'O', 'AB', 'AB', 'O']

result = {}
for i in a:
    result[i] = a.count(i)

print(result)
