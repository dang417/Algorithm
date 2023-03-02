import sys
sys.stdin = open('input.txt')

def fib(n):
    cnt[0] += 1
    if n == 1 or n == 2:
        cnt[0] -=1
        return 1
    else:
        return fib(n-1) + fib(n-2)


def fibo(n):
    f[1], f[2] = 1, 1
    for i in range(3, n+1):
        cnt[1] += 1
        f[i] = f[i-1] + f[i-2]
    return f[n]

n = int(input())
f = [0] * (n+1)
cnt = [0, 0]

fib(n)
fibo(n)

print(cnt[0] + 1, cnt[1])