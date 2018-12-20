# 문제2 반 평균을 구하시오.

scores = {
    'a' : {
        '수학': 80,
        '국어': 90,
        '음악': 70,
    },

    'b' : {
        '수학': 80,
        '국어': 90,
        '음악': 100,
    }

}

total_score = 0
count = 0 #과목의 갯수를 저장하는 변수

#scores.values() #=> [{수학': 80, '국어': 90,'음악': 70}, {수학': 80, '국어': 90,'음악': 100}] 각각의 딕셔너리가 리스트안에 들어가게됨.

for person_score in scores.values():
    # 1번째 시행
    # person_score #=> {수학': 80, '국어': 90,'음악': 70}
    # person_score.values() #=> [80,90.70]
    for subject_score in person_score.values():
        # 1번째 시행
        # subject_score #=> 80, total_score #=> 80, count = 1
        total_score += subject_score
        count += 1
        # 2번째 시행
        # subject_score #=> 90, total_score #=> 80 + 90 , count = 2
    # 2번째 시행
    # person_score #=> {수학': 80, '국어': 90,'음악': 100}
    # person_score.values() #=> [80,90.100]

avg_score = total_score / count
print(avg_score)