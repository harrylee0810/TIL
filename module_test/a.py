# 1. 직접 실행
# __name__ == '__main__'  => 이부분은 파이썬이 직접 실행
# 2. import
# __name__ = 'a' => import 하는 경우는 main이 a로 바뀜.


if __name__ == '__main__':
    print('a.py를 직접 실행')
else:
    print('a.py가 import 되어 실행')