import csv

with open('lunch.csv','r',encoding='utf8',newline='') as f:

# #1. 문자열(string)을 통해 읽어오는 방법 
#     lines = f.readlines()
#     for line in lines:
#         print(line.strip().split(','))
#         #내장함수(ex.print)는 개행문자(\n)이포함되어있음
#         #split: 문자열을 어떤기준으로 나눌것인가? string을 나누는 내장함수
#     #string을 이용하면 strip, split 등 추가적인 작업이 많아짐.. 비효율적

#2. 외장 함수 csv를 이용하는 방법 
    items = csv.reader(f)
    for item in items:
        print(item)

