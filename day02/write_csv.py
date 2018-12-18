lunch = {
    '맥도날드':'051-327-7864',
    '롯데리아':'051-333-4444',
    '버거킹':'051-123-1234'
}

import csv


with open('lunch.csv','w',encoding = 'utf8',newline='') as f:
    csv_writer = csv.writer(f) 

    for item in lunch.items(): #리스트 [(key,value), ...]
        csv_writer.writerow(item)
        #f.write(f'{item[0]},{item[1]}\n')

#줄바꿈이 두번생기는 이유? with open()에서도 라인을 우선 하나 생성하고, writerow에서도 라인을 추가로 생성하기 때문.
#이경우, open()안에 newline=''을 넣어서 with open()에서 생기는 라인을 없앨 수 있다.