# 다음의 결과와 같이 임의의 양의 정수를 입력받아 그 정수의 모든 약수를 구하십시오

# 입력: 9
# 출력:
# 1(은)는 9의 약수입니다.
# 3(은)는 9의 약수입니다.
# 9(은)는 9의 약수입니다.

init_num = int(input())

for i in range(1,init_num+1):
    if init_num % i == 0:
        print(f'{i}(은)는 {init_num}의 약수입니다.')