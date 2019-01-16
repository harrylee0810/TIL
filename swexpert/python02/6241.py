# 다음의 결과와 같이 임의의 URL 주소를 입력받아 protocol, host, 나머지(path, querystring, ...)로
# 구분하는 프로그램을 작성하십시오.

# 입력: http://www.example.com/test?p=1&q=2

# 출력
# protocol: http
# host: www.example.com
# others: test?p=1&q=2

import re
a = ['protocol', 'host' , 'others']
b = re.split(':|\/',input())
c = []
for i in b:
    if bool(i) == True:
        c.append(i)
    else:
        continue

for k in range(len(a)):
    print(f'{a[k]}: {c[k]}')






