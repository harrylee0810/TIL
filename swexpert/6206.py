# 킬로그램(kg)를 파운드(lb)으로 변환하는 프로그램을 작성하십시오.
# 이 때 1 킬로그램은 2.2046 파운드입니다.
# 입력: 90
# 출력: 90.00 kg =>  198.41 lb


init_num = float(input())
init_num2 = '%.2f'% init_num
converted_num = init_num * 2.2046
converted_num2 = format(converted_num, '.2f')
print(f'{init_num2} kg =>  {converted_num2} lb')