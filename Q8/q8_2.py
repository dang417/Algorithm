m = int(input())
n = int(input())

def isprime(num):
    if num == 1:
        return 0
    for i in range(1,num+1):
        if num % i == 0 and num != i and i != 1:
            return 0
            break
    else :
        return num
        
cnt = 0
rlt = []

for num in range(m,n+1):
    cnt += isprime(num)
    if isprime(num) !=0:
        rlt.append(isprime(num))
if cnt == 0:
    print(-1)
else:
    print(cnt)
    print(min(rlt))