# 다음의 결과와 같이 5명의 학생의 점수에 대해 60 이상일 때 합격 메시지를 출력하고,
# 60미만일 때 불합격 메시지를 출력하는 프로그램을 만드십시오.

# 입력: 입력값 없음
# 출력: 
# 1번 학생은 88점으로 합격입니다.
# 2번 학생은 30점으로 불합격입니다.
# 3번 학생은 61점으로 합격입니다.
# 4번 학생은 55점으로 불합격입니다.
# 5번 학생은 95점으로 합격입니다.

a = [88, 30, 61, 55, 95]
count = 0
for i in a:
    if int(i) > 60:
        count += 1
        print(f'{count}번 학생은 {i}점으로 합격입니다.')
    else:
        count += 1
        print(f'{count}번 학생은 {i}점으로 불합격입니다.')
