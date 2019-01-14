# 한 학생의 국어, 수학 점수를 튜플로 저장하고 이 튜플을 항목으로 갖는 리스트 객체가 있습니다.
# 이 때 첫 번째 학생은 (90, 80), 두 번째 학생은 (85, 75), 세 번째 학생은 (90, 100)의 점수를 갖습니다.
# 다음과 같이 결과를 만들기 위한 프로그램을 작성하십시오.

# 출력:
# 1번 학생의 총점은 170점이고, 평균은 85.0입니다.
# 2번 학생의 총점은 160점이고, 평균은 80.0입니다.
# 3번 학생의 총점은 190점이고, 평균은 95.0입니다.

lst = [(90,80), (85, 75), (90, 100)]
for i in range(len(lst)):
    print(f'{i+1}번 학생의 총점은 {lst[i][0]+lst[i][1]}점이고, 평균은 {(lst[i][0]+lst[i][1])/2}입니다.')