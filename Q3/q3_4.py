x = int(input())
n = int(input())
c = 0
for i in range(1,n+1) :
    a,b = map(int,input().split())
    c = c + a * b

if x == c :
    print('Yes')
else :
    print('No')