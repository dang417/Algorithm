import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    n, number = input().split()
    n = int(n)
    a = ''
    for i in range(n-1):
        if number[i] == number[i+1]:
            j = 1
            k = i
            while number[k] == number[k+j]:
                number = number.replace(number[k], 'x')
                number = number.replace(number[k+j], 'x')
                j += 2
                k -= 1

    print(a)


