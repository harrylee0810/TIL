# "ADCBBBBCABBCBDACBDCAACDDDCAABABDBCBCBDBDBDDABBAAAAAAADADBDBCBDABADCADC"와
# 같은 문자열이 주어지고, A는 4점, B는 3점, C는 2점, D는 1점이라고 할 때 문자열에 사용된
# 알파벳 점수의 총합을 map 함수와 람다식을 이용해 구하십시오.

# 출력: 184

a = "ADCBBBBCABBCBDACBDCAACDDDCAABABDBCBCBDBDBDDABBAAAAAAADADBDBCBDABADCADC"

map_result = list(set(map(lambda x: a.count('A')*4 + a.count('B')*3 + a.count('C')*2 + a.count('D')*1 , a)))
for i in map_result:
    print(i)


# total = a_total + b_total + c_total + d_total
# print(total)