# 다음의 결과와 같이 입력된 영어 알파벳 문자에 대해 
# 대소문자를 구분하는 코드를 작성하십시오.

# 입력: b
# 출력: b 는 소문자 입니다.

# print(ord("A")) #=> 65
# print(ord("Z")) #=> 90

# print(ord("a"))  #=> 97
# print(ord("z"))  #=> 122

a = input()
if 65 <= ord(a) <= 90:
    print('{} 는 대문자 입니다.'.format(a))
elif 97 <= ord(a) <= 122:
    print('{} 는 소문자 입니다.'.format(a))