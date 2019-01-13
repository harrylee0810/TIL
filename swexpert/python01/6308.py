# 다음의 결과와 같이 이름과 나이를 입력 받아
# 올해를 기준으로 100세가 되는 해를 표시하는 코드를 작성하십시오.

# 입력:
# 홍길동
# 20
# 출력:
# 홍길동(은) 2098년에 100세가 될 것 입니다.

from datetime import datetime

c_year = datetime.today().year

name = input()
name_year = int(input())
remained_year = 99 - name_year
target_year = remained_year + c_year

print(f'{name}(은)는 {target_year}년에 100세가 될 것입니다.')
