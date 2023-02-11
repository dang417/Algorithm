n = int(input())

for i in range(n+1):
    num = i
    tmp = 0
    while num > 0:
        tmp += num % 10
        num = num // 10
    if tmp + i == n:
        print(i)
        break
else:
    print(0)