# 리스트 내포 기능을 활용해 입력된 정수 값 5개의 평균을 출력하는 프로그램을 작성하십시오.
# 출력: 입력된 값 [10, 10, 20, 30, 40]의 평균은 22.0입니다.
a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
lst = [a,b,c,d,e]

avg = sum([x for x in lst])/len(lst)
print(f'입력된 값 {lst}의 평균은 {avg}입니다.')