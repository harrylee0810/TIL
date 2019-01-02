# 두 개의 정수 n과 m이 주어집니다. 반복문을 사용하지 않고 
# 별(*) 문자를 이용해 가로 의 길이가 n, 세로의 길이가 m인 직사각형 형태를 출력해보세요

n = 5
m = 9
print(('*'*n+'\n')*m)


# 다음 딕셔너리에서 평균 점수를 출력하시오.
student = {'python' : 80, 'algorithm' : 99, 'django':89,'flask':83}
total_scores = sum(student.values())
avg_scores = total_scores / len(student)
print(avg_scores)


t_score = 0
for s_score in student.values():
    t_score += s_score

average_score = t_score / len(student)
print(average_score)


# 다음은 학생들의 혈액형(A, B, AB, O)에 대한 데이터이다. 
# for문을 이용하여 각 혈액형 별 학생수의 합계를 구하시오.

blood_types = ['A','B','A','O','AB','AB','O','A','B','O','B','AB']

a = 0
b = 0
ab = 0
o = 0
for n in blood_types:
    if n == "A":
        a += 1
    elif n == "B":
        b += 1
    elif n == "AB":
        ab += 1
    else:
        o += 1

print(f'각 혈액형의 학생수는 A형:{a}명, B형:{b}명, AB형:{ab}명, O형:{o}명 입니다')
print(f'B형의 학생수는 {b}입니다')   
print(f'AB형의 학생수는 {ab}입니다')
print(f'O형의 학생수는 {o}입니다')

print(blood_types.count('A'))
print(blood_types.count('AB'))
print(blood_types.count('B'))
print(blood_types.count('O'))
