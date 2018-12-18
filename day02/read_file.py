with open('ssafy.txt','r',encoding='utf8') as f:
    lines = f.readlines()
    print(lines)
    for line in lines:
    #    print(line.strip()) #strip: 공백지우기