# 다음 결과와 같이 문자열을 입력하면 짝수 인덱스를 가진 문자들을 출력하는 프로그램을 작성하십시오.
# 입력:
# H1e2l3l4o5w6o7r8l9d
# 출력:
# Helloworld
a = input()
b =''
for i in range(0,len(a),2):
    b+=a[i]
print(b)