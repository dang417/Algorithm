t = int(input())

def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n-1)

for tc in range(1, t+1):
        r, n = map(int, input().split())
        print(factorial(n)//(factorial(r)*factorial(n-r)))