import sys
sys.stdin = open('sample_input.txt')

t = int(input())

for tc in range(1, t+1):
    n = int(input())
    if n == 1:
        print(f'#{tc}', 1)
        continue
    for i in range(1, n):
        if i ** 3 > n:
            print(f'#{tc}', -1)
            break
        elif i ** 3 == n:
            print(f'#{tc}', i)
            break
