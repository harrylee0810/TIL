# 20% 농도의 소금물 100g과 물 200g을 혼합한 소금물의 농도(%)를 
# 소수점 두 번째 자리까지 구하는 프로그램을 작성하십시오.

# 입력:
# 출력: 혼합된 소금물의 농도: 6.67%

# nong, s_water, water = map(int,input().split())

nong = 20
s_water = 100
water =200

salt = nong * s_water
total_water = s_water + water
total_nong = salt / total_water

print(f'혼합된 소금물의 농도: {total_nong:0.2f}%')