# N개의 숫자가 공백 없이 쓰여있다. 이 숫자를 모두 합해서 출력하는 프로그램을 작성하시오.
# 첫째 줄에 숫자의 개수 N (1 ≤ N ≤ 100)이 주어진다. 둘째 줄에 숫자 N개가 공백없이 주어진다.
# 입력으로 주어진 숫자 N개의 합을 출력한다.
# 예제 입력 1 
# 1
# 1
# 예제 출력 1 
# 1
# 예제 입력 2 
# 5
# 54321
# 예제 출력 2 
# 15

init_num = input()
init_num2 = input()

if int(init_num) ==  len(str(init_num2)):
    result = 0
    for i in init_num2:
        result += int(i)
    print(result)

else:
    pass