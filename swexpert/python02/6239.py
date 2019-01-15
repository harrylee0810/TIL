# 다음과 같이 문장을 구성하는 단어를 역순으로 출력하는 프로그램을 작성하십시오.
# 입력: A better tomorrow
# 출력: tomorrow better A

a = list(map(str, input().split()))
a.reverse()
print(' '.join(a))
