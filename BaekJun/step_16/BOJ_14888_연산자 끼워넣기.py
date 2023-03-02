import sys
sys.stdin = open('input.txt')

from collections import deque

def calc(x, y, ope):
    while operator:
        o = ope.popleft()
        if o == '+':
            return x + y
        if o == '-':
            return x - y
        if o == '*':
            return x * y
        if o == '/':
            if x < 0:
                return -((-x)//y)
            else:
                return x // y

def oper(arr):
    global oper_list
    if len(arr) == n-1:
        oper_list.append(deque(arr))
        return
    for i in '+-*/':
        if operator[i]:
            operator[i] -= 1
            arr.append(i)
            oper(arr)
            operator[i] += 1
            arr.pop()

n = int(input())
numbers = list(map(int, input().split()))
visited = [0] * (n-1)
tmp = list(map(int, input().split()))
oper_list = deque([])
operator = {'+' : tmp[0], '-' : tmp[1], '*' : tmp[2], '/' : tmp[3]}
oper([])
max_rlt = -10000000001
min_rlt = 10000000001

for j in range(len(oper_list)):
    num = numbers[::]
    for i in range(n-1):
        num[i+1] = calc(num[i], num[i+1], oper_list[j])
    if num[-1] >= max_rlt:
        max_rlt = num[-1]
    if num[-1] <= min_rlt:
        min_rlt = num[-1]

print(max_rlt)
print(min_rlt)