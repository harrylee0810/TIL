import os

os.chdir(r'C:\Users\student\harry\day02\dummy')
#print(os.getcwd())
for filename in os.listdir('.'):
    #1. replace 함수이용, 새로운 파일 이름 생성
    new_filename = filename.replace('지원자_지원자','합격자')
    #2. os.rename 함수 이용, 파일 이름 변경
    os.rename(filename, new_filename)

print(os.listdir())
