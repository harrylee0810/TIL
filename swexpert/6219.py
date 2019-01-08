# 다음의 결과와 같이 임의의 양의 정수를 입력받아 그 정수의 모든 약수를 구하십시오
# (단, 약수가 2개일 경우 소수임을 나타내십시오)

# 입력: 5
# 출력:
# 1(은)는 5의 약수입니다.
# 5(은)는 5의 약수입니다.
# 5(은)는 1과 5로만 나눌 수 있는 소수입니다.

init_num = int(input())
lst =[]
for i in range(1, init_num+1):
    if init_num % i == 0:
        lst.append(i)

for k in lst:
    print(f'{k}(은)는 {init_num}의 약수입니다.')

if len(lst) == 2:
    print(f'{init_num}(은)는 {lst[0]}과 {lst[1]}로만 나눌 수 있는 소수입니다.')        
    