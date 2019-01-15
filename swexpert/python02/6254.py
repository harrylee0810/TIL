# 다음과 같이 등록된 학생의 이름을 출력하고, 이름을 입력하면 전화번호를 출력해주는
# 딕셔너리 객체를 이용한 전화번호부 프로그램을 작성하십시오.

# [등록된 학생]
# 홍길동: 010-1111-1111
# 이순신: 010-1111-2222
# 강감찬: 010-1111-3333

# [프로그램]
# 아래 학생들의 전화번호를 조회할 수 있습니다.
# 홍길동
# 이순신
# 강감찬
# 전화번호를 조회하고자 하는 학생의 이름을 입력하십시오.

# 입력: 이순신
# 출력:
# 아래 학생들의 전화번호를 조회할 수 있습니다.
# 홍길동
# 이순신
# 강감찬
# 전화번호를 조회하고자 하는 학생의 이름을 입력하십시오.
# 이순신의 전화번호는 010-1111-2222입니다.

a = {'홍길동': '010-1111-1111',
    '이순신': '010-1111-2222',
    '강감찬': '010-1111-3333'}

b = input()

print('아래 학생들의 전화번호를 조회할 수 있습니다.\n홍길동\n이순신\n강감찬\n전화번호를 조회하고자 하는 학생의 이름을 입력하십시오.')
print(f'{b}의 전화번호는 {a[b]}입니다.')