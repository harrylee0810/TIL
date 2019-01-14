# 콤마(,)로 구분해 숫자를 입력하고, 입력된 숫자 중 홀수를 콤마(,)로 구분해 출력하는
# 리스트 내포 기능을 이용한 프로그램을 작성하십시오.
# 입력: 1, 2, 3, 4, 5
# 출력: 1, 3, 5

a = list(map(int, input().split(',')))
result = [str(x) for x in a if x % 2 ==1]
print(', '.join(result))
