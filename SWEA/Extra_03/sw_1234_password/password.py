import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    n, number = input().split()
    n = int(n)

    while True:
        for i in range(n-2):
            if number[i] == number[i+1]:
                number = number[:i] + number[i+2:]
                n -= 2
                break
        else:
            break

    if number[-2] == number[-1]:
        number = number[:-2]

    print(f'#{tc}', number)



