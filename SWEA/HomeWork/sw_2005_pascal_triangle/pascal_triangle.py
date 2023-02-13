import sys
sys.stdin = open('input.txt')

def pascal_triangle(n):
    if n == 1:
        a = [1]
        return a
    a = [0] * n
    a[0] = a[-1] = 1
    for i in range(0, n-2):
        a[i+1] = pascal_triangle(n-1)[i] + pascal_triangle(n-1)[i+1]
    return a

t = int(input())

for tc in range(1, t+1):
    n = int(input())
    print(f'#{tc}')
    for i in range(1, n+1):
        print(*pascal_triangle(i))
