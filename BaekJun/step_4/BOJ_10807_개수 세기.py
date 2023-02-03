n = int(input())
num = list(map(int,input().split()))
v = int(input())
count = 0
while v in num :
    if v in num :
        count = count + 1
        num.remove(v)
print(count)

