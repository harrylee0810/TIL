# f = open('ssafy.txt','w') #w: write, r: read, a: append
# f.write('This is SSAFY!')
# f.close() #close를 꼭 넣어야 정상적으로 종료가 됨!!! (열려있으니까 닫아야함. 추가로 open()을 쓸 경우 열려있다는 에러가 뜰 수 있음.)

with open('ssafy.txt','w',encoding='utf8') as f:
    f.writelines(['1\n','2\n','3\n'])
    # for i in range(10):
    #    f.write(f'This is \'SSAFY!\' {i}\n')
    #    #\t : tab, \\ : '\'문자, \' & \" : 따옴표 & 쌍따옴표 문자
 

