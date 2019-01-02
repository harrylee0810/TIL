A = int(input())

if A % 5 == 0:
    print(A//5)
elif A % 5 == 3:
    print(A//5 + 1)
elif A % 3 == 0:
    print(A//3)
else:
    print('-1')

A = int(input())
n = (A//5)+1
count = 0
for i in range(n):
    if (A-(5*(n-i-1)))%3 == 0:
        print((n-i-1)+(A-(5*(n-i-1)))//3)
        count += 1
        break
if count == 0: 
    print(-1)


n = int(input())
Five = n//5
n = n%5
Three = 0
 
while Five >= 0:
  if n % 3 == 0:
    Three = n // 3
    n = n % 3
    break
  Five -= 1
  n += 5
print((n==0) and (Five + Three) or -1)


N=int(input())
a = int(N/5)
b = N%5

if b==0:
    print(a)
elif b==3:
    print(a+1)
else:
    if a>0:
        if b==1:
            print(a+1)
        elif b==4:
            print(a+2)
        else:
            if a>1:
                print(a+2)
            else:
                print("-1")        
    else:
        print("-1") 