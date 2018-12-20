# 문제
score = {
    '수학': 80,
    '국어': 90,
    '음악': 100,
}

#1. 이 학생이 평균을 구하시오.

#1-1 풀이 1
total_score = 0
for subject_score in score.values():
    total_score += subject_score

avg_score = total_score / len(score)
print(avg_score)

#1-2 풀이 2
total_score = sum(score.values()) #=> sum([80,90,100]) => 270
avg_score = total_score / len(score)
print(avg_score)