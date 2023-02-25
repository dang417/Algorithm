import sys
sys.stdin = open('input.txt')

n = int(input())

rlt = [n]

for num in range(n, -1, -1):
    num1 = n
    num2 = num
    tmp = [num1, num2]
    while True:
        num1 = num1 - num2
        if num1 >= 0:
            tmp.append(num1)
        else:
            break
        num2 = num2 - num1
        if num2 >= 0:
            tmp.append(num2)
        else:
            break
    if len(tmp) >= len(rlt):
        rlt = tmp

print(len(rlt))
print(*rlt)
