# 인치(inch)를 센티미터(cm)으로 변환하는 프로그램을 작성하십시오.
# 이 때 1 인치는 2.54 센티미터입니다.

# 입력: 3
# 출력: 3.00 inch =>  7.62 cm


init_num = float(input())
init_num2 = '%.2f'% init_num
converted_num = 2.54 * init_num
converted_num2 = '%.2f'% converted_num
print(f'{init_num2} inch =>  {converted_num2} cm')

