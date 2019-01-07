# 섭씨(℃)를 화씨(℉)로 변환하는 프로그램을 작성하십시오.
# 이 때 물의 빙점은 화씨 32도이고 비등점은 화씨 212도(표준 기압에서)입니다.
# 물의 비등점과 빙점 사이에 정확하게 180도 차이가 납니다.
# 그러므로 화씨 눈금에서의 간격은 물의 빙점과 비등점 사이의 간격의 1/180입니다.

# 입력: 28
# 출력: 28.00 ℃ =>  82.40 ℉

# 화씨(C): 0C 100C (100등분)
# 섭씨(F): 32F 212F (180등분)

# F = 32 + (C*1.8 => 180/100)

temp_c = float(input())
temp_c2  = format(temp_c , '.2f')
temp_f = (temp_c*1.8) + 32
temp_f2 = format(temp_f , '.2f')

print(f'{temp_c2} ℃  =>  {temp_f2} ℉')