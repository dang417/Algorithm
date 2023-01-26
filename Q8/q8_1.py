num = int(input())
numbers = list(map(int,input().split()))

for j in numbers:
    for i in range(1,1000+1):
        if j % i == 0:
            num = num - 1
print(num)

